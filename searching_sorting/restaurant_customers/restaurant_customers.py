from sys import stdin

def max_customers(times):
    times.sort()
    m = 0
    cur_customers = 0
    max_func = max
    for i in range(len(times)):
        cur_customers += 1 if times[i][1] == "A" else -1
        m = max_func(m, cur_customers)
    return m

if __name__ == '__main__':
    n = int(stdin.readline())
    times = []
    for _ in range(n):
        a_time, d_time = [int(num) for num in stdin.readline().split()]
        times.append((a_time, "A"))
        times.append((d_time, "D"))
    print(max_customers(times))