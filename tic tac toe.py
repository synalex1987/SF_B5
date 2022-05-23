# Игра "Крестики-Нолики"

# Рисование игрового поля в консоли
def draw_field(field):
    print('  0 1 2')
    for i in range(len(field)):
        print(str(i), *field[i])


# Функция проверяет ввод от игрока и возвращает корректные координаты x, y
def check_move(field, player):
    while True:
        try:
            coords = input(f'Ходит игрок [{player}]. Введите координаты(x, y): ').split()
            x, y = map(int, coords)
        except:
            print('Упс, ошибка. Проверьте введенные значения. 2 координаты, которые являются числами от 0 до 2')
            continue

        if (x < 0 or x > 2) or (y < 0 or y > 2):
            print('Упс, ошибка. Введите значение от 0 до 2. Попробуйте ещё раз.')
            continue
        if field[x][y] != '-':
            print('Упс, ошибка. Данная клетка занята другим игроком.Попробуйте ещё раз.')
            continue

        return x, y


# Проверка условия победы одного из игроков. Вернет булево значение
def is_win(field, player):
    field_in_row = []
    for row in field:
        field_in_row += row
    win_positions = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                     [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    player_indexes = set([i for i, x in enumerate(field_in_row) if x == player])
    for win_pos in win_positions:
        if len(player_indexes & set(win_pos)) == 3:
            return True
    return False


# Функция запуска игры.
def game(field):
    count, player = 0, ''
    while True:
        draw_field(field)
        player = 'X' if not count % 2 else 'O'
        if count == 9:
            print('Ничья. Победила дружба!')
            break
        x, y = check_move(field, player)
        field[x][y] = player
        if is_win(field, player):
            draw_field(field)
            print(f'Игрок [{player}] победил! Поздравляем!')
            break
        count += 1


f3_3 = [['-'] * 3 for _ in range(3)]
game(f3_3)
input('Нажмите любую клавишу для выхода...')
