import random
import turtle

screen = turtle.Screen()
screen.setup(700, 700)
turtle.speed(0)
turtle.hideturtle()

# draw lines for rows
for row in range(10):
    if row % 3 == 0:
        turtle.pensize(3)
    else:
        turtle.pensize(1)

    turtle.penup()
    turtle.goto(-220, 220 - row * 50)
    turtle.pendown()
    turtle.forward(450)

turtle.right(90)

# draw lines for columns
for col in range(10):
    if col % 3 == 0:
        turtle.pensize(3)
    else:
        turtle.pensize(1)

    turtle.penup()
    turtle.goto(-220 + col * 50, 220)
    turtle.pendown()
    turtle.forward(450)

# Write numbers in tabel
turtle.up()
turtle.setpos(235 - 25, -240 + 25)
XPos = turtle.position()[0]
YPos = turtle.position()[1]


def is_valid(board, ro, co, num):
    # Check if 'num' is not in the same row and column
    for i2 in range(9):
        if board[ro][i2] == num or board[i2][co] == num:
            return False

    # Check if 'num' is not in the 3x3 subgrid
    start_row, start_col = 3 * (ro // 3), 3 * (co // 3)
    for i3 in range(3):
        for j3 in range(3):
            if board[start_row + i3][start_col + j3] == num:
                return False

    return True


def solve_sudoku(board):
    for i1 in range(9):
        for j1 in range(9):
            if board[i1][j1] == 0:
                random_numbers = random.sample(range(1, 10), 9)
                for num in random_numbers:
                    if is_valid(board, i1, j1, num):
                        board[i1][j1] = num
                        if solve_sudoku(board):
                            return True
                        board[i1][j1] = 0
                return False
    return True


# Create an empty 9x9 Sudoku board
sudoku_board = [[0 for _ in range(9)] for _ in range(9)]

# Solve the Sudoku with random numbers
solve_sudoku(sudoku_board)

# Print the solved Sudoku
for j in range(9):
 for i in range(9):
     turtle.setpos(XPos - (i * 50), YPos + (j * 50))
     turtle.write(sudoku_board[i][j], move=False, align='right', font=('Arial', 15, 'normal'))

screen.exitonclick()