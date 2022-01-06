from sys import stdin

def apartments(k, desired_sizes, sizes):
    desired_sizes.sort()
    sizes.sort()
    i, j = 0, 0
    num_housed = 0
    while i < len(desired_sizes) and j < len(sizes):
        if abs(sizes[j] - desired_sizes[i]) <= k:
            num_housed += 1
            i += 1
            j += 1
        elif sizes[j] < desired_sizes[i]:
            j += 1
        else:
            i += 1
    return num_housed

if __name__ == '__main__':
    _, _, k = [int(num) for num in stdin.readline().split()]
    desired_sizes = [int(num) for num in stdin.readline().split()]
    sizes = [int(num) for num in stdin.readline().split()]
    print(apartments(k, desired_sizes, sizes))