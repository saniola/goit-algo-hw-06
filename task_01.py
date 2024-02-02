import networkx as nx
import matplotlib.pyplot as plt

# Creating a graph
G = nx.Graph()

# Adding characters
characters = [
    "Luke",
    "Leia",
    "Han",
    "Chewbacca",
    "DarthVader",
    "ObiWan",
    "Yoda",
    "R2D2",
    "C3PO",
    "Palpatine",
    "BobaFett",
    "Dooku",
    "MaceWindu",
    "Padme",
]

for character in characters:
    G.add_node(character)

# Adding random connections between new users and existing ones
import random

for character1 in characters:
    for character2 in G.nodes():
        if character1 != character2 and not G.has_edge(character1, character2):
            weight = random.randint(1, 10)  # Random weight for the connection
            G.add_edge(character1, character2, weight=weight)

# Visualizing the graph
pos = nx.spring_layout(G)
edge_labels = nx.get_edge_attributes(G, "weight")

nx.draw(G, pos, with_labels=True, node_color="lightblue", font_weight="bold")
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.show()

# Analyzing basic characteristics
print("Number of nodes:", G.number_of_nodes())
print("Number of edges:", G.number_of_edges())
print("List of nodes:", list(G.nodes()))
print("Node degrees:", dict(G.degree()))
