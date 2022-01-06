from sys import stdin

def num_min_rounds(nums):
    index_list = [-1 for _ in range(len(nums) + 1)]

    for i in range(len(nums)):
        num = nums[i]
        index_list[num] = i

    num_min_rounds = 1
    for i in range(2, len(index_list)):
        if index_list[i] < index_list[i - 1]:
            num_min_rounds += 1
    return num_min_rounds

def read_nums():
    return [int(num) for num in stdin.readline().split()]

if __name__ == '__main__':
    _ = read_nums()
    nums = read_nums()
    print(num_min_rounds(nums))