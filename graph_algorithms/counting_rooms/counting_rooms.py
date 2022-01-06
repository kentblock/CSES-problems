from sys import stdin

def counting_rooms(room_map):
    rooms = 0
    for i in range(len(room_map)):
        for j in range(len(room_map[0])):
            if room_map[i][j]:
                dfs(room_map, (i, j))
                rooms += 1
    return rooms

def dfs(room_map, pos):
    i, j = pos
    if i < 0 or j < 0 or i >= len(room_map) or j >= len(room_map[0]) or not room_map[i][j]:
        return
    room_map[i][j] = 0
    dfs(room_map, (i + 1, j))
    dfs(room_map, (i, j + 1))
    dfs(room_map, (i - 1, j))
    dfs(room_map, (i, j - 1))


if __name__ == '__main__':
    room_map = []
    _ = stdin.readline()
    for line in stdin.readlines():
        room_map.append([1 if c == '.' else 0 for c in line if c != '\n'])
    print(counting_rooms(room_map))