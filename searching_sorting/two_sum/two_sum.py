from sys import stdin
from collections import Counter

not_possible_output = "IMPOSSIBLE"

# ugly solution
def two_sum_ugly(nums, target):
    sorted_nums = sorted(nums)
    s, e = 0, len(nums) - 1
    while s < e:
        left, right = sorted_nums[s], sorted_nums[e]
        num = left + right
        if num == target:
            l_index, r_index = nums.index(left), None
            if left == right:
                r_index = nums.index(right, l_index + 1)
            else:
                r_index = nums.index(right)
            print(f"{l_index + 1} {r_index + 1}")
            return
        elif num < target:
            s += 1
        else:
            e -= 1
    print(not_possible_output)

def two_sum_clean(nums, target):
    d = {}
    for i, num in enumerate(nums):
        other_num = target - num
        if other_num in d:
            print(f"{d[other_num] + 1} {i + 1}")
            return
        else:
            d[nums[i]] = i
    print(not_possible_output)


def read_nums():
    return [int(num) for num in stdin.readline().split()]

if __name__ == '__main__':
    _, target = read_nums()
    nums = read_nums()
    two_sum_clean(nums, target)