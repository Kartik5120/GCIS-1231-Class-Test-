"""# function that returns 2d list of numbers from sudoku
def readSudoku(file_name):
    row, column = 9, 9
    int_list = [[0 for x in range(row)] for y in range(column)]
    file = open(file_name, "r")
    lines = 0

    while(lines != 9):  # read while lines counter is not 9
        # read each line from txt file(strip() is used to remove \n from lines)
        line = file.readline().strip()
        # j counter to use column index of 2d list (j goes from 0 to 9) after that characters end from line
        j = 0
        for i in line:  # traversing each character of currently read line
            # assigning each character to 2d list
            int_list[lines][j] = int(i)
            j += 1  # increasing j counter by 1
        lines += 1  # increasing lines counter by 1
    file.close()  # closing file after reading

    return int_list  # returning 2d list

def validate(sudoku):
    rows = set()
    cols = set()
    # checks the rows and cols valid numbers in or not
    # and returns True if valid else False
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] in list(range(0,10)) and sudoku[j][i] in list(range(0,10)):
                rows.add(sudoku[i][j])
                cols.add(sudoku[j][i])
        if len(rows) != 9 or len(cols) != 9:
            return False
        rows.clear()
        cols.clear()
    return True


def main():  # main method
    file_name = input("Enter file name : ")  # input file name
    print(readSudoku(file_name))  # call function and print the returned list
    
main()"""

# N is the size of the 2D matrix N*N
N = 9

# A utility function to print grid
def printing(arr):
	for i in range(N):
		for j in range(N):
			print(arr[i][j], end = " ")
		print()

# Checks whether it will be
# legal to assign num to the
# given row, col
def isSafe(grid, row, col, num):

	# Check if we find the same num
	# in the similar row , we
	# return false
	for x in range(9):
		if grid[row][x] == num:
			return False

	# Check if we find the same num in
	# the similar column , we
	# return false
	for x in range(9):
		if grid[x][col] == num:
			return False

	# Check if we find the same num in
	# the particular 3*3 matrix,
	# we return false
	startRow = row - row % 3
	startCol = col - col % 3
	for i in range(3):
		for j in range(3):
			if grid[i + startRow][j + startCol] == num:
				return False
	return True

# Takes a partially filled-in grid and attempts
# to assign values to all unassigned locations in
# such a way to meet the requirements for
# Sudoku solution (non-duplication across rows,
# columns, and boxes) */
def solveSudoku(grid, row, col):

	# Check if we have reached the 8th
	# row and 9th column (0
	# indexed matrix) , we are
	# returning true to avoid
	# further backtracking
	if (row == N - 1 and col == N):
		return True
	
	# Check if column value becomes 9 ,
	# we move to next row and
	# column start from 0
	if col == N:
		row += 1
		col = 0

	# Check if the current position of
	# the grid already contains
	# value >0, we iterate for next column
	if grid[row][col] > 0:
		return solveSudoku(grid, row, col + 1)
	for num in range(1, N + 1, 1):
	
		# Check if it is safe to place
		# the num (1-9) in the
		# given row ,col ->we
		# move to next column
		if isSafe(grid, row, col, num):
		
			# Assigning the num in
			# the current (row,col)
			# position of the grid
			# and assuming our assigned
			# num in the position
			# is correct
			grid[row][col] = num

			# Checking for next possibility with next
			# column
			if solveSudoku(grid, row, col + 1):
				return True

		# Removing the assigned num ,
		# since our assumption
		# was wrong , and we go for
		# next assumption with
		# diff num value
		grid[row][col] = 0
	return False

# Driver Code

# 0 means unassigned cells
grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
		[5, 2, 0, 0, 0, 0, 0, 0, 0],
		[0, 8, 7, 0, 0, 0, 0, 3, 1],
		[0, 0, 3, 0, 1, 0, 0, 8, 0],
		[9, 0, 0, 8, 6, 3, 0, 0, 5],
		[0, 5, 0, 0, 9, 0, 6, 0, 0],
		[1, 3, 0, 0, 0, 0, 2, 5, 0],
		[0, 0, 0, 0, 0, 0, 0, 7, 4],
		[0, 0, 5, 2, 0, 6, 3, 0, 0]]

if (solveSudoku(grid, 0, 0)):
	printing(grid)
else:
	print("no solution exists ")
