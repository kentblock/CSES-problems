from sys import stdin

# TODO refactor, remove nested loops make things cleaner
# can store the index in the map so you can jump to the next position as well

def playlist(song_ids):
    played = {}
    max_unique = 0
    i, j = 0, 0
    while j < len(song_ids):
        id = song_ids[j]
        if id in played:
            while i < j:
                pop_id = song_ids[i]
                i += 1
                if pop_id == id:
                    break
                del played[pop_id]
        else:
            played[id] = True
        j += 1
        max_unique = max(j - i, max_unique)
    return max_unique

def read_num():
    return int(stdin.readline())

def read_nums():
    return [int(num) for num in stdin.readline().split()]

if __name__ == '__main__':
    _ = read_num()
    song_ids = read_nums()
    print(playlist(song_ids))
    