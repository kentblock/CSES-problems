from sys import stdin
from collections import deque

# Bipartite graph check using BFS
# Idea check if all connected components of graph are bipartite, if not then it is impossible

def building_teams(graph):

    level = [0 for _ in range(len(graph))]
    visited = [False for _ in range(len(graph))]

    def bfs(start):
        q = deque()
        q.append(start)
        visited[start] = True
        level[start] = 1
        while q:
            cur = q.popleft()
            for u in graph[cur]:
                if visited[u] and level[u] & 1 != (level[cur] + 1) & 1:
                    print("IMPOSSIBLE")
                    return False
                elif not visited[u]:
                    visited[u] = True
                    level[u] = level[cur] + 1
                    q.append(u)
        return True

    for i in range(len(graph)):
        if not visited[i] and not bfs(i):
            return

    print(' '.join([str((l & 1) + 1) for l in level]))

def read_num():
    return int(stdin.readline())

def read_nums():
    return [int(num) for num in stdin.readline().split()]

if __name__ == '__main__':
    n, m = read_nums()
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v = read_nums()
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)
    building_teams(graph)