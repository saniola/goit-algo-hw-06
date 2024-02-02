import networkx as nx
import matplotlib.pyplot as plt
import random

# Creating a graph
G = nx.Graph()

# Adding characters
characters = [
    "Luke",
    "Leia",
    "Han",
    "Chewbacca",
    "DarthVader",
    "ObiWanKenobi",
    "Yoda",
    "R2D2",
]

for character in characters:
    G.add_node(character)

# Adding connections with different weights
edges_to_add = [
    ("Luke", "Leia", 4),
    ("Han", "Chewbacca", 6),
    ("Chewbacca", "Luke", 8),
    ("Leia", "DarthVader", 5),
    ("Han", "DarthVader", 7),
    ("Luke", "ObiWanKenobi", 3),
    ("ObiWanKenobi", "Yoda", 2),
    ("Yoda", "DarthVader", 9),
    ("DarthVader", "R2D2", 1),
    ("ObiWanKenobi", "Chewbacca", 5),
]

for edge in edges_to_add:
    G.add_edge(edge[0], edge[1], weight=edge[2])

# Visualizing the graph with custom positions for better layout
custom_pos = {
    "Luke": (0, 0),
    "Leia": (1, 1),
    "Han": (2, 0),
    "Chewbacca": (3, 1),
    "DarthVader": (4, 0),
    "ObiWanKenobi": (0, 2),
    "Yoda": (1, 3),
    "R2D2": (3, 3),
}

edge_labels = nx.get_edge_attributes(G, "weight")

nx.draw(G, custom_pos, with_labels=True, node_color="lightblue", font_weight="bold")
nx.draw_networkx_edge_labels(G, custom_pos, edge_labels=edge_labels)
plt.show()


# Analyzing basic characteristics
print("Number of nodes:", G.number_of_nodes())
print("Number of edges:", G.number_of_edges())
print("List of nodes:", list(G.nodes()))
print("Node degrees:", dict(G.degree()))
