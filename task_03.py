from dijkstra import dijkstra
from task_01 import G, characters


start_node = characters[characters.index("Chewbacca")]
end_node = characters[characters.index("R2D2")]

distances = dijkstra(G, start_node)
path = [end_node]
current_node = end_node
while current_node != start_node:
    current_node = min(
        G[current_node],
        key=lambda neighbor: distances[neighbor] + G[current_node][neighbor]["weight"],
    )
    path.append(current_node)
path = path[::-1]

path_length = distances[end_node]

print(f"Shortest path from {start_node} to {end_node}: {path}")
print(f"Shortest path length: {path_length}\n")
