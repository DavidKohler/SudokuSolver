#!/usr/bin/env python3
#Sudoku.py
'''
Author: David Kohler
Sudoku Solver
'''

import random

full = set([1, 2, 3, 4, 5, 6, 7, 8, 9])

'''
Set of example grids to test validity
of grid checker
'''
#Good example grid
goodGridEx = [[4,3,5,2,6,9,7,8,1],
        [6,8,2,5,7,1,4,9,3],
        [1,9,7,8,3,4,5,6,2],
        [8,2,6,1,9,5,3,4,7],
        [3,7,4,6,8,2,9,1,5],
        [9,5,1,7,4,3,6,2,8],
        [5,1,9,3,2,6,8,7,4],
        [2,4,8,9,5,7,1,3,6],
        [7,6,3,4,1,8,2,5,9]]

#Bad bc boxes
badGridBoxes = [[4,3,5,2,6,9,7,8,1],
        [6,8,2,5,7,1,4,9,3],
        [1,9,7,8,3,4,5,6,2],
        [8,2,6,1,9,5,3,4,7],
        [3,7,4,6,8,2,9,1,5],
        [5,1,9,3,2,6,8,7,4],
        [9,5,1,7,4,3,6,2,8],
        [2,4,8,9,5,7,1,3,6],
        [7,6,3,4,1,8,2,5,9]]

#Bad bc rows
badGridRows = [[1,1,1,1,1,1,1,1,1],
        [2,2,2,2,2,2,2,2,2],
        [3,3,3,3,3,3,3,3,3],
        [4,4,4,4,4,4,4,4,4],
        [5,5,5,5,5,5,5,5,5],
        [6,6,6,6,6,6,6,6,6],
        [7,7,7,7,7,7,7,7,7],
        [8,8,8,8,8,8,8,8,8],
        [9,9,9,9,9,9,9,9,9]]

#Bad bc columns
badGridCols = [[4,3,5,2,6,9,7,8,1],
        [4,3,5,2,6,9,7,8,1],
        [4,3,5,2,6,9,7,8,1],
        [4,3,5,2,6,9,7,8,1],
        [4,3,5,2,6,9,7,8,1],
        [4,3,5,2,6,9,7,8,1],
        [4,3,5,2,6,9,7,8,1],
        [4,3,5,2,6,9,7,8,1],
        [4,3,5,2,6,9,7,8,1]]

#123456789234567891345678912456789123567891234678912345789123456891234567912345678

def user_select():
    '''
    Asks user to choose what they want to do
    '''
    print("Welcome to my Sudoku program, made by David Kohler")
    print("To solve an existing Sudoku, please enter 1")
    print("To get a new Sudoku puzzle, please enter 2")
    print("To verify a completed Sudoku, please enter 3")
    option = input()
    while((option != "1") and (option != "2") and (option != "3")):
        print("Please enter a valid input")
        option = input()
    return int(option)

def input_grid():
    '''
    Inputs Sudoku grid from user in form of single
    string of numbers
    '''
    rawGrid = input()
    rawList = list(rawGrid)
    grid = [[0 for x in range(9)] for y in range(9)]
    for j in range(0,9):
        grid[j] = [int(rawList[i+(j*9)]) for i in range(0,9)]
    return grid

#TODO SOLVE SUDOKU GRID
def solve_puzzle():
    print("solve")

#TODO CREATE NEW SUDOKU
def new_puzzle():
    print("new")

#TODO VERIFY A COMPLETED SUDOKU
def verify_puzzle():
    print("verify")

#TODO PRINT RULES
def print_rules():
    '''
    Prints rules and instructions of the program
    '''
    print("Rules:")

def next_open(grid, x1, y1):
    '''
    Searches grid for next open spot.
    If no spot found, returns -1,-1 to indicate grid is full
    '''
    #Systematically search next spots
    for i in range(x1, 9):
        for j in range(y1, 9):
            if grid[i][j] == 0:
                return i, j
    #Check from beginning of grid
    for i in range(0, 9):
        for j in range(0, 9):
            if grid[i][j] == 0:
                return i, j
    #No next spot found
    return -1, -1

    '''
def init_grid():
    w, h = 9, 9;
    #grid = [[0 for x in range(w)] for y in range(h)]
    grid = [[random.randint(1,9) for x in range(w)] for y in range(h)]
    return grid
    '''

def print_grid(grid):
    '''
    Prints the grid in a more readible format
    '''
    colcnt, rowcnt = 0, 0
    for i in range(9):
        for j in range(9):
            colcnt+=1
            print(grid[i][j], end=' ')
            if (colcnt == 3) or (colcnt == 6):
                print('|', end=' ')
        rowcnt += 1
        print()
        if (rowcnt == 3) or (rowcnt == 6):
            print('------+-------+-------')
        colcnt = 0
    print()

def grid_success(grid):
    '''
    Checks if grid is complete
    '''
    ##TODO RETURN INTS TO INDICATE WHAT KIND OF FAILURE
    #Checks each row for unique 9 numbers
    for i in range(9):
        if set(grid[i][:]) != full:
            #print("Conflict in rows")
            return False
    #Checks each column for unique 9 numbers
    for j in range(9):
        if set([x[j] for x in grid]) != full:
            #print("Conflict in columns")
            return False
    #Checks each 3x3 box for unique 9 numbers
    if check_boxes(grid) == False:
        #print("Conflict in boxes")
        return False
    return True

def check_boxes(grid):
    '''
    Checks 4 of the grid's boxes. Namely
    boxes 1, 2, 4, and 5. This is the minimum
    amount of boxes to check to verify a complete
    Sudoku grid
    '''
    box1 = [grid[0][0], grid[0][1], grid[0][2],
            grid[1][0], grid[1][1], grid[1][2],
            grid[2][0], grid[2][1], grid[2][2]]

    box2 = [grid[0][3], grid[0][4], grid[0][5],
            grid[1][3], grid[1][4], grid[1][5],
            grid[2][3], grid[2][4], grid[2][5]]

    box4 = [grid[3][0], grid[3][1], grid[3][2],
            grid[4][0], grid[4][1], grid[4][2],
            grid[5][0], grid[5][1], grid[5][2]]

    box5 = [grid[3][3], grid[3][4], grid[3][5],
            grid[4][3], grid[4][4], grid[4][5],
            grid[5][3], grid[5][4], grid[5][5]]

    if (set(box1) == set(box2) == set(box4) == set(box5) == full):
        return True
    return False

if __name__ == '__main__':
    option = user_select()
    if option == 1:
        solve_puzzle()
    elif option == 2:
        new_puzzle()
    elif option == 3:
        verify_puzzle()


    #print_rules()
    #grid = input_grid()
    #print_grid(grid)
    #print(grid_success(grid))







    #print_grid(grid)

    #x = 1
    #cnt = 0
    #while x == 1:
    #    grid = init_grid()
        #print_grid(grid)
    #    cnt += 1
    #    print(cnt)
    #    if grid_success(grid):
    #        print_grid(grid)
    #        x = 2
        #for i in range(9):
        #    if (set(grid[i][:]) == full):
        #        print(grid[i][:]
        #        print_grid(grid)
        #        x=2

    #for i in range(9):
    #    print(set(grid[i][:]) == full)
