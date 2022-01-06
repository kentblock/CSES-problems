from sys import stdin
from collections import Counter

""" 
    - Takes advantage of the fact that for, i < k, sum(nums[i:k]) = sum(nums[0:k]) - sum(nums[0:i])
    - Much simpler solution than the sliding window I used for subarray sums I
"""
def count_subarray_sums(size, nums):
    c = Counter()
    running_sum = 0
    c[0] = 1
    ans = 0
    for num in nums:
        running_sum += num
        ans += c[running_sum - size]
        c[running_sum] += 1
    return ans

def read_num():
    return int(stdin.readline())

def read_nums():
    return [int(num) for num in stdin.readline().split()]

if __name__ == '__main__':
    _, size = read_nums()
    nums = read_nums()
    print(count_subarray_sums(size, nums))
    