def isValid(x, y, sizeX, sizeY):
    return 0 <= x < sizeX and 0 <= y < sizeY

def findWordInDirection(grid, n, m, word, index, x, y, dirX, dirY):
    if index == len(word):
        return True
    if isValid(x, y, n, m) and word[index] == grid[x][y]:
        return findWordInDirection(grid, n, m, word, index + 1,  x + dirX, y + dirY, dirX, dirY)
    return False

def searchWord(grid, word):
    ans = []
    n = len(grid)
    m = len(grid[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    for i in range(n):
        for j in range(m):
            for dirX, dirY in directions:
                if grid[i][j] == word[0] and findWordInDirection(grid, n, m, word, 0, i, j, dirX, dirY):
                    ans.append([i, j])
    return ans

def read_matrix_from_file(filename):
    matrix = []
    with open(filename, 'r') as f:
        for line in f:
            row = list(line.strip().upper())
            matrix.append(row)
    return matrix

grid = read_matrix_from_file('day4.txt')
word = "XMAS"
ans = searchWord(grid, word)
print(len(ans))
