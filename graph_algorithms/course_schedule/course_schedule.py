from sys import stdin

# There is a schedule iff graph is a DAG, graph is a DAG iff it has a topological sort
# Use dfs to find a topological sort if possible

# TODO do iteratively, gets stack overflow for one testcase on CSES

def course_schedule(graph):
    visited = [0 for _ in range(len(graph))]
    topo_sort = []

    def dfs(node):
        if not visited[node]:
            visited[node] = 1
            for u in graph[node]:
                if not dfs(u):
                    return False
            visited[node] = 2
            topo_sort.append(node)
        elif visited[node] == 1:
            return False   
        return True

    for i in range(1, len(graph)):
        if not visited[i]:
            if not dfs(i):
                print("IMPOSSIBLE")
                return

    print(' '.join([f"{num}" for num in topo_sort[::-1]]))

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
    course_schedule(graph)


    