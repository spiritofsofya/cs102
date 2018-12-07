from collections import Counter
import datetime
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
from typing import List, Tuple

from api import messages_get_history
from api_models import Message
import config


Dates = List[datetime.date]
Frequencies = List[int]


plotly.tools.set_credentials_file(
    username=config.PLOTLY_CONFIG['username'],
    api_key=config.PLOTLY_CONFIG['api_key']
)


def fromtimestamp(ts: int) -> datetime.date:
    return datetime.datetime.fromtimestamp(ts).date()


def count_dates_from_messages(messages: List[Message]) -> Tuple[Dates, Frequencies]:
    """ Получить список дат и их частот

    :param messages: список сообщений
    """
    c = Counter()
    # counter() считает количество повторяющихся дат сообщений
    for message in messages:
        date = fromtimestamp(message.date)
        c[date] += 1
    result = list(zip(*c.most_common()))
    # * превращает интератор в отдельные аргументы
    # zip(a, b) создает объект-итератор,
    # из которого при каждом обороте цикла извлекается кортеж, состоящий из двух элементов
    return tuple((sorted(result[0]), [c[date] for date in sorted(result[0])]))


def plotly_messages_freq(dates: Dates, freq: Frequencies) -> None:
    """ Построение графика с помощью Plot.ly

    :param date: список дат
    :param freq: число сообщений в соответствующую дату
    """
    # PUT YOUR CODE HERE
