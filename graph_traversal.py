from collections import deque

def bfs(graph, start, target):
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == target:
            return path

        if node not in visited:
            visited.add(node)

            for neighbor in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return []
    
    def dfs(graph, start):
    visited = set()

    def explore(node):
        if node in visited:
            return
        visited.add(node)

        for neighbor in graph.get(node, []):
            explore(neighbor)

    explore(start)
    return visited
