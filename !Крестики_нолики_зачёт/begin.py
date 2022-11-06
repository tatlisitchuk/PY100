from typing import Optional

EMPTY_CEIL = None
STANDART_FIELD = [3, 3]
PLAYERS_SYMBOLS = {1: "X", 2: "O"}
NON_HUMAN_OPPONENT = 'Компьютер'


def get_name_opponent() -> dict:
    """
    Запрашивает ввод имен соперников; если имя не введено, то игрок - компьютер
    :return: словарь, номер игрока - имя игрока
    """
    players_names = {}
    for number_ in PLAYERS_SYMBOLS:
        print('Пожалуйста, представьтесь')
        player = input(f'Введите имя игрока, который ходит {number_}й ({PLAYERS_SYMBOLS[number_]}). '
                       f'Если {number_}й игрок - {NON_HUMAN_OPPONENT}, '
                       f'введите \'{NON_HUMAN_OPPONENT}\' или намжите Enter\n')
        if not player:
            player = NON_HUMAN_OPPONENT
        players_names[number_] = player
    return players_names


def get_size(name_opponent: dict, objects: list[str]) -> list[int]:
    """
    Запрашивает у пользователя стороны поля, пока тот не введет целое положит.число. Если среди игроков комп - станд.поле
    :return: целое число, размерность поля object_
    """
    if NON_HUMAN_OPPONENT in name_opponent.values():
        print(f'Игра с {NON_HUMAN_OPPONENT} реализована на поле {STANDART_FIELD}')
        return STANDART_FIELD
    else:
        field_size = []
        for object_ in objects:
            while True:
                try:
                    qty = int(input(f'Введите {object_} (целое положит.число):\n'))
                    if not qty > 0:
                        raise ValueError(f'{object_} должно быть целым положит.числом!')
                except ValueError:
                    print(f'{object_} должно быть целым положит.числом!')
                    continue  #ни на что не влияет, цикл и так пойдет заново?
                else:
                    field_size.append(qty)
                    break
        return field_size


def prove_game(name_opponent: dict, row_qty: int, column_qty: int) -> Optional[bool]:
    """
    Запрашивает подтверждение начала игры; выводит приветствие игроков
    :param name_opponent: имена игроков для печати
    :param row_qty: кол-во строк для печати
    :param column_qty: кол-во столбцов для печати
    :return: True если подтверждение начала игры (введено 1) или None
    """
    while True:
        begin = input('Нажмите 1, чтобы начать игру, или 0, чтобы ввести параметры заново:\n')
        if begin in ('1', '0'):
            break
    if begin == '1':
        print(
            f"Добро пожаловать, {', '.join(list(name_opponent.values()))}! Игра на поле {row_qty} на {column_qty}.\n"
            f"Начинаем игру.")
        return True


def create_field(row_qty: int, column_qty: int) -> list[list]:
    """
    Создает список списков
    :param row_qty: кол-во строк (кол-во списков в списке)
    :param column_qty: кол-во столбцов (кол-во элементов в каждом вложенном списке)
    :return: список с row_qty списками , в каждом column_qty элементов
    """
    return [[EMPTY_CEIL]*column_qty for _ in range(row_qty)]


def get_picture(field: list[list]) -> None:
    """
    Отрисовывает список списков в 2хмерную картинку с заполнением ячеек символами PLAYERS_SYMBOLS
    :param field: получает список списков
    :return: возвращает None, отрисовка поля функцией print
    """
    print("Игровое поле")
    for row in field:
        for index, symbol_number in enumerate(row):
            if symbol_number != EMPTY_CEIL:
                print(f'| {PLAYERS_SYMBOLS[symbol_number]} ', end='')
            else:
                print('|   ', end='')
            if index == len(row) - 1:
                print('|')


def get_player(number_action: int, name_opponent: dict) -> int:
    """
    Меняет игрока в начале каждого хода; печатает информацию чей ход
    :param number_action: номер хода
    :param name_opponent: имена игроков для печати
    :return: номер игрока (1 или 2) в завис-ти от номера хода
    """
    player = 1 if number_action % 2 == 1 else 2
    print(f'Ход {number_action}. Игрок {name_opponent[player]} ({PLAYERS_SYMBOLS[player]}) вводит номер ячейки\n')
    return player


def get_ceil(row_qty: int, column_qty: int) -> tuple[int, int]:
    """
    Запрашивает координаты ячейки, проверяет их существование
    :param row_qty: кол-во строк для диапазона x
    :param column_qty: кол-во столбцов для диапазона y
    :return: кортеж из 2х целых положит.чисел, номер строки и номер столбца, выбранные пользователем
    """
    while True:
        try:
            x = int(input(f'Введите номер строки (целое положит.число не больше {row_qty}):\n'))
            y = int(input(f'Введите номер столбца (целое положит.число не больше {column_qty}):\n'))
        except ValueError:
            print(f'Номера строк и столбцов должны быть целым положит.числом!')
            continue
        if x not in (range(1, row_qty+1)) or y not in (range(1, column_qty+1)):
            print(f'Переданы неверные значения. Номер строки должен быть от 1 до {row_qty}, номер столбца - от 1 до {column_qty}!')
            continue
        else:
            break
    return (x, y)


def check_empty(field: list[list], x: int, y: int) -> bool:
    """
    Проверяет, что ячейка пустая
    :param field: список списков
    :param x: искомый список
    :param y: искомый элемент в списке
    :return: True or False
    """
    if field[x-1][y-1] == EMPTY_CEIL:
        return True
    else:
        print(f'Ячейка {x}, {y} уже занята! Посмотрите на поле, выберите свободную ячейку.')
        return False


def get_comp_ceil(field: list[list]) -> tuple[int, int]:
    ...


def fill_field(field: list[list], current_player: int, x: int, y: int) -> list[list]:
    """
    записывает в список списков номер игрока по введенным им координатам
    :param field: список списков
    :param current_player: номер игрока
    :param x: номер списка
    :param y: номер элемента во внутреннем списке
    :return: список списков, где элемент изменен на номер игрока
    """
    field[x-1][y-1] = current_player
    return field


def transp(field: list[list]) -> list[list]:
    """
    транспонирует список списков
    :param field: список списков
    :return: транспонированный список списков
    """
    return [list(i) for i in zip(*field)]


def check_row_column(field: list[list], current_player: int) -> Optional[bool]:
    """
    Проверяет каждый список, что все элементы списка = current_player
    :param field: список списков
    :param current_player: номер игрока, его значение в field
    :return: True, если хотя бы один список целиком состоит из current_player, или None
    """
    #или лучше не связываться с None и прописать else False?
    #в этом проекте неважно, но вообще?
    for index, row in enumerate(field):
        flag = True
        for ceil in row:
            if ceil != current_player:
                flag = False
                break
        if flag:
            return True


def check_diag(field: list[list], current_player: int) -> Optional[bool]:
    """
    Проверяет заполнены ли диагонали у игрока current_player; выполняется только для квадратных полей
    :param field: список списков
    :param current_player: номер игрока; значение, которое ищем в списках
    :return: None для неквадратных полей, False если хоть один эл-т диагонали не равен current_player, иначе True
    """
    if len(field) == len(field[0]):
        is_diag_1 = True
        for index, row in enumerate(field):
            column = index
            if field[index][column] != current_player:
                is_diag_1 = False
                break
        is_diag_2 = True
        for index, row in enumerate(field):
            column = -index-1
            if field[index][column] != current_player:
                is_diag_2 = False
                break
        return is_diag_1 or is_diag_2


def main():
    while True:
        name_opponent = get_name_opponent()
        row_qty, column_qty = get_size(name_opponent, ["Кол-во строк", "Кол-во столбцов"])
        begin = prove_game(name_opponent, row_qty, column_qty)
        if begin:
            break
    field = create_field(row_qty, column_qty)
    get_picture(field)
    for number_action in range(1, row_qty * column_qty + 1):
        current_player = get_player(number_action, name_opponent)
        if name_opponent[current_player] == NON_HUMAN_OPPONENT:
            x, y = get_comp_ceil(field)
        else:
            while True:
                x, y = get_ceil(row_qty, column_qty)
                if check_empty(field, x, y):
                    break
        field = fill_field(field, current_player, x, y)  # нехорошо так перезаписывать поле??
        field_transp = transp(field)
        get_picture(field)
        result = check_row_column(field, current_player) or check_row_column(field_transp, current_player) \
                 or check_diag(field, current_player)
        if result:
            print(f"Победа!!! Игрок {name_opponent[current_player]} выиграл.")
            break
        if number_action == row_qty * column_qty:
            print('Игра окончена. Никто не выиграл :-(.')
    return ''  # ? норм , чтобы в конце не было None
        

print(b := main())





