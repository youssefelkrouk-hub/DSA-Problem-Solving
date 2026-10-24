from collections import deque

# Example graph (adjacency list)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}


# ---------- DFS (recursive) ----------
def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    print(node, end=' ')
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)
    return visited


# ---------- DFS (iterative, using a stack) ----------
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node, end=' ')
            # reversed() keeps the same visiting order as the recursive version
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)


# ---------- BFS (using a queue) ----------
def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


print("DFS recursive: ", end='')
dfs_recursive(graph, 'A')

print("\nDFS iterative: ", end='')
dfs_iterative(graph, 'A')

print("\nBFS:           ", end='')
bfs(graph, 'A')