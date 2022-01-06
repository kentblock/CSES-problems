from sys import stdin

# Notes
# - Key realization 1: is that on player2's turn, minimizing player1's score is equivalent to maximizing player2's score.
# - Key realization 2: the turn is determined by i and j no need for an extra variable.

# tabulation solution TLE on CSES
def removal_game_tabulation(nums):
    if not nums:
        return 0
    dp = [[0 for _ in range(len(nums))] for _ in range(len(nums))]
    turn = (len(nums) - 1) & 1

    for k in range(len(nums)):
        dp[k][k] = nums[k] if not turn else 0

    for i in range(len(nums) -1, -1, -1):
        for j in range(i + 1, len(nums)):
            if turn == ((j - i) & 1):
                dp[i][j] = max(
                    nums[i] + dp[i + 1][j],
                    nums[j] + dp[i][j - 1]
                )
            else:
                dp[i][j] = min(
                    dp[i + 1][j],
                    dp[i][j - 1]
                )
    return dp[0][len(nums) - 1]

# memoization solution 
def removal_game_memo(nums):
    if not nums:
        return 0
    dp = [[-1 for _ in range(len(nums))] for _ in range(len(nums))]

    def solve(i, j, is_turn):
        if i > j:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        
        if is_turn:
            dp[i][j] = max(
                nums[i] + solve(i + 1, j, False),
                nums[j] + solve(i, j - 1, False)
            )
        else:
            dp[i][j] = min(
                solve(i + 1, j, True),
                solve(i, j - 1, True)
            )
        return dp[i][j]

    return solve(0, len(nums) - 1, True)

def read_num():
    return int(stdin.readline())

def read_nums():
    return [int(num) for num in stdin.readline().split()]

if __name__ == '__main__':
    _ = read_num()
    nums = read_nums()
    print(removal_game_tabulation(nums))
    
