import networkx as nx
import matplotlib.pyplot as plt
from task_01 import G, characters
from dfs_paths import dfs_paths
from bfs_paths import bfs_paths

# Finding paths using DFS and BFS
start_node = characters[characters.index("Chewbacca")]
end_node = characters[characters.index("R2D2")]

dfs_paths_result = dfs_paths(G, start_node, end_node)
bfs_paths_result = bfs_paths(G, start_node, end_node)

# Displaying the results
print("Paths using DFS:")
for path in dfs_paths_result:
    print(" -> ".join(path))

print("\nPaths using BFS:")
for path in bfs_paths_result:
    print(" -> ".join(path))
