print('---------')
print('|       |')
print('|       |')
print('|       |')
print('---------')

s = ' ' * 9
flag = True
currentPlayer = 'X'

while flag:
    occupied_cells = []
    for n in range(9):
        if s[n] != ' ':
            occupied_cells.append(n)
    coords_str = input('Enter the coordinates:')
    coords = coords_str.split()
    if len(coords) != 2:
        print('You should enter numbers!')
    elif not coords[0].isdigit() or not coords[1].isdigit():
        print('You should enter numbers!')
    elif not (3 >= int(coords[0]) >= 1 and 3 >= int(coords[1]) >= 1):
        print('Coordinates should be from 1 to 3!')
    else:
        index = 0
        if int(coords[0]) == 1:
            index = int(coords[1]) - 1
        elif int(coords[0]) == 2:
            index = int(coords[1]) + 2
        else:
            index = int(coords[1]) + 5
        if index in occupied_cells:
            print('This cell is occupied! Choose another one!')
        else:
            s_list = list(s)
            s_list[index] = currentPlayer
            s = ''.join(s_list)
            print('---------')
            print(f'| {s[0]} {s[1]} {s[2]} |')
            print(f'| {s[3]} {s[4]} {s[5]} |')
            print(f'| {s[6]} {s[7]} {s[8]} |')
            print('---------')
            currentPlayer = 'O' if currentPlayer == 'X' else 'X'

            lines = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
                     [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
            number_of_x_winning_lines = 0
            number_of_o_winning_lines = 0
            number_of_x = 0
            number_of_o = 0
            number_of_empty_cells = 0

            for line in lines:
                if s[line[0]] == s[line[1]] == s[line[2]]:
                    if s[line[0]] == 'X':
                        number_of_x_winning_lines += 1
                    elif s[line[0]] == 'O':
                        number_of_o_winning_lines += 1

            for n in range(9):
                if s[n] == 'X':
                    number_of_x += 1
                elif s[n] == 'O':
                    number_of_o += 1
                else:
                    number_of_empty_cells += 1

            if number_of_o_winning_lines + number_of_x_winning_lines > 1:
                print('Impossible')
                print(number_of_x_winning_lines, number_of_o_winning_lines, s)
            elif abs(number_of_x - number_of_o) > 1:
                print('Impossible')
            elif number_of_o_winning_lines == 1:
                print('O wins')
                flag = False
            elif number_of_x_winning_lines == 1:
                print('X wins')
                flag = False
            elif number_of_empty_cells == 0:
                print('Draw')
                flag = False
