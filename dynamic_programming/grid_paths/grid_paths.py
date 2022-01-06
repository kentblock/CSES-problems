from sys import stdin

mod = 10 ** 9 + 7

def grid_paths(grid):
    if not grid or grid[0][0] == -1:
        return 0
    grid[0][0] = 1
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == -1:
                continue
            if i:
                grid[i][j] += max(grid[i - 1][j], 0)
            if j:
                grid[i][j] += max(grid[i][j - 1], 0)
            grid[i][j] %= mod
    return grid[-1][-1] if grid[-1][-1] != -1 else 0

def read_num():
    return int(stdin.readline())

def read_nums():
    return [int(num) for num in stdin.readline().split()]

if __name__ == '__main__':
    _ = read_num()
    grid = []
    for line in stdin.readlines():
        grid.append([-1 if c == '*' else 0 for c in line if c != '\n'])
    print(grid_paths(grid))
    