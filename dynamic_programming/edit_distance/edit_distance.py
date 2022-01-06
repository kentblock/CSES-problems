from sys import stdin
import math

# memoization
def edit_distance_memo(s1, s2):

    dp = [[-1 for _ in range(len(s2))] for _ in range(len(s1))]

    def solve(i, j):
        if i >= len(s1):
            return math.inf if j != len(s2) else 0

        if j == len(s2):
            return len(s1) - i - 1
    
        if dp[i][j] != -1:
            return dp[i][j]

        dp[i][j] = min(
            [
                solve(i + 1, j + 1) + (1 if s2[j] != s1[i] else 0),
                solve(i + 1, j) + 1,
                solve(i, j + 1) + 1
            ]
        )
        return dp[i][j]
    return solve(0, 0)

# tabulation
def edit_distance_tabulation(s1, s2):
    dp = [[-1 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
    for i in range(len(s1) + 1):
        for j in range(len(s2) + 1):
            if not i:
                dp[i][j] = j - 1
            elif not j:
                dp[i][j] = i - 1
            elif s2[j - 1] == s1[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(
                    [
                        dp[i - 1][j - 1],
                        dp[i - 1][j],
                        dp[i][j - 1]
                    ]
                ) + 1
    return dp[-1][-1] 

if __name__ == '__main__':
    print(edit_distance_tabulation(stdin.readline(), stdin.readline()))
    