# A recursive backtracking program to solve a Sudoku grid


# Function to print the grid.
def print_grid(arr):
    print '+ - - - - - - - - - - - +'
    for i in range(9):
        for j in range(9):
            if j % 3 == 0:
                print '|',
            print arr[i][j],
        print '|',
        if (i+1) % 3 == 0:
            print '\n+ - - - + - - - + - - - +'
        else:
            print ('\n')


# Function to find square that is still not used.
# Square coordinates and stored in l.
def find_empty_square(arr, l):
    for row in range(9):
        for col in range(9):
            if arr[row][col] == 0:
                l[0] = row
                l[1] = col
                return True
    return False


# Function to indicate if num can be used in row.
def already_in_row(arr, row, num):
    for i in range(9):
        if arr[row][i] == num:
            return True
    return False


# Function to indicate if num can be used in col.
def already_in_col(arr, col, num):
    for i in range(9):
        if arr[i][col] == num:
            return True
    return False


# Function to indicate if num can be used in 3x3 box around (row,col).
def already_in_box(arr, row, col, num):
    for i in range(3):
        for j in range(3):
            if arr[i + row - row % 3][j + col - col % 3] == num:
                return True
    return False


# Function to check if num can be used in (row,col).
def check_square_is_safe(arr, row, col, num):
    return not already_in_row(arr, row, num) and \
           not already_in_col(arr, col, num) and \
           not already_in_box(arr, row, col, num)


# Main function.
def solve(arr):
    # Coordinates of empty square.
    l = [0, 0]

    # OK if any square in the grid is empty.
    if not find_empty_square(arr, l):
        return True

    row = l[0]
    col = l[1]

    for num in range(1, 10):

        # If num can be used.
        if check_square_is_safe(arr, row, col, num):

            # Try with num.
            arr[row][col] = num

            # OK if we can solve the problem using num in this position.
            if solve(arr):
                return True

            # Otherwise we try with another num.
            arr[row][col] = 0

    # No solution.
    return False


# Initializing the grid.
grid = [[3, 6, 2, 1, 0, 0, 0, 0, 7],
        [5, 0, 9, 0, 0, 0, 0, 0, 8],
        [0, 7, 0, 0, 5, 0, 0, 4, 0],
        [4, 5, 3, 0, 9, 0, 0, 1, 0],
        [2, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 2, 6, 3, 0],
        [0, 0, 0, 9, 1, 0, 8, 5, 0],
        [0, 0, 0, 0, 6, 3, 2, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 4]]

# Print problem.
print("\nProblem:")
print_grid(grid)

# Print solution.
print("\nSolution:")
if solve(grid):
    print_grid(grid)
else:
    print "No solution"
