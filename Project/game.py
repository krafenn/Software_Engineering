import tkinter as tk
from tkinter import simpledialog, messagebox

root = tk.Tk()
root.title("Крестики-нолики")

current_player = "X"
moves = 0
game_over = False
buttons = []


def create_game_board():
    global buttons, current_player, moves, game_over

    board_size = simpledialog.askinteger("Размер поля", "Введите размер поля (например, 3 для поля 3x3):", parent=root)
    win_length = simpledialog.askinteger("Выигрышные клетки", "Введите количество выигрышных клеток:", parent=root)

    buttons = [
        tk.Button(root, text="", font=("Arial", 20), width=4, height=2,
                  command=lambda pos=i: on_click(buttons[pos], pos))
        for i in range(board_size ** 2)
    ]

    for i in range(board_size):
        for j in range(board_size):
            buttons[i * board_size + j].grid(row=i, column=j)

    current_player = "X"
    moves = 0
    game_over = False

    def check_winner():
        global game_over
        # Получаем размер поля для проверки выигрышных комбинаций
        board_size = int(len(buttons) ** 0.5)

        win_combinations = []
        # Горизонтальные комбинации
        for i in range(board_size):
            for j in range(board_size - win_length + 1):
                win_combinations.append([i * board_size + j + k for k in range(win_length)])

        # Вертикальные комбинации
        for i in range(board_size - win_length + 1):
            for j in range(board_size):
                win_combinations.append([i * board_size + j + k * board_size for k in range(win_length)])

        # Диагонали слева направо
        for i in range(board_size - win_length + 1):
            for j in range(board_size - win_length + 1):
                win_combinations.append([i * board_size + j + k * (board_size + 1) for k in range(win_length)])

        # Диагонали справа налево
        for i in range(board_size - win_length + 1):
            for j in range(win_length - 1, board_size):
                win_combinations.append([i * board_size + j - k * (board_size - 1) for k in range(win_length)])

        for combination in win_combinations:
            if all([buttons[pos]["text"] == current_player for pos in combination]):
                game_over = True
                messagebox.showinfo("Победа!", f"Игрок {current_player} выиграл!")
                root.quit()
                break

        if moves == board_size ** 2 and not game_over:
            messagebox.showinfo("Ничья!", "Игра окончена ничьей!")
            root.quit()

    def on_click(button, position):
        global current_player, moves
        if button["text"] == "" and not game_over:
            button["text"] = current_player
            moves += 1
            check_winner()
            current_player = "O" if current_player == "X" else "X"

    check_winner()


create_game_board()

root.mainloop()
