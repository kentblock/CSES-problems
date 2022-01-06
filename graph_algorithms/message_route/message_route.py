from sys import stdin, stdout
from collections import deque

# Simple with BFS

def message_route(graph, end):
    visited = [False for _ in range(len(graph))]
    level = [0 for _ in range(len(graph))]
    prev = [-1 for _ in range(len(graph))]
    q = deque()
    q.append(1)

    while q:
        cur = q.popleft()
        if cur == end:
            break
        for u in graph[cur]:
            if not visited[u]:
                level[u] = level[cur] + 1
                prev[u] = cur
                visited[u] = True
                q.append(u)

    if not visited[end]:
        print("IMPOSSIBLE")
    else:
        print(level[end] + 1)
        path = []
        cur = end
        while True:
            path.append(cur)
            if cur == 1:
                break
            cur = prev[cur]
        print(' '.join([str(p) for p in path[::-1]]))

def read_num():
    return int(stdin.readline())

def read_nums():
    return [int(num) for num in stdin.readline().split()]

if __name__ == '__main__':
    n, m = read_nums()
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = read_nums()
        graph[u].append(v)
        graph[v].append(u)
    message_route(graph, n)
    