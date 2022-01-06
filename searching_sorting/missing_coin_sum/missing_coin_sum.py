from sys import stdin

def smallest_missing_sum(nums):
    nums.sort()
    have_sums_lte = 0
    for num in nums:
        if num - 1 > have_sums_lte:
            break
        have_sums_lte += num
    return have_sums_lte + 1


def read_nums():
    return [int(num) for num in stdin.readline().split()]

if __name__ == '__main__':
    _ = read_nums()
    nums = read_nums()
    print(smallest_missing_sum(nums))
