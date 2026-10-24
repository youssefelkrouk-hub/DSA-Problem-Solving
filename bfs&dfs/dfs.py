# dfs stands for depth-first-search , and those are the step to implement it using a stack
# why stack beacause it support the LIFO operation :LAST-IN-FIRST-OUT
#DFS must go deep first. The most recently discovered node is the one you explore next, which is exactly what a stack (LIFO) does. 
# When you hit a dead end,popping returns you to the most recent node that still has unexplored neighbors.
# That is backtracking.

def dfs(graph, start):
    visited = set()
    stack = [start]              # stack: Last In, First Out

    while stack:
        node = stack.pop()       # take the LAST node added
        if node not in visited:
            visited.add(node)
            print(node, end=' ')
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)


# Push the start node onto a stack.
# Pop the top node. If it was not visited, mark it visited.
# Push its unvisited neighbors onto the stack.
# Repeat until the stack is empty.

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

dfs(graph,'A')