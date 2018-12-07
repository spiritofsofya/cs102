import datetime as dt
import time
from statistics import median
from typing import Optional

from api import get_friends
from api_models import User


def age_predict(user_id: int) -> Optional[float]:
    """ Наивный прогноз возраста по возрасту друзей

    Возраст считается как медиана среди возраста всех друзей пользователя

    :param user_id: идентификатор пользователя
    :return: медианный возраст пользователя
    """
    assert isinstance(user_id, int), "user_id must be positive integer"
    assert user_id > 0, "user_id must be positive integer"
    # assert проверка условий

    current_date = dt.date.today()
    # метод встроенный данная дата
    friends = [User(**i) for i in get_friends(user_id, 'bdate')]
    # перебор друзей по id, создаем список дат
    for friend in friends:
        birthday = friend.bdate
        try:
            # выполнение инструкций, если исключение - пропуск
            bd = time.strptime(birthday, "%d, %m, %Y")
        except (ValueError, TypeError):
            pass
        else:
            ages = []
            age = current_date.year - bd.year - ((current_date.month, current_date.day) < (bd.month, bd.day))
            ages.append(age)
    return float(median())


