import sys
from collections import Counter

# hash map solution
def get_num_distinct(numbers):
    return len(Counter(numbers).keys())

# sorting solution
def get_num_distinct2(numbers):
    if len(numbers) <= 1:
        return len(numbers)
    numbers.sort()
    num_distinct = 0
    for i in range(len(numbers) - 1):
        if numbers[i] != numbers[i + 1]:
            num_distinct += 1
    
    return num_distinct + 1

if __name__ == '__main__':
    _ = sys.stdin.readline()
    numbers = [int(num) for num in sys.stdin.readline().split()]
    print(f"{get_num_distinct2(numbers)}")

