#!/usr/bin/python3
import os
import platform

if platform.system() == "Windows":
    CLEAR_SCREEN_COMMAND = "cls"
else:
    CLEAR_SCREEN_COMMAND = "clear"


def show_title(msg: str, size=30) -> None:
    """
    Show a msg as title.
    """
    print("=" * size)
    print(f"{msg:^{size}}")
    print("=" * size)


def sep_line(size=30) -> None:
    """
    Seperate a line by a dam.
    """
    print("-" * size)


def clear_screen() -> None:
    """
    Clear the screen, depending on the OS.
    """
    os.system(CLEAR_SCREEN_COMMAND)


def show_error(err_msg: str) -> None:
    """
    Show a error msg.
    """
    print(f"[Error] {err_msg}")


def show_grid(grid: []) -> None:
    """
    Show the current state of the grid (game).
    """
    GRID_SIZE = len(grid)
    GRID_INTERVAL = GRID_SIZE ** 0.5

    for i in range(GRID_SIZE):
        if i == GRID_INTERVAL or i == GRID_INTERVAL * 2:  # Break line
            print(flush=True)
        
        print(f"[{grid[i].upper()}]", end="")
    print()


def input_pos(turn: int, grid: [], symbols: []) -> int:
    """
    Return the input of a pos.
    """
    valid_pos = False

    while not valid_pos:
        try:
            player_number = turn // 2 + 1
            pos = int(input(f"Player {player_number} ({symbols[player_number - 1].upper()}): "))

            # Verify if is a valid pos for the grid
            if pos > 0 and pos < 10:
                # Verify if the position is already used
                if grid[pos - 1] not in "xo":
                    valid_pos = True
                else:
                    show_error("Position already used!")
            else:
                show_error("Please type a position between 0 and 9!")
        except ValueError:
            show_error("Please type a valid position!")
    
    return pos


def get_winner(grid: [], symbols: []) -> int:
    """
    Verifies if any player won.
    Return: 1 if player 1 won, 2 if player 2 won, 0 if nobody won yet.
    """
    player1_pos = ""
    player2_pos = ""

    for i in range(len(grid)):
        if grid[i] == symbols[0]:
            player1_pos += str(i + 1)
        elif grid[i] == symbols[1]:
            player2_pos += str(i + 1)
    
    # Verify if any player won
    if ("123" in player1_pos) or ("456" in player1_pos) or ("789" in player1_pos) or \
        ("1" in player1_pos and "5" in player1_pos and "9" in player1_pos) or \
        ("3" in player1_pos and "5" in player1_pos and "7" in player1_pos):
        return 1  # Player 1 won
    if ("123" in player2_pos) or ("456" in player2_pos) or ("789" in player2_pos) or \
        ("1" in player2_pos and "5" in player2_pos and "9" in player2_pos) or \
        ("3" in player2_pos and "5" in player2_pos and "7" in player2_pos):
        return 2  # Player 1 won
    
    return 0  # Nobory won yet


def confirm(question: str, yes="y", no="n") -> bool:
    """
    Returns if the user answered the question with 'yes'.
    """
    try:
        yes = yes[0]
        no = no[0]
    except IndexError:
        yes = "y"
        no = "n"

    valid_answer = False
    while not valid_answer:
        try:
            answer = str(input(question)).strip().lower()[0]

            if answer not in (yes + no):
                show_error(f"Please type {yes} or {no}!")
                continue
            
            if answer == yes:
                return True
            
            break
        except IndexError:
            show_error("Please type a valid answer!")
    
    return False


def run() -> None:
    """
    Run the game.
    """
    try:
        clear_screen()
        show_title("Tic Tac Toe")

        grid = []

        # Start the grid values
        for i in range(9):
            grid.append(str(i + 1))

        # Choose symbol to play
        valid_symbols = False
        while not valid_symbols:
            try:
                symbol1 = str(input("Player 1 [X / O]: ")).strip().lower()[0]
                symbol2 = str(input("Player 2 [X / O]: ")).strip().lower()[0]

                if not (symbol1 in "xo" and symbol2 in "xo"):
                    show_error("Please type 'X' or 'O!")
                elif symbol1 == symbol2:
                    show_error("Symbols cannot be equal!")
                else:
                    valid_symbols = True
            except IndexError:
                show_error("Please type valid symbols!")
        
        # 1 for player 1 and 2 for player 2, can't be 0
        turn = 1
        times = 0

        # Show the game (grid) state
        while True:
            # Show the title
            clear_screen()
            show_title("Tic Tac Toe")

            # Show the grid
            sep_line()
            show_grid(grid)
            sep_line()

            # Verify if anyone won
            winner = get_winner(grid, [symbol1, symbol2])
            if winner == 1:
                print(f"Player 1 ({symbol1.upper()}) won!")
                sep_line()
                
                if confirm("Play again? [y/n]: "):
                    run()
                else:
                    quit()
            elif winner == 2:
                print(f"Player 2 ({symbol2.upper()}) won!")
                sep_line()

                if confirm("Play again? [y/n]: "):
                    run()
                else:
                    quit()
            elif times == len(grid):
                print("Nobody won!")
                sep_line()

                if confirm("Play again? [y/n]: "):
                    run()
                else:
                    quit()

            # Get the pos from the player
            pos = input_pos(turn, grid, [symbol1, symbol2])
            grid.pop(pos - 1)
            
            # Insert new symbol
            if turn == 1:
                grid.insert(pos - 1, symbol1)
                turn += 1
            elif turn == 2:
                grid.insert(pos - 1, symbol2)
                turn -= 1
            else:
                show_error(f"Invalid 'turn' value: {turn}!")
            
            times += 1
    except (KeyboardInterrupt, EOFError):
        print()
        sep_line()
        print("Game finished!")


if __name__ == "__main__":
    run()
