from sys import stdin

def towers(cube_queue):
    towers = []
    for cube in cube_queue:
        index = find_tower(towers, cube)
        if index == -1:
            towers.append(cube)
        else:
            towers[index] = cube
    return len(towers)

def find_tower(towers, size):
    if not towers or towers[-1] <= size:
        return -1
    s, e = 0, len(towers) - 1
    while s < e:
        mid = (s + e) // 2
        if towers[mid] > size:
            e = mid
        else:
            s = mid + 1
    return s 

def read_num():
    return int(stdin.readline())

def read_nums():
    return [int(num) for num in stdin.readline().split()]

if __name__ == '__main__':
    _ = read_num()
    cube_sizes = read_nums()
    print(towers(cube_sizes))
    