import requests
from bs4 import BeautifulSoup


def extract_news(parser):
    """ Extract news from a given web page """
    news_list = []
    table_list = parser.table.findAll('table')
    news_table = table_list[1]
    all_rows = news_table.findAll('td')[:90]
    news_rows = (all_rows[i], all_rows[i + 1] for i in range(90) if i % 3 == 0)
    for news in news_rows:
        first_line = news[0].findAll('td')[2]
        second_line = news[1].findAll('td')[1]

        comments_str = second_line.findAll('a')[-1].text
        if comments_str == "discuss":
            comments_int = 0
        else:
            comments_int = int(comments_str[0])

        points = int(second_line.span.text[0])
        link = str(first_line.a)[27:]
        href_end = link.find('"')
        href = link[:href_end]
        if 'http' not in href:
            url = 'https://news.ycombinator.com/' + href
        else:
            url = href

        news_dict = {'author': second_line.a.text,
                     'comments': comments_int,
                     'points': points,
                     'title': str(first_line.a.text),
                     'url': url
                     }
        news_list.append(news_dict)
    return news_list


def extract_next_page(parser):
    """ Extract next page URL """
    # PUT YOUR CODE HERE


def get_news(url, n_pages=1):
    """ Collect news from a given web page """
    news = []
    while n_pages:
        print("Collecting data from page: {}".format(url))
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        news_list = extract_news(soup)
        next_page = extract_next_page(soup)
        url = "https://news.ycombinator.com/" + next_page
        news.extend(news_list)
        n_pages -= 1
    return news

