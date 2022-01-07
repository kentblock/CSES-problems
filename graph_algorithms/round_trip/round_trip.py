from sys import stdin, stdout

# Cycle detection - use iterative DFS

def round_trip(graph):
    visited = [False for _ in range(len(graph))]
    prev = [-1 for _ in range(len(graph))]

    for node in range(1, len(graph)):
        if visited[node]:
            continue
        s = []
        s.append(node)
        while s:
            cur = s.pop()
            if visited[cur]:
                continue
            visited[cur] = True
            for u in graph[cur]:
                if visited[u] and u != prev[cur]:
                    v = cur
                    cycle = []
                    while v != u:
                        cycle.append(f"{v}")
                        v = prev[v]
                    cycle = [f"{u}"] + cycle + [f"{u}"]
                    print(len(cycle))
                    print(' '.join(cycle))
                    return
                if not visited[u]:
                    prev[u] = cur
                    s.append(u)

    print("IMPOSSIBLE")


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
    round_trip(graph)
    