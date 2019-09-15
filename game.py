def sepl(quant=30, symbol='-'):
    """
    Separator of line, print a symbol to separate lines
    :param quant: quantity of times to multiply the symbol
    :param symbol: symbol to be shown
    :return: print a symbol times quantity/a separator of line
    """
    return print(symbol * quant)


def title(msg, symbol='-'):
    """
    Do a title separated by a symbol
    :param symbol: Symbol to be the separator of the title
    :param msg: Message/Text to be shown
    :return: return 3 print, one separator, one title, and another separator
    """
    return print(f'{symbol}' * 30), print(f'{msg:^30}'), print(f'{symbol}' * 30)


def clear():
    """
    Clean the screen of the terminal
    :return:
    """
    os.system('clear') or None


def run():
    """
    Function that runs all the program
    :return:
    """

    # Title of the tic-tac-toe
    title(msg='JOGO DA VELHA')

    # The structure of tic-tac-toe initial
    structure_initial = [[' '], [' '], [' '],
                         [' '], [' '], [' '],
                         [' '], [' '], [' ']]
    # The structure with position
    structure_position = [['1'], ['2'], ['3'],
                          ['4'], ['5'], ['6'],
                          ['7'], ['8'], ['9']]

    # The structure that will be change while the program is running
    structure = structure_initial.copy()

    # Where player1 and player2 will pass
    player1_pos = ''
    player2_pos = ''

    # Choosing X or O
    not_std_symbols = True
    while not_std_symbols:
        player1 = str(input('player1 [x ou o]? ')).lower()
        player2 = str(input('player2 [x ou o]? ')).lower()
        if player1 != 'x' and player1 != 'o' or player2 != 'x' and player2 != 'o':
            print('Please choose "x" or "o" (standard values).')
        break

    # Tic-tac-toe with position for the user can understand
    sepl()
    for i, element in enumerate(structure_position):
        if i == 2 or i == 5:
            print(f'[{element[0]}]')
        else:
            print(f'[{element[0]}]', end=' ')
    print()
    sepl()

    # Even now no one wins
    without_victory = True

    # Var Temp
    list_temp1 = []
    list_temp2 = []

    c = 2
    while True:
        # Verify when the program need to stop
        if c == 11:
            break

        # Verify the turn (player1, player2)
        if c % 2 == 0:
            player_turn_name = 'player1'
            player_turn_value = player1
        else:
            player_turn_name = 'player2'
            player_turn_value = player2

        # Input position to put the signal on the tic-tac-toe
        while True:
            try:
                pos = int(input(f'[{player_turn_name}] Posição: ')) - 1
                if pos + 1 > 9 or pos + 1 <= 0:
                    print('POSIÇÕES DEVEM SER ENTRE 1 E 9!')
                else:
                    break
            except ValueError:
                print('DIGITE UMA DAS POSIÇÕES!')

        if str(pos + 1) not in player1_pos and str(pos + 1) not in player2_pos:
            different_pos = True
            structure.pop(pos)
            structure.insert(pos, [player_turn_value])
        else:
            print('Está posição está OCUPADA!')
            continue

        # Save where the player1 or player2 passed
        if different_pos and player_turn_name == 'player1':
            list_temp1.append(str(pos + 1))
            list_temp1.sort()
            for element in list_temp1:
                player1_pos += element

        elif different_pos:
            list_temp2.append(str(pos + 1))
            list_temp2.sort()
            for element in list_temp2:
                player2_pos += element

        # Show the tic-tac-toe
        sepl()
        for i, element in enumerate(structure):
            if i == 2 or i == 5:
                print(f'[{element[0]}]')
            else:
                print(f'[{element[0]}]', end=' ')
        print()
        sepl()

        # Verify who win
        if '1' in player1_pos and '2' in player1_pos and '3' in player1_pos \
                or '4' in player1_pos and '5' in player1_pos and '6' in player1_pos \
                or '7' in player1_pos and '8' in player1_pos and '9' in player1_pos \
                or '1' in player1_pos and '4' in player1_pos and '7' in player1_pos \
                or '2' in player1_pos and '5' in player1_pos and '8' in player1_pos \
                or '3' in player1_pos and '6' in player1_pos and '9' in player1_pos \
                or '1' in player1_pos and '5' in player1_pos and '9' in player1_pos \
                or '3' in player1_pos and '5' in player1_pos and '7' in player1_pos:
            print(f'[player1] O "{player1}" GANHOU!')
            without_victory = False
            break

        elif '1' in player2_pos and '2' in player2_pos and '3' in player2_pos \
                or '4' in player2_pos and '5' in player2_pos and '6' in player2_pos \
                or '7' in player2_pos and '8' in player2_pos and '9' in player2_pos \
                or '1' in player2_pos and '4' in player2_pos and '7' in player2_pos \
                or '2' in player2_pos and '5' in player2_pos and '8' in player2_pos \
                or '3' in player2_pos and '6' in player2_pos and '9' in player2_pos \
                or '1' in player2_pos and '5' in player2_pos and '9' in player2_pos \
                or '3' in player2_pos and '5' in player2_pos and '7' in player2_pos:
            print(f'[player2] O "{player2}" GANHOU!')
            without_victory = False
            break

        c += 1

    # Verify if no one wins
    if without_victory:
        print('DEU VELHA!')

