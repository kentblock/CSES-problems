from sys import stdin
import math

# TODO TLE O(n ^ 3) 
def rectangle_cutting(h, w):
    dp = [[0 for _ in range(h + 1)] for _ in range(w + 1)]
    for i in range(1, w + 1):
        for j in range(1, h + 1):
            if i == j:
                dp[i][j] = 0
                continue
            dp[i][j] = math.inf
            for k in range(1, i):
                dp[i][j] = min(dp[i][j], dp[k][j] + dp[i - k][j] + 1)
            for k in range(1, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[i][j - k] + 1)
    return dp[w][h]

def read_num():
    return int(stdin.readline())

def read_nums():
    return [int(num) for num in stdin.readline().split()]

if __name__ == '__main__':
    height, width = read_nums()
    print(rectangle_cutting(height, width))