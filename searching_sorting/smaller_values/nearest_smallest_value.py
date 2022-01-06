from sys import stdin

def get_nearest_smaller_values(nums):
    smaller_values = [-1]
    for i in range(1, len(nums)):
        val = nums[i]
        if nums[i - 1] < val:
            smaller_values.append(i - 1)
        else:
            j = smaller_values[i - 1]
            while j >= 0 and nums[j] >= val:
                j = smaller_values[j]
            smaller_values.append(j)

    return [index + 1 for index in smaller_values]

def read_num():
    return int(stdin.readline())

def read_nums():
    return [int(num) for num in stdin.readline().split()]

if __name__ == '__main__':
    _ = read_num()
    nums = read_nums()
    print(
        ' '.join([str(val) for val in get_nearest_smaller_values(nums)])
    )