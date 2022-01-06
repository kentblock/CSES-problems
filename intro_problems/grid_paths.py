from sys import stdin

move_map = {(0, 1): "D", (1, 0): "R", (-1, 0): "L", (0, -1): "U"}

def grid_paths(path):
    marked = [[False for _ in range(7)] for _ in range(7)]

    def helper(position, path_length):
        if path_length == 49:
            print("found")
            return 1 if position[0] == 6 and not position[1] else 0
        print(position)
        for move, symbol in move_map.items():
            x, y = (move[0] + position[0], move[1] + position[1])
            s = 0
            if on_grid((x, y)) and not marked[x][y] \
                and (path[path_length] == "?" or path[path_length] == symbol):
                marked[x][y] = True
                #print(marked)
                s += helper((x, y), path_length + 1)
                marked[x][y] = False
        return s

    return helper((0, 0), 0)

def on_grid(pos):
    return pos[0] >= 0 and pos[0] < 7 and pos[1] >= 0 and pos[1] < 7


if __name__ == '__main__':

    path = list(stdin.readline())
    print(f"{grid_paths(path)}")