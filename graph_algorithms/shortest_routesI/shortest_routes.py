from sys import stdin
import math, heapq

# Dijkstras

def shortest_route(graph):
    dist = [math.inf for _ in range(len(graph))]
    dist[1] = 0
    visited = [False for _ in range(len(graph))]
    pq = [(0, 1)]
    while pq:
        _, v = heapq.heappop(pq)
        if visited[v]:
            continue
        visited[v] = True
        for u, weight in graph[v]:
            if dist[v] + weight < dist[u]:
                dist[u] = dist[v] + weight
                heapq.heappush(pq, (dist[u], u))

    print(' '.join([f"{d}" for d in dist[1:]]))

def read_num():
    return int(stdin.readline())

def read_nums():
    return [int(num) for num in stdin.readline().split()]

if __name__ == '__main__':
    n, m = read_nums()
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, weight = read_nums()
        graph[u].append((v, weight))
    shortest_route(graph)
    