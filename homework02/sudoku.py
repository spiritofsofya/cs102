<<<<<<< HEAD
def read_sudoku(filename):
=======
from typing import List, Union, Optional, Union
import random


def read_sudoku(filename: str) -> list:
>>>>>>> develop
    """ Прочитать Судоку из указанного файла """
    digits = [c for c in open(filename).read() if c in '123456789.']
    grid = group(digits, 9)
    return grid


<<<<<<< HEAD
def display(values):
=======
def display(values: list) -> None:
>>>>>>> develop
    """Вывод Судоку """
    width = 2
    line = '+'.join(['-' * (width * 3)] * 3)
    for row in range(9):
<<<<<<< HEAD
        print(''.join(values[row][col].center(width) + ('|' if str(col) in '25' else '') for col in range(9)))
=======
        print(''.join(values[row][col].center(width) +
                      ('|' if str(col) in '25' else '') for col in range(9)))
>>>>>>> develop
        if str(row) in '25':
            print(line)
    print()


<<<<<<< HEAD
def group(values, n):
=======
def group(values: list, n: int) -> list:
>>>>>>> develop
    """
    Сгруппировать значения values в список, состоящий из списков по n элементов
    >>> group([1,2,3,4], 2)
    [[1, 2], [3, 4]]
    >>> group([1,2,3,4,5,6,7,8,9], 3)
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    """
<<<<<<< HEAD
    pass


def get_row(values, pos):
=======
    a = []
    for i in range(0, len(values), n):
        a.append(values[i:i + n])
    return a


def get_row(values: List[list], pos: tuple) -> list:
>>>>>>> develop
    """ Возвращает все значения для номера строки, указанной в pos
    >>> get_row([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '2', '.']
    >>> get_row([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 0))
    ['4', '.', '6']
    >>> get_row([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 0))
    ['.', '8', '9']
    """
<<<<<<< HEAD
    pass


def get_col(values, pos):
=======
    row, _ = pos
    return values[row]


def get_col(values: list, pos: tuple) -> list:
>>>>>>> develop
    """ Возвращает все значения для номера столбца, указанного в pos
    >>> get_col([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '4', '7']
    >>> get_col([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (0, 1))
    ['2', '.', '8']
    >>> get_col([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (0, 2))
    ['3', '6', '9']
    """
<<<<<<< HEAD
    pass


def get_block(values, pos):
=======
    _, col = pos
    b = []
    for row in range(len(values)):
        b.append(values[row][col])
    return b


def get_block(values: list, pos: tuple) -> list:
>>>>>>> develop
    """ Возвращает все значения из квадрата, в который попадает позиция pos
    >>> grid = read_sudoku('puzzle1.txt')
    >>> get_block(grid, (0, 1))
    ['5', '3', '.', '6', '.', '.', '.', '9', '8']
    >>> get_block(grid, (4, 7))
    ['.', '.', '3', '.', '.', '1', '.', '.', '6']
    >>> get_block(grid, (8, 8))
    ['2', '8', '.', '.', '.', '5', '.', '7', '9']
    """
<<<<<<< HEAD
    pass


def find_empty_positions(grid):
    """ Найти первую свободную позицию в пазле
    >>> find_empty_positions([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']])
    (0, 2)
    >>> find_empty_positions([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']])
    (1, 1)
    >>> find_empty_positions([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']])
    (2, 0)
    """
    pass


def find_possible_values(grid, pos):
=======
    row, col = pos
    d = []
    block_row = 3 * (row // 3)
    block_col = 3 * (col // 3)
    for r in range(3):
        for c in range(3):
            d.append(values[block_row+r][block_col+c])
    return d


def find_empty_positions(grid: list) -> Union[tuple, None]:
    """ Найти первую свободную позицию в пазле
    >>> find_empty_positions([['1', '2', '.'], ['4', '5', '6'], /
    ['7', '8', '9']])(0, 2)
    >>> find_empty_positions([['1', '2', '3'], ['4', '.', '6'], /
    ['7', '8', '9']])(1, 1)
    >>> find_empty_positions([['1', '2', '3'], ['4', '5', '6'], /
    ['.', '8', '9']])(2, 0)
    """
    for row in range(len(grid)):
        for col in range(len(grid)):
            if grid[row][col] == ".":
                return (row, col)
    return None


def find_possible_values(grid: list, pos: tuple) -> set:
>>>>>>> develop
    """ Вернуть множество возможных значения для указанной позиции
    >>> grid = read_sudoku('puzzle1.txt')
    >>> values = find_possible_values(grid, (0,2))
    >>> values == {'1', '2', '4'}
    True
    >>> values = find_possible_values(grid, (4,7))
    >>> values == {'2', '5', '9'}
    True
    """
<<<<<<< HEAD
    pass


def solve(grid):
    """ Решение пазла, заданного в grid """
    """ Как решать Судоку?
        1. Найти свободную позицию
        2. Найти все возможные значения, которые могут находиться на этой позиции
=======
    possible = set('123456789')
    unigue_r = set(get_row(grid, pos))
    unigue_c = set(get_col(grid, pos))
    unigue_b = set(get_block(grid, pos))
    t = possible - unigue_r - unigue_c - unigue_b
    return t


def solve(grid: list) -> Union[list, None]:
    """ Решение пазла, заданного в grid """
    """ Как решать Судоку?
        1. Найти свободную позицию
        2. Найти все возможные значения,
        которые могут находиться на этой позиции
>>>>>>> develop
        3. Для каждого возможного значения:
            3.1. Поместить это значение на эту позицию
            3.2. Продолжить решать оставшуюся часть пазла
    >>> grid = read_sudoku('puzzle1.txt')
    >>> solve(grid)
<<<<<<< HEAD
    [['5', '3', '4', '6', '7', '8', '9', '1', '2'], ['6', '7', '2', '1', '9', '5', '3', '4', '8'], ['1', '9', '8', '3', '4', '2', '5', '6', '7'], ['8', '5', '9', '7', '6', '1', '4', '2', '3'], ['4', '2', '6', '8', '5', '3', '7', '9', '1'], ['7', '1', '3', '9', '2', '4', '8', '5', '6'], ['9', '6', '1', '5', '3', '7', '2', '8', '4'], ['2', '8', '7', '4', '1', '9', '6', '3', '5'], ['3', '4', '5', '2', '8', '6', '1', '7', '9']]
    """
    pass


def check_solution(solution):
    """ Если решение solution верно, то вернуть True, в противном случае False """
    # TODO: Add doctests with bad puzzles
    pass


def generate_sudoku(N):
=======
    [['5', '3', '4', '6', '7', '8', '9', '1', '2'], /
    ['6', '7', '2', '1', '9', '5', '3', '4', '8'], /
    ['1', '9', '8', '3', '4', '2', '5', '6', '7'], /
    ['8', '5', '9', '7', '6', '1', '4', '2', '3'], /
    ['4', '2', '6', '8', '5', '3', '7', '9', '1'], /
    ['7', '1', '3', '9', '2', '4', '8', '5', '6'], /
    ['9', '6', '1', '5', '3', '7', '2', '8', '4'], /
    ['2', '8', '7', '4', '1', '9', '6', '3', '5'],/
     ['3', '4', '5', '2', '8', '6', '1', '7', '9']]
    """
    position = find_empty_positions(grid)
    if not position:
        return grid
    row, col = position
    for value in find_possible_values(grid, position):
        grid[row][col] = value
        result = solve(grid)
        if result:
            return result
    grid[row][col] = '.'
    return None


def check_solution(solution: list) -> bool:
    """ Если решение solution верно, то вернуть True,
        в противном случае False """
    for row in range(len(solution)):
        r_val = set(get_row(solution, (row, 0)))
        if r_val != set('123456789'):
            return False

    for col in range(len(solution)):
        c_val = set(get_col(solution, (0, col)))
        if c_val != set('123456789'):
            return False

    for row in (0, 3, 6):
        for col in (0, 3, 6):
            b_val = set(get_block(solution, (row, col)))
            if b_val != set('123456789'):
                return False
    return True


def generate_sudoku(t: int) -> list:
>>>>>>> develop
    """ Генерация судоку заполненного на N элементов
    >>> grid = generate_sudoku(40)
    >>> sum(1 for row in grid for e in row if e == '.')
    41
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    >>> grid = generate_sudoku(1000)
    >>> sum(1 for row in grid for e in row if e == '.')
    0
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    >>> grid = generate_sudoku(0)
    >>> sum(1 for row in grid for e in row if e == '.')
    81
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    """
<<<<<<< HEAD
    pass
=======
    grid_s = solve([['.'] * 9 for _ in range(9)])
    t = 81 - min(81, max(0, t))
    while t:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if grid_s[row][col] != '.':
            grid_s[row][col] = '.'
            t -= 1
    return grid_s
>>>>>>> develop


if __name__ == '__main__':
    for fname in ['puzzle1.txt', 'puzzle2.txt', 'puzzle3.txt']:
<<<<<<< HEAD
        grid = read_sudoku(fname)
        display(grid)
        solution = solve(grid)
        display(solution)
=======
        grid_d = read_sudoku(fname)
        display(grid_d)
        solution = solve(grid_d)
        display(solution)
>>>>>>> develop
