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
    #Checks that grid was input in correct format
    while (check_valid_grid(rawList) == False):
        print("Incorrect format for grid. Please try again")
        rawGrid = input()
        rawList = list(rawGrid)
    #Initialize 9x9 empty grid
    grid = [[0 for x in range(9)] for y in range(9)]
    #Fill in grid values
    for j in range(9):
        grid[j] = [int(rawList[i+(j*9)]) for i in range(9)]
    return grid

def check_valid_grid(gridlist):
    '''
    Checks that grid was input in correct format
    '''
    #Makes sure every item is a digit
    for item in gridlist:
        if (item.isdigit() == False):
            print("Grid contains non-digit item")
            return False
    #Makes sure string entered is of correct length
    if (len(gridlist) != 81):
        print("Grid of incorrect length")
        return False
    return True

#TODO SOLVE SUDOKU GRID
def solve_puzzle():
    '''
    Start solving a puzzle passed in by the user.
    Starts at 0,0 (box 1)
    '''
    print()
    gridToSolve = input_grid()
    solve(gridToSolve)
    print_grid(gridToSolve)
    print("Puzzle completed!")


def solve(grid, x = 0, y = 0):
    '''
    Process of solving grid, one cell at a timeself.
    Uses backtracking to find correct cell value
    '''
    xn, yn = next_open(grid, x, y)
    #Check if puzzle is filled
    if (xn == -1):
        return True
    for z in range(1,10):
        #Checks for valid cell placement
        if isValidPlace(grid, xn, yn, z):
            grid[xn][yn] = z
            if (solve(grid, xn, yn)):
                return True
            #Resets cell
            grid[xn][yn] = 0
    return False


def isValidPlace(grid, x, y, z):
    '''
    Checks for valid placement of z at x,y
    '''
    if (z in grid[x]):
        #z is already in this row
        return False
    if (z in [grid[i][y] for i in range(9)]):
        #z is already in this column
        return False
    #Find the top right cell coordinates in box
    topX, topY = (3 * (x//3)), (3 * (y//3))
    for ix in range(topX, topX+3):
        for iy in range(topY, topY+3):
            if (z == grid[ix][iy]):
                #z already in this box
                return False
    return True

#TODO CREATE NEW SUDOKU
def new_puzzle():
    print("new under construction")

def verify_puzzle():
    '''
    Verifies existing puzzle based on input grid
    from the user. Will return a success or what
    kind of conflict was found
    '''
    print("Please enter the puzzle you wish to verify")
    print("Enter in format 123456789123456789123... etc")
    gridToCheck = input_grid()
    print_grid(gridToCheck)
    print("Is this the correct puzzle? (Enter y/n)")
    response = input()
    while((response.lower() != 'y') and (response.lower() != 'n')):
        print("Enter 'y' for yes, or 'n' for no")
        response = input()
    if (response.lower() == 'n'):
        verify_puzzle()
    else:
        print("Verifying puzzle...")
        result = grid_success(gridToCheck)
        if (result == 1):
            print("Puzzle incorrect. Conflict in row(s)")
        elif (result == 2):
            print("Puzzle incorrect. Conflict in column(s)")
        elif (result == 3):
            print("Puzzle incorrect. Conflict in box(s)")
        else:
            print("Puzzle solved correctly! Congratulations!")

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
    #Checks each row for unique 9 numbers
    for i in range(9):
        if set(grid[i][:]) != full:
            return 1
    #Checks each column for unique 9 numbers
    for j in range(9):
        if set([x[j] for x in grid]) != full:
            return 2
    #Checks each 3x3 box for unique 9 numbers
    if check_boxes(grid) == False:
        return 3
    return 0

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
    print()
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
