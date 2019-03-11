from bottle import route, run, template, request, redirect

from scraputils import get_news
from db import News, session, fill
from bayes import NaiveBayesClassifier, clean


@route("/news")
def news_list():
    s = session()
    rows = s.query(News).filter(News.label == None).all()
    return template('news_template', rows=rows)


@route("/add_label/")
def add_label():
    label = request.query.label
    row_id = request.query.id
    row = s.query(News).filter(News.id == row_id).one()
    row.label = label
    s.commit()
    if request.query.classify == 'True':
        redirect('/classify')
    else:
        redirect('/news')


@route("/update")
def update_news():
    recent_news = get_news()
    authors = [news['author'] for news in recent_news]
    titles = s.query(News.title).filter(News.author.in_(authors)).subquery()
    existing_news = s.query(News).filter(News.title.in_(titles)).all()
    titles_bd = [i.title for i in existing_news]
    authors_bd = [i.author for i in existing_news]
    for news in recent_news:
        if not existing_news or (news['title'] not in titles_bd and news["author"] not in authors_bd):
            fill(news)
    redirect("/news")


@route('/recommendations')
def recommendations():
    # 1. Classify labeled news
    rows = s.query(News).filter(News.label != None).all()

    x, y = [], []
    for row in rows:
        x.append(row.title)
        y.append(row.label)

    x = [clean(x).lower() for x in X]

    model = NaiveBayesClassifier()
    model.fit(x, y)

    # 2. Get unlabeled news
    new_rows = s.query(News).filter(News.label == None).all()

    # 3. Get predictions
    marked = []
    for row in new_rows:
        marked.append((model.predict(row.title.split()), row))

    # 4. Print ranked table
    return template('news_recommendations', rows=marked)


if __name__ == "__main__":
    s = session()
    classifier = NaiveBayesClassifier()
    marked_news = s.query(News).filter(News.label != None).all()
    x_train = [row.title for row in marked_news]
    y_train = [row.label for row in marked_news]
    classifier.fit(x_train, y_train)
    run(host="localhost", port=8081)

