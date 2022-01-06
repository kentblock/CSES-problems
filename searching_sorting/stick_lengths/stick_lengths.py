from sys import stdin

def min_total_cost(stick_lengths):
    if not stick_lengths:
        return 0
    stick_lengths.sort()
    median = stick_lengths[len(stick_lengths) // 2]
    min_cost = 0
    for length in stick_lengths:
        min_cost += abs(length - median)
    return min_cost

def read_nums():
    return [int(num) for num in stdin.readline().split()]

if __name__ == '__main__':
    _ = read_nums()
    stick_lengths = read_nums()
    print(min_total_cost(stick_lengths))
    