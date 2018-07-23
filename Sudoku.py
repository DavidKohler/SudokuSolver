#!/usr/bin/env python3
#Sudoku.py
'''
Author: David Kohler
Sudoku Solver
'''

import random
import sys

#Example 17 starting clue puzzle (Smallest number of starting clues possible)
#000801000000000430500000000000070800000000100020030000600000075003400000000200600

def print_grid(grid):
    '''
    Prints the grid in a more readible format
    '''
    colcnt, rowcnt = 0, 0
    for i in range(9):
        for j in range(9):
            colcnt+=1
            if (grid[i][j] == 0):
                print('x', end=' ')
            else:
                print(grid[i][j], end=' ')
            if (colcnt == 3) or (colcnt == 6):
                print('|', end=' ')
        rowcnt += 1
        print()
        if (rowcnt == 3) or (rowcnt == 6):
            print('------+-------+-------')
        colcnt = 0
    print()

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
    print("Please enter the puzzle you wish to solve")
    print("Enter in format reading left to right, top to")
    print("bottom, as one string. Indicate blank cells with 0")
    print("For example:10345670912005608012... etc")
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

def solve_puzzle():
    '''
    Start solving a puzzle passed in by the user.
    Starts at 0,0 (box 1)
    '''
    print()
    gridToSolve = input_grid()
    print_grid(gridToSolve)
    print("Does this puzzle look correct? (y/n)")
    response = input()
    while((response.lower() != 'y') and (response.lower() != 'n')):
        print("Enter 'y' for yes, or 'n' for no")
        response = input()
    if (response.lower() == 'n'):
        solve_puzzle()
    if (solve(gridToSolve) == False):
        print("No solution found")
        sys.exit()
    print_grid(gridToSolve)
    print("Puzzle completed!")


def solve(grid, x = 0, y = 0):
    '''
    Process of solving grid, one cell at a timeself.
    Uses backtracking to find correct cell value
    '''
    #Move to next 0 cell
    xn, yn = next_open(grid, x, y)
    #Check if puzzle is filled already
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

def new_puzzle():
    '''
    Creates a new puzzle and returns it with a
    certain number of starting hints, based on
    the selected difficulty. Also returns solution
    '''
    print()
    print("Select puzzle difficulty to create")
    print("Enter 1 for Very Easy")
    print("Enter 2 for Easy")
    print("Enter 3 for Medium")
    print("Enter 4 for Hard")
    print("Enter 5 for Expert")
    print("Enter 6 for Insane")
    difficulty = input()
    while((difficulty != "1") and (difficulty != "2") and (difficulty != "3")
                                and (difficulty != "4") and (difficulty != "5")
                                and (difficulty != "6")):
        print("Please enter a valid input")
        option = input()
    puzzle, solution = make_puzzle(difficulty)
    while (grid_success(solution) != 0):
        puzzle, solution = make_puzzle(difficulty)
    print()
    print_grid(puzzle)
    print("Do you want the solution? (y/n)")
    response = input()
    while((response.lower() != 'y') and (response.lower() != 'n')):
        print("Enter 'y' for yes, or 'n' for no")
        response = input()
    if (response.lower() == 'n'):
        sys.exit()
    else:
        print()
        print_grid(solution)

def make_puzzle(diff):
    '''
    Creates a new Sudoku puzzle by randomly choosing
    20 numbers and then solving the puzzle from that
    '''
    solvedGrid = [[0 for x in range(9)] for y in range(9)]
    solvedGrid[0][0] = random.randint(1, 9)
    x, y = 0, 0
    for i in range(20):
        x, y = next_open(solvedGrid, x, y)
        z = rand_num(solvedGrid, x, y)
        solvedGrid[x][y] = z
    solve(solvedGrid)
    if diff == "1":
        #35 blank spots, 46 starting hints
        grid = blankify(solvedGrid, 35)
    elif diff == "2":
        #42 blank spots, 39 starting hints
        grid = blankify(solvedGrid, 42)
    elif diff == "3":
        #50 blank spots, 31 starting hints
        grid = blankify(solvedGrid, 50)
    elif diff == "4":
        #55 blank spots, 26 starting hints
        grid = blankify(solvedGrid, 55)
    elif diff == "5":
        #59 blank spots, 22 starting hints
        grid = blankify(solvedGrid, 59)
    else:
        #64 blank spots, 17 starting hints
        #Lowest number of starting hints mathematically possible
        grid = blankify(solvedGrid, 64)
    return grid, solvedGrid

def blankify(origGrid, num):
    '''
    Takes a solved grid and adds number num blanks
    to create an unsolved puzzle grid
    '''
    grid = [row[:] for row in origGrid]
    coordsVisited = set([])
    for i in range(num):
        randX, randY = random.randint(0, 8), random.randint(0, 8)
        while ((randX, randY) in coordsVisited):
            randX, randY = random.randint(0, 8), random.randint(0, 8)
        coordsVisited.add((randX, randY))
        grid[randX][randY] = 0
    return grid

def rand_num(grid, x, y):
    '''
    Chooses a number randomly such that it would be
    a valid placement at the given coordinates
    '''
    num = random.randint(1, 9)
    while (isValidPlace(grid, x, y, num) == False):
        num = random.randint(1, 9)
    return num

def verify_puzzle():
    '''
    Verifies existing puzzle based on input grid
    from the user. Will return a success or what
    kind of conflict was found
    '''
    print("Please enter the puzzle you wish to verify")
    print("Enter in format reading left to right, top to")
    print("bottom, as one string: 12345678912345678912...")
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

def isValidPlace(grid, x, y, z):
    '''
    Checks for valid placement of z at x, y
    '''
    if (z in grid[x]):
        #z is already in this row
        return False
    if (z in [grid[i][y] for i in range(9)]):
        #z is already in this column
        return False
    #Find the top right cell coordinates in box
    x0, y0 = (3 * (x//3)), (3 * (y//3))
    for ix in range(x0, x0+3):
        for iy in range(y0, y0+3):
            if (z == grid[ix][iy]):
                #z already in this box
                return False
    return True

def check_boxes(grid):
    '''
    Checks 4 of the grid's boxes. Namely
    boxes 1, 2, 4, and 5. This is the minimum
    amount of boxes to check to verify a complete
    Sudoku grid
    '''
    full = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
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

def grid_success(grid):
    '''
    Checks if grid is complete
    '''
    full = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
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

if __name__ == '__main__':
    option = user_select()
    print()
    if option == 1:
        solve_puzzle()
    elif option == 2:
        new_puzzle()
    elif option == 3:
        verify_puzzle()
