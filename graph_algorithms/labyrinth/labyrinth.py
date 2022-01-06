from sys import stdin

MOVES = [((0, 1), 'R'), ((0, -1), 'L'), ((1, 0), 'D'), ((-1, 0), 'U')]


# TODO should print shortest path in the case that there are many valid paths
# TODO max recursion depth exceeded use stack based DFS ? 

def is_path(labyrinth):

    for i in range(len(labyrinth)):
        for j in range(len(labyrinth[0])):
            if labyrinth[i][j] == 'A':
                start = (i, j)
                break

    current_path = []

    def dfs(pos):
        i, j = pos
        if not 0 <= i < len(labyrinth) or not 0 <= j < len(labyrinth[0]) or labyrinth[i][j] == '#':
            return False

        if labyrinth[i][j] == 'B':
            print("YES")
            print(len(current_path))
            print(''.join(current_path))
            return True

        labyrinth[i][j] = '#'

        for m in MOVES:
            move, symbol = m
            current_path.append(symbol)
            if dfs(tuple(sum(x) for x in zip(pos, move))):
                return True
            current_path.pop()
        return False

    if not dfs(start):
        print("NO")

def read_num():
    return int(stdin.readline())

def read_nums():
    return [int(num) for num in stdin.readline().split()]

if __name__ == '__main__':
    _ = read_nums()
    labyrinth = []
    for line in stdin.readlines():
        labyrinth.append([c for c in line.rstrip('\n')])

    is_path(labyrinth)
