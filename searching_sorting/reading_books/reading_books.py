from sys import stdin

# fuck this fucking question is not hard but I can't quite handle all the cases elegantly
# come back tomorrow

def min_read_time(book_times):
    book_times.sort()
    l, r = 0, len(book_times) - 1
    lt, rt = 0, 0
    while l < r:
        if lt < rt:
            lt += book_times[l]
            l += 1
        else:
            rt += book_times[r]
            r += -1
    wait_time = 0
    diff = abs(rt - lt)
    if lt <= rt:
        wait_time = max(book_times[l] - (lt + diff), 0)
    else:
        wait_time = max(book_times[l] - (rt + diff), 0)
    return wait_time + lt + rt + book_times[l]

def read_num():
    return int(stdin.readline())

def read_nums():
    return [int(num) for num in stdin.readline().split()]

if __name__ == '__main__':
    _ = read_num()
    book_times = read_nums()
    print(min_read_time(book_times))