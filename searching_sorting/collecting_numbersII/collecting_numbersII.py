from sys import stdin
from math import inf

# TODO this is garbage, need to regroup and try again

def num_min_rounds(nums, swaps):
    index_list = [-1 for _ in range(len(nums) + 1)]

    for i in range(len(nums)):
        num = nums[i]
        index_list[num] = i

    num_min_rounds = 1
    for i in range(2, len(index_list)):
        if index_list[i] < index_list[i - 1]:
            num_min_rounds += 1

    for swap in swaps:
        a_index, b_index = swap
        a, b = nums[a_index - 1], nums[b_index] - 1

        if abs(a - b) == 1:
            num_min_rounds += round_change_neighbours(a_index, b_index)
        else:
            num_min_rounds += round_change(a_index)
            num_min_rounds += round_change(b_index)

        
        print(num_min_rounds)


def round_change(num, from_index, to_index, index_list):
    left = index_list[num - 1] if num > 1 else -1
    right = index_list[num + 1] if num < len(index_list) - 1 else inf

    if (from_index < min(left, right) or from_index > max(left, right)) and left < to_index and to_index < right:
        return 1
    
    if (to_index < min(left, right) or to_index > max(left, right)) and left < from_index and from_index < right:
        return -1

    return 0


def round_change_neighbours(a, b, a_index, b_index, index_list):
    max_index = a_index if a > b else b_index
    min_index = a_index if a < b else b_index
    


def read_nums():
    return [int(num) for num in stdin.readline().split()]

if __name__ == '__main__':
    _, m = read_nums()
    nums = read_nums()
    swaps = []
    for _ in range(m):
        swaps.append(tuple(read_nums()))
    num_min_rounds(nums, swaps)