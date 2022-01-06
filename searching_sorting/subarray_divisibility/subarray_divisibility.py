from sys import stdin
from collections import Counter

# TODO this is fucking wrong

""" Use properties of mod arithmetic to reduce the problem to subarray sums II"""
def subarray_divisibility(nums, n):
    c = Counter()
    running_sum = 0
    c[0] = 1
    ans = 0
    for num in nums:
        running_sum += num % n
        ans += c[running_sum - n]
        c[running_sum] += 1
    return ans

def read_num():
    return int(stdin.readline())

def read_nums():
    return [int(num) for num in stdin.readline().split()]

if __name__ == '__main__':
    size = read_num()
    nums = read_nums()
    print(subarray_divisibility(nums, size))
    