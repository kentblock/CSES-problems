from sys import stdin
from math import inf

def max_subarray_sum(nums):
    max_sum = -inf
    cur_max = -inf
    for num in nums:
        cur_max = max(num + cur_max, num)
        max_sum = max(cur_max, max_sum)
    return max_sum

def read_nums():
    return [int(num) for num in stdin.readline().split()]

def read_num():
    return int(stdin.readline())

if __name__ == '__main__':
    _ = read_num()
    nums = read_nums()
    print(max_subarray_sum(nums))
    