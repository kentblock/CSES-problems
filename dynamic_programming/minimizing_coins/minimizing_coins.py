from sys import stdin

# TLE use cpp
def minimizing_coins(coins, s):
    dp = [-1 for _ in range(s + 1)]
    dp[0] = 0
    for i in range(1, len(dp)):
        for c in coins:
            if i - c >= 0 and dp[i - c] != -1:
                dp[i] = min(dp[i], dp[i - c] + 1) if dp[i] != -1 else dp[i - c] + 1
    return dp[s]
    
def read_num():
    return int(stdin.readline())

def read_nums():
    return [int(num) for num in stdin.readline().split()]

if __name__ == '__main__':
    _, sum_size = read_nums()
    coins = read_nums()
    print(minimizing_coins(coins, sum_size))
    