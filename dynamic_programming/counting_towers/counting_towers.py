from sys import stdin
mod = 10 ** 9 + 7

def counting_towers(height):
    dp = [[0 for _ in range(6)] for _ in range(height + 1)]
    dp[0][3] = 1
    for i in range(1, height + 1):
        all = sum(dp[i - 1])
        for j in range(6):
            if j == 0:
                dp[i][j] = dp[i - 1][3] + dp[i - 1][5] + dp[i - 1][0]
            elif j == 1:
                dp[i][j] = all - dp[i - 1][0]
            elif j == 2:
                dp[i][j] = all - dp[i - 1][0]
            elif j == 3:
                dp[i][j] = dp[i - 1][5] + dp[i - 1][0] + dp[i - 1][3]
            elif j == 4:
                dp[i][j] = all - dp[i - 1][0]
            else:
                dp[i][j] = all - dp[i - 1][0]
            dp[i][j] %= mod
    return (dp[height][3] + dp[height][5]) % mod


def read_num():
    return int(stdin.readline())

def read_nums():
    return [int(num) for num in stdin.readline().split()]

if __name__ == '__main__':
    print(counting_towers(int(stdin.readline())))

    