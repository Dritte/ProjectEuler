dim = 1001
matrix = [[0 for i in xrange(dim)] for j in xrange(dim)]
n = 1
start_col = dim/2
start_row = dim/2 
matrix[start_row][start_col] = 1
for radius in xrange(1, dim/2+1):
    start_col += 1
    start_row -= 1
    for (col_dir, row_dir) in [(0,1),(-1,0),(0,-1),(1,0)]:
        for move in xrange(radius * 2):
            n +=1
            start_col += col_dir
            start_row += row_dir
            matrix[start_row][start_col] = n
sumy = -1
for row in xrange(dim):
    sumy += matrix[row][row]
    sumy += matrix[row][dim - 1 - row]
print sumy
