adj_matrix = [
    [0, 1, 1, 0, 0],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

def dfs_matrix(matrix, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            for neighbor in range(len(matrix[node]) - 1, -1, -1):
                if matrix[node][neighbor] == 1 and neighbor not in visited:
                    stack.append(neighbor)

print("DFS Traversal:")
dfs_matrix(adj_matrix, 0)
