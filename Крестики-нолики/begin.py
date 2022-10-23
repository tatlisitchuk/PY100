# Запрос параметров для игры
# Мы еще не проходили обработку ошибок, поэтому пока коряво написано

while True:

    opponent = input('Введите соперника 1 - компьютер, 2 - человек: ')
    while opponent not in ('1', '2'):
        opponent = input('Такого игрока нет! Введите соперника 1 - компьютер, 2 - человек: ')

    if opponent == '1':  #комп
        print('Игра с компьютером реализована на поле 3*3')
    else:  # человек
        while True:
            row = input('Введите кол-во строк (целое положит.число): ')
            try:
                if isinstance(int(row), int) and int(row) > 0:   # не очень
                    break
            except Exception:  # нельзя так писать ((
                ('Кол-во строк должно быть целым положит.числом!')  #  не выполняется

        while True:
            column = input('Введите кол-во столбцов (целое положит.число): ')
            try:
                if isinstance(int(column), int) and int(column) > 0:
                    break
            except Exception:
                ('Кол-во столбцов должно быть целым положит.числом!')

    if opponent == '1':  #комп
        while True:
            first_player = input('Введите, кто ходит первым (1 - компьютер, 2 - человек: ')
            if first_player in ('1', '2'):
                break

    # print (f'Игра с {[компьютером] if opponent == '1' else [человеком] на поле ...)}   можно ли if в print? уточнить, дописать

    while True:
        begin = input('Нажмите 1, чтобы начать игру, или 0, чтобы ввести параметры заново: ')
        if begin in ('1', '0'):
            break

    if begin == '1':
        print('Добро пожаловать!')
        break

ROW = int(row)
COLUMN = int(column)

# if opponent == '2':
#     import two_people
# elif first_player == '1':
#     import comp1_man2
# else:
#     import man1_2comp2
