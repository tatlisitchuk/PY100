# from begin import ROW, COLUMN
ROW = 3
COLUMN = 3

actions = {1:[], 2:[]}  #ключ - это номер игрока (1 и 2), значение - лист с номерами его ячеек
actions_for_picture = {}  #ключ - это номер ячейки, значение - номер игрока (1 или 2)

# Ф-я проверки выигрыша принимает номер игрока, список всех ходов, список с номерами ячеек игрока
# Из него с помощью ф-ий делает два списка с номерами строк и столбцов.
# Если в них есть: {column} кол-во одинаковых строк или {row} кол-во одинаковых столбцов
# (т.е. строка или столбец целиком заполнены одним игроком)
# или есть диагональ (только для квадратов row = column) - победа.
# Возвращает 1 или 2 если победил один из игроков, -1 если ничья (ходов больше нет), 0 если игра продолжается,
# переписать бы нормально через continue и break когда с ними разберусь

from collections import Counter


def check_victory(player: int, actions_: dict, current_list: list) -> int:
    list_row = [row_number(i) for i in current_list]
    list_column = [column_number(i) for i in current_list]
    # проверка, есть ли целиком заполненный столбец или строка
    if max(Counter(list_row).values()) == COLUMN or max(Counter(list_column).values()) == ROW:
        return player
    if check_diag(current_list):  # проверка диагонали
        return player
    elif len(actions_) == ROW * COLUMN:  # ходы кончились
        return -1
    else:
        return 0

# Функция получает список ячеек игрока, проверяет, что заполнена диагональ.
# У диагонали1 номера строк и столбцов равны, у диагонали2 сумма строк и столбцов равна 1 + ROW
# Возвращает тип bool

def check_diag (current_list: list) -> bool:
    if ROW == COLUMN:
        diag_1 = [i for i in current_list if row_number(i) == column_number(i)]
        diag_2 = [i for i in current_list if row_number(i) + column_number(i) == ROW + 1]
        a = len(diag_1) == ROW or len(diag_2) == ROW
        return a




#  Функции раскладывают номер ячейки (от 1 до row*column) на координаты: номер строки, номер столбца
import math
from math import ceil

def row_number (a: int):
    x = math.ceil(a / COLUMN)
    return x

def column_number(a: int):
    # если a%b = 0, возвращает y = b
    y = a % ROW if a % ROW != 0 else ROW  # не нравится конструкция
    return y


# Ф-я инициирует ход игрока. Вычисляет, чей ход, в завис-ти от номера хода; запрашивает у игрока ввод cell_number (номер ячейки);
# добавляет номер ячейки как ключ в словарь actions_for_picture и в словарь actions в список по ключу игрока
# затем вызывает ф-ю отрисовки поля (не реализовано)
# затем вызывает ф-ю проверки выигрыша и в завис-ти от ее значения цикл продолжается или печатается сообщение о рез-те игры

# def action(cell_number: int):

for action_number in range(1, ROW * COLUMN + 1):  # номер хода
    if action_number % 2 == 1:
            player = 1
    else:
        player = 2
    while True:
        cell_number = input(f'Ход {action_number}. Игрок {player} вводит номер ячейки')
        cell_number = int(cell_number) # ?? надо будет обработать ошибку
        if cell_number not in range(1, ROW * COLUMN + 1):
            print(f'Ячейки с номером {cell_number} нет. Введите целое число от 1 до {ROW * COLUMN + 1}')
        elif cell_number in actions_for_picture:
            print(f'Ячейка с номером {cell_number} уже занята. Введите другое целое число от 1 до {ROW * COLUMN + 1}')
        else:
            current_list = actions.get(player,[])
            current_list.append(cell_number)
            actions[player] = current_list
            actions_for_picture[cell_number] = player
            break
    result = check_victory(player, actions_for_picture, current_list)
    if result == player:
        print(f'Игра окончена. Игрок {player} выиграл!!!')
        break
    if result == -1:
        print('Игра окончена. Никто не выиграл :-(.')
        break









