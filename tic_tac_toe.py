def check_for_win():
    first_diagonal = all([field[i][i] == players[0][1] for i in range(len(field))])
    second_diagonal = all([field[i][len(field)-1 - i] == players[0][1]for i in range(len(field))])
    row_win = any([all(True if pos == players[0][1] else False for pos in row)for row in field])
    col_win = any([all(True if field[row][col] == players[0][1] else False for row in range(len(field))) for col in range(len(field))])

    if any([first_diagonal, second_diagonal, row_win, col_win]):
        print(f'{players[0][0]} won!')
        raise SystemExit

    players.append(players.pop(0))


def place_position(position):

    row = (position - 1) // 3
    col = (position - 1) % 3

    if field[row][col] in ['X', 'O']:
        print('This position is taken.')
        choose_position()
    else:
        field[row][col] = players[0][1]

    print_field()
    check_for_win()
    choose_position()


def choose_position():
    while True:
        try:
            player_position = int(input(f'{players[0][0]} choose a free position [1-9]: '))
        except ValueError:
            print(f"{players[0][0]}, please select a valid position!")
            continue

        if 1 <= player_position < len(field) * len(field):
            break
        else:
            print(f"{players[0][0]}, please select a valid position!")

    place_position(player_position)


def print_field(begin=False):
    if begin:
        print('This is the numeration of the board:')
        [print(f'| {" | ".join(row)} |') for row in field]
        print(f'{players[0][0]} starts first!')

        for row in range(len(field)):
            for col in range(len(field)):
                field[row][col] = ' '

    else:
        [print(f'| {" | ".join(row)} |') for row in field]


def start():
    player_one = input('Player one name: ')
    player_two = input('Player two name: ')

    while True:
        player_one_symbol = input(f'{player_one} would you like to play with "X" or "O"? ').upper()

        if player_one_symbol not in ['X', 'O']:
            print('Please enter the correct symbol')
            continue

        else:
            break

    player_two_symbol = 'O' if player_one_symbol == 'X' else 'X'
    players.append([player_one, player_one_symbol])
    players.append([player_two, player_two_symbol])
    print_field(begin=True)
    choose_position()


players = []
field = [[str(i), str(i+1), str(i+2)] for i in range(1, 10, 3)]
start()

