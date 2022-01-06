import sys

# TODO this is trivial in python do it in C++ where you have to worry about overflow

if __name__ == '__main__':
    print((1 << int(sys.stdin.readline())) % (10 ** 9 + 7))
