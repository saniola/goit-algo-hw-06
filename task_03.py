import networkx as nx
from task_01 import G, characters

# Implementing Dijkstra's algorithm to find the shortest path between all nodes
shortest_paths = dict(nx.all_pairs_dijkstra_path(G, weight="weight"))

# Print shortest paths between all pairs of nodes

start_node = characters[characters.index("Chewbacca")]
end_node = characters[characters.index("R2D2")]

path = shortest_paths[start_node][end_node]
path_length = sum(G[path[i]][path[i + 1]]["weight"] for i in range(len(path) - 1))
print(f"Shortest path from {start_node} to {end_node}: {path}")
print(f"Shortest path length: {path_length}\n")
