import networkx as nx
import matplotlib.pyplot as plt
from task_01 import G  # Importing the graph from task_01.py


# Implementation of the DFS algorithm to find paths
def dfs_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            new_paths = dfs_paths(graph, node, end, path)
            for new_path in new_paths:
                paths.append(new_path)
    return paths


# Implementation of the BFS algorithm to find paths
def bfs_paths(graph, start, end):
    queue = [(start, [start])]
    paths = []
    while queue:
        (vertex, path) = queue.pop(0)
        for next_node in graph[vertex]:
            if next_node not in path:
                if next_node == end:
                    paths.append(path + [next_node])
                else:
                    queue.append((next_node, path + [next_node]))
    return paths


# Finding paths using DFS and BFS
start_node = "Luke"
end_node = "DarthVader"

dfs_paths_result = dfs_paths(G, start_node, end_node)
bfs_paths_result = bfs_paths(G, start_node, end_node)

# Displaying the results
print("Paths using DFS:")
for path in dfs_paths_result:
    print(" -> ".join(path))

print("\nPaths using BFS:")
for path in bfs_paths_result:
    print(" -> ".join(path))
