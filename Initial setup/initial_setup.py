# write your code here
from typing import *


def create_matrix(state):
    matrix = [[], [], []]
    # print(matrix)
    m = 0

    for k, i in enumerate(state):
        if k % 3 == 0 and k != 0:
            m += 1

        if i != '_':
            matrix[m].append(i)
        else:
            matrix[m].append(' ')

    return matrix


def print_matrix(matrix):
    print('---------')
    for i in matrix:
        print('|', end=' ')
        for j in i:
            print(j, end=' ')
        print('|')
    print('---------')


def user_move(matrix: List[List], value):
    while True:
        move = input("Enter the coordinates: ")

        if not move.replace(' ', '').isdigit():
            print("You should enter numbers!")
            print(move.replace(' ', ''))
            continue

        x, y = move.split()
        x = int(x) - 1
        y = int(y) - 1

        if x > 2 or y > 2:
            print("Coordinates should be from 1 to 3!")
            continue

        if matrix[x][y] != ' ':
            print("This cell is occupied! Choose another one!")
            continue

        matrix[x][y] = value

        break


def end_of_game(matrix: List[List]):
    # Check row by row
    for k, i in enumerate(matrix):
        first_index = i[0]
        if i.count(first_index) == 3:
            print(f"{first_index} wins")

    # Check column by column
    for c in range(3):
        first_index = c
        for r in range(3):
            if matrix[r][c] != first_index:
                pass


def game():
    initial_state = input("Enter the cells: ")

    table = create_matrix(initial_state)
    print_matrix(table)

    if initial_state.count('X') <= initial_state.count('O'):
        user_move(table, 'X')
    else:
        user_move(table, 'O')

    print_matrix(table)

    end_of_game(table)


game()
