from sys import stdin

# TLE 
def book_shop(prices, pages, max_price):
    dp = [0 for _ in range(max_price + 1)]
    for i in range(len(prices)):
        price = prices[i]
        for x in range(max_price - price, -1, -1):
            dp[x + price] = max(dp[x] + pages[i], dp[x + price])
    return dp[max_price]

def read_num():
    return int(stdin.readline())

def read_nums():
    return [int(num) for num in stdin.readline().split()]

if __name__ == '__main__':
    _, max_price = read_nums()
    prices = read_nums()
    pages = read_nums()
    print(book_shop(prices, pages, max_price))
    