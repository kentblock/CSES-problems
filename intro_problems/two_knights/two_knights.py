import sys

# TODO refactor this to use a better solution the 2x3 / 3x2 block solution, maybe using c++??

def solve(n):
    dp = [0 for _ in range(max(n + 1, 5))]
    dp[2] = 6
    dp[3] = 28
    dp[4] = 96
    for i in range(5, n + 1):
        dp[i] = dp[i - 1]
        m = 2 * i - 1
        l = i ** 2
        dp[i] += (m - 7) * (l - 4)
        dp[i] += 3 * (l - 2)
        dp[i] += 4 * (l - 3)
        dp[i] -= ((m * (m + 1)) // 2) - 2

    for num in dp[1:n + 1]:
        print(num)


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    solve(n)


