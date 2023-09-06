def display_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# تابعی برای بررسی برد بازی
def check_win(board):
    # بررسی ردیف‌ها
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return True

    # بررسی ستون‌ها
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # بررسی قطرها
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    elif board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

# تابع اجرای بازی
def play_game():
    print("بازی دوز شروع می شود!")
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]

    player = "X"
    game_over = False

    while not game_over:
        display_board(board)
        print(f"نوبت بازیکن {player}")
        row = int(input("لطفاً شماره ردیف را وارد کنید (0-2): "))
        col = int(input("لطفاً شماره ستون را وارد کنید (0-2): "))

        if board[row][col] == " ":
            board[row][col] = player
        else:
            print("مکان انتخاب شده قبلاً پر شده است. لطفاً مکان دیگری انتخاب کنید.")
            continue

        if check_win(board):
            display_board(board)
            print(f"بازیکن {player} برنده شد!")
            game_over = True
        elif all([cell != " " for row in board for cell in row]):
            display_board(board)
            print("تساوی!")
            game_over = True
        else:
            player = "O" if player == "X" else "X"

# اجرای بازی
play_game()