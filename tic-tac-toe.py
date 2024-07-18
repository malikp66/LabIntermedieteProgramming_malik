import tkinter as tk
from tkinter import simpledialog

# Step 1: Set Up the Tic-Tac-Toe Game Board With Tkinter
root = tk.Tk()
root.title("Tic Tac Toe")

# Get board size from user
while True:
    try:
        board_size = int(simpledialog.askstring("Ukuran Papan", "Masukkan ukuran papan (contoh: 3 untuk 3x3, 4 untuk 4x4, dll.):"))
        if board_size < 3:
            raise ValueError("Ukuran papan minimal 3x3.")
        break
    except ValueError as e:
        tk.messagebox.showerror("Error", str(e))

# Create an empty board
board = [' '] * (board_size ** 2)

# Fungsi untuk membuat papan permainan
def create_board():
    for i in range(board_size ** 2):
        button = tk.Button(root, text=board[i], font=('Arial', 20),
                           width=3, height=1, command=lambda row=i//board_size, col=i%board_size: handle_move(row, col))
        button.grid(row=i//board_size, column=i%board_size)

# Step 2: Set Up the Tic-Tac-Toe Game Logic in Python

player = 'X'

def check_winner():
    # Memeriksa baris, kolom, dan diagonal
    winning_combinations = []

    # Baris dan kolom
    for i in range(board_size):
        winning_combinations.append(tuple(range(i*board_size, (i+1)*board_size)))
        winning_combinations.append(tuple(range(i, board_size**2, board_size)))

    # Diagonal utama
    winning_combinations.append(tuple(range(0, board_size**2, board_size+1)))

    # Diagonal sekunder
    winning_combinations.append(tuple(range(board_size-1, board_size**2-1, board_size-1)))

    for combo in winning_combinations:
        if all(board[combo[i]] == board[combo[0]] != ' ' for i in range(1, board_size)):
            return board[combo[0]]

    # Memeriksa jika permainan seri
    if ' ' not in board:
        return 'Seri'

    return None

# Step 3: Process the Players' Moves on the Game's Logic

def handle_move(row, col):
    global player

    if board[row * board_size + col] == ' ':
        board[row * board_size + col] = player
        create_board()
        winner = check_winner()

        if winner:
            if winner == 'Seri':
                result_label.config(text="Permainan Seri!")
            else:
                result_label.config(text=f"Pemenangnya adalah {winner}!")

        player = 'O' if player == 'X' else 'X'

# Step 4: Process Players' Moves on the Game Board

create_board()

# Step 5: Provide Options to Play Again and Exit the Game

result_label = tk.Label(root, text="")
result_label.grid(row=board_size, column=0, columnspan=board_size)

root.mainloop()
