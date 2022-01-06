from sys import stdin
from collections import deque

# Simple solution using BFS

def build_roads(graph):
    visited = [False for _ in range(len(graph))]
    component_representatives = []

    for u in range(1, len(graph)):
        if not visited[u]:
            component_representatives.append(u)
            bfs(graph, u, visited)

    print(len(component_representatives) - 1)
    for i in range(1, len(component_representatives)):
        print(f"{component_representatives[i - 1]} {component_representatives[i]}")

def bfs(graph, s, visited):
    q = deque()
    q.append(s)
    while q:
        cur = q.popleft()
        for u in graph[cur]:
            if not visited[u]:
                visited[u] = True
                q.append(u)

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
    build_roads(graph)