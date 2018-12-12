import requests
import config
import telebot
import time
import datetime
from bs4 import BeautifulSoup


bot = telebot.TeleBot(config.access_token)
week_list = ['/monday', '/tuesday', '/wednesday', '/thursday', '/friday', '/saturday']


@bot.message_handler(commands=['start'])
def greeting(message):
    bot.send_message(message.chat.id, 'Список команд: \n \
    /monday GROUP, WEEK - расписание на пн (остальные дни аналогично) (недели: 1-чет, 2-нечет, пусто-обе) \n \
    /near GROUP - следующая пара \n \
    /tomorrow GROUP - расписание на завтра \n \
    /all GROUP - полное расписание группы')


def get_page(group, week=''):
    if week:
        week = str(week) + '/'
    url = '{domain}/{group}/{week}raspisanie_zanyatiy_{group}.htm'.format(
        domain=config.domain,
        week=week,
        group=group)
    response = requests.get(url)
    web_page = response.text
    return web_page


def get_schedule(web_page, day):
    soup = BeautifulSoup(web_page, "html5lib")

    # Получаем таблицу с расписанием на день недели
    if day in week_list:
        number = str(week_list.index(day) + 1) + 'day'
    else:
        number = '1day'
    schedule_table = soup.find('table', attrs={'id': number})
    if not schedule_table:
        return None

    # Время проведения занятий
    times_list = schedule_table.find_all("td", attrs={"class": "time"})
    times_list = [time.span.text for time in times_list]

    # Место проведения занятий
    locations_list = schedule_table.find_all("td", attrs={"class": "room"})
    locations_list = [room.span.text for room in locations_list]

    # Название дисциплин и имена преподавателей
    lessons_list = schedule_table.find_all("td", attrs={"class": "lesson"})
    lessons_list = [lesson.text.replace('\n', '').replace('\t', '') for lesson in lessons_list]

    return times_list, locations_list, lessons_list


@bot.message_handler(commands=['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday'])
def get_day(message):
    try:
        day, week, group = message.text.split()
    except bot.send_message(message.chat.id, 'Данные введены неверно или не полностью.'):
        return None
    week = str(week)
    web_page = get_page(group, week)
    schedule = get_schedule(web_page, day)
    if not schedule:
        bot.send_message(message.chat.id, 'Данные введены неверно или в указанный день у группы нет занятий')
        return None

    times_lst, locations_lst, lessons_lst = schedule

    resp = ''
    for time, location, lesson in zip(times_lst, locations_lst, lessons_lst):
        resp += '<b>{}</b>, {}, {}\n'.format(time, location, lesson)

    bot.send_message(message.chat.id, resp, parse_mode='HTML')


@bot.message_handler(commands=['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'])
def get_schedule(message):
    """ Получить расписание на указанный день """

    pass


@bot.message_handler(commands=['near'])
def get_near_lesson(message):
    """ Получить ближайшее занятие """
    # PUT YOUR CODE HERE
    pass


@bot.message_handler(commands=['tommorow'])
def get_tommorow(message):
    """ Получить расписание на следующий день """
    # PUT YOUR CODE HERE
    pass


@bot.message_handler(commands=['all'])
def get_all_schedule(message):
    """ Получить расписание на всю неделю для указанной группы """
    # PUT YOUR CODE HERE
    pass


if __name__ == '__main__':
    bot.polling(none_stop=True)

