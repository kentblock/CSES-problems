from sys import stdin
import time

# TLE might work in C++, there is probably a slicker solution though

""" Binary search the solution space """
def factory_machines(machine_times, num_products):
    max_time = (-(-sum(machine_times) // len(machine_times))) * -(-num_products // len(machine_times))
    s, e = 0, max_time
    while s < e:
        mid = (s + e) // 2
        if can_produce(num_products, mid, machine_times):
            e = mid
        else:
            s = mid + 1
    return s

def can_produce(num_products_needed, time, machine_times):
    num_produced = 0
    for t in machine_times:
        num_produced += time // t
        if num_produced >= num_products_needed:
            return True
    return num_produced >= num_products_needed


def read_num():
    return int(stdin.readline())

def read_nums():
    return [int(num) for num in stdin.readline().split()]

if __name__ == '__main__':
    _, products_needed = read_nums()
    machine_times = read_nums()
    print(factory_machines(machine_times, products_needed))
    