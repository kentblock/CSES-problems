from sys import stdin

""" Use sliding window to count sums """
def count_subarray_sums(size, nums):
    l, r = 0, 0
    current_sum = 0
    ans = 0
    while l < len(nums):
        if current_sum < size:
            if r == len(nums):
                break
            current_sum += nums[r]
            r += 1
        else:
            if current_sum == size:
                ans += 1
            current_sum -= nums[l]
            l += 1
    return ans

def read_num():
    return int(stdin.readline())

def read_nums():
    return [int(num) for num in stdin.readline().split()]

if __name__ == '__main__':
    _, size = read_nums()
    nums = read_nums()
    print(count_subarray_sums(size, nums))
    