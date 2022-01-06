import sys

def get_val(row, col):
    layer = max(row, col)
    val = layer ** 2
    if layer & 1:
        val += row + 1 + layer - col
    else:
        val += col + 1 + layer - row
    return val


if __name__ == '__main__':
    num_tests = int(sys.stdin.readline())
    for _ in range(num_tests):
        line = sys.stdin.readline()
        row, col = [int(num) for num in line.split()]
        print(f"{get_val(row - 1, col - 1)}")