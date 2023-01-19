from collections import deque

player_one_symbol = '1'
player_two_symbol = '2'
directions = (
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
    (1, 1),
    (-1, -1),
    (1, -1),
    (-1, 1)
)
rows, cols = 6, 7
field = [['0'] * cols for _ in range(rows)]
turn = deque([[1, player_one_symbol], [2, player_two_symbol]])

while True:
    [print(f'[ {" ".join(row)} ]') for row in field]

    player_number, player_symbol = turn[0]

    try:
        player_col = int(input(f'Player {player_number}, please choose a column: '))-1
    except ValueError:
        print('Please choose a valid number')
        continue

    if not 0 <= player_col < cols:
        print(f'Select a valid number in range (1-{cols})')
        continue

    row = 0

    if field[row][player_col] != '0':
        print(f'This column has no available spots!')
        continue

    while True:
        if row == rows - 1 or field[row+1][player_col] != '0':
            field[row][player_col] = player_symbol
            break
        row += 1

    for row in range(rows):
        for col in range(cols):
            if field[row][col] != player_symbol:
                continue

            for direction in directions:
                r, c = row, col

                for _ in range(3):
                    r, c = r + direction[0], c + direction[1]

                    if not (0 <= r < rows and 0 <= c < cols):
                        break

                    if field[r][c] != player_symbol:
                        break

                else:
                    [print(f'[ {" ".join(row)} ]') for row in field]
                    print(f'Player {player_number} is the winner')
                    exit()

    turn.append(turn.popleft())