from sys import stdin

# TLE in CSES
mod = 10 ** 9 + 7
def coin_combinations(coins, s):
    dp = [0 for _ in range(s + 1)]
    dp[0] = 1
    for i in range(len(dp)):
        for c in coins:
            if i - c >= 0:
                dp[i] += dp[i - c]
                dp[i] %= mod
    return dp[s]

def read_num():
    return int(stdin.readline())

def read_nums():
    return [int(num) for num in stdin.readline().split()]

if __name__ == '__main__':
    _, sum_size = read_nums()
    coins = set(read_nums())
    print(coin_combinations(coins, sum_size))
    