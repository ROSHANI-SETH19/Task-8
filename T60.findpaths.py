def find_all_paths(graph, start, end):
    def dfs(current_node, path):
        if current_node == end:
            paths.append(path)
        else:
            for neighbor in graph[current_node]:
                if neighbor not in path:
                    dfs(neighbor, path + [neighbor])

    paths = []
    dfs(start, [start])
    return paths

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

start_node = 'A'
end_node = 'F'

all_paths = find_all_paths(graph, start_node, end_node)
print("All paths from", start_node, "to", end_node, "are:")
for i, path in enumerate(all_paths):
    print("Path", i+1, ":", ' -> '.join(path))
