"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Petr Svetr
email: petr.svetr@gmail.com
discord: Petr Svetr#4490
"""

def print_welcome():
    print("Vítejte ve hře Piškvorky (Tic-Tac-Toe)")
    print("=" * 40)
    print("PRAVIDLA HRY:")
    print("Hraje se na mřížce 3×3")
    print("Hráči střídavě vkládají 'X' a 'O'")
    print("První hráč, který poskládá 3 své symboly")
    print("v řadě, sloupci nebo diagonále – vyhrává!")
    print("Čísla políček:")
    print_board(["1","2","3","4","5","6","7","8","9"])
    print("=" * 40)


def print_board(board):
    print("+" + "-"*3 + "+" + "-"*3 + "+" + "-"*3 + "+")
    for i in range(3):
        row = board[i*3:(i+1)*3]
        print("| " + " | ".join(row) + " |")
        print("+" + "-"*3 + "+" + "-"*3 + "+" + "-"*3 + "+")

def is_valid_input(player_input, board):
    if not player_input.isdigit():
        return False, "Zadej prosím číslo!"
    
    num = int(player_input)
    if num < 1 or num > 9:
        return False, "Číslo musí být v rozmezí 1–9!"
    
    if board[num-1] in ["X", "O"]:
        return False, "Toto pole je již obsazené!"
    
    return True, ""


def check_winner(board, player):
    # Řádky
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == player:
            return True
    
    # Sloupce
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player:
            return True
    
    # Diagonály
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    
    return False


def is_board_full(board):
    return all(field in ["X", "O"] for field in board)


def play_game():
    board = [str(i) for i in range(1, 10)]  # 1 až 9 jako stringy
    current_player = "X"
    
    print_welcome()
    
    while True:
        print_board(board)
        print(f"Hraje hráč {current_player}")
        
        move = input("Zadejte číslo pole (1-9): ").strip()

valid, message = is_valid_input(move, board)
        if not valid:
            print(message)
            print("-" * 40)
            continue
        
        # Zápis tahu
        position = int(move) - 1
        board[position] = current_player
        
        # Kontrola výhry
        if check_winner(board, current_player):
            print_board(board)
            print("=" * 40)
            print(f"GRATULACE! Hráč {current_player} VYHRÁL!")
            print("=" * 40)
            break
        
        # Kontrola remízy
        if is_board_full(board):
            print_board(board)
            print("=" * 40)
            print("REMÍZA! Hrací pole je plné.")
            print("=" * 40)
            break
        
        # Změna hráče
        current_player = "O" if current_player == "X" else "X"
        print("-" * 40)


if __name__ == "__main__":
    play_game()