def solve(bo):
    """
    It solves the sudoku puzzle using backtracking algorithm.
    It returns the solution.
    param bo: 2d list of ints
    """
    find = find_empty(bo)
    if find:
        row, col = find
    else:
        return True

    for i in range(1,10):
        if check(bo, (row, col), i):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def check(bo, pos, num):
    """
    It returns True if the attempted move is check else returns False.
    param bo: 2d list of ints
    param pos: (row, col)
    param num: int
    """

    # Check the number in row
    for i in range(0, len(bo)):
        if bo[pos[0]][i] == num:
            return False

    # Check the number in column
    for i in range(0, len(bo)):
        if bo[i][pos[1]] == num:
            return False

    # Check the number in box
    box_x = pos[1]//3
    box_y = pos[0]//3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if bo[i][j] == num:
                return False

    return True


def find_empty(bo):
    '''It finds an empty space in the board and returns its position.
    :param bo: partially complete board'''

    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)

    return None

#==================================================

bo = []
row = []

with open("D:/Work/PROJECTS/Jocuri/Sudoku/Level 2.txt", "r") as file:
    for line in file:
        for elem in line:
            if elem != "\n":
                row.append(int(elem))
        bo.append(row)
        row = []

unsolved = list(map(list, bo))
solve(bo)
solved = list(map(list, bo))
