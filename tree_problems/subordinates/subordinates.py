from sys import stdin

class TreeNode:

    def __init__(self, id, children = None) -> None:
        self.id = id
        self.children = children or []

    def add_child(self, child):
        self.children.append(child)

# calculate size of each subtree
def subordinates(root, n):
    size = [0 for _ in range(n + 1)]
    def dfs(node):
        size[node.id] = 0
        if node.children:
            size[node.id] += sum([dfs(child) for child in node.children])
        return size[node.id] + 1

    _ = dfs(root)
    print(' '.join(map(str, size[1:])))

def read_num():
    return int(stdin.readline())

def read_nums():
    return [int(num) for num in stdin.readline().split()]

if __name__ == '__main__':
    nodes = [None]
    n = read_num()
    for i in range(n):
        nodes.append(TreeNode(i + 1))

    for i, boss in enumerate(read_nums()):
        nodes[boss].add_child(nodes[i + 2])

    subordinates(nodes[1], n)

    

