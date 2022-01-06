from sys import stdin

MOD = 10 ** 9 + 7

# Knapsack problem
# Can reduce space from O(n^3) to O(n^2) using knapsack technique
# TLE in CSES
def two_sets(n):
    s = n * (n + 1) // 2
    if s % 2 != 0:
        return 0
    target = s // 2
    dp = [[0 for _ in range(target + 1)] for _ in range(n + 1)]
    dp[0][0] = 1 
    for i in range(1, len(dp)):
        dp[i][0] = 1
        for j in range(1, len(dp[0])):
            dp[i][j] = dp[i - 1][j] + (dp[i - 1][j - i] if j - i >= 0 else 0)
    return (dp[n][target] // 2) % MOD

def read_num():
    return int(stdin.readline())

def read_nums():
    return [int(num) for num in stdin.readline().split()]

if __name__ == '__main__':
    print(two_sets(read_num()))