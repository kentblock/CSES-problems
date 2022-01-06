from sys import stdin


if __name__ == '__main__':

    n = int(stdin.readline())
    for _ in range(n):
        a, b = [int(num) for num in stdin.readline().split()]
        if not min(a, b) and max(a, b):
            print("NO")
        elif min(a, b) * 2 == max(a, b) or (min(a, b) - abs(a - b)) % 3 == 0:
            print("YES")
        else:
            print("NO")