import networkx as nx
import matplotlib.pyplot as plt

# Creating a graph
G = nx.Graph()

# Adding initial nodes and edges
G.add_node("Luke")
G.add_node("Leia")
G.add_node("Han")
G.add_node("Chewbacca")
G.add_edge("Luke", "Leia", weight=5)
G.add_edge("Luke", "Han", weight=3)
G.add_edge("Leia", "Chewbacca", weight=2)
G.add_edge("Han", "Chewbacca", weight=4)

# Adding 10 new users
new_users = [
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

for user in new_users:
    G.add_node(user)

# Adding random connections between new users and existing ones
import random

for user1 in new_users:
    for user2 in G.nodes():
        if user1 != user2 and not G.has_edge(user1, user2):
            weight = random.randint(1, 10)  # Random weight for the connection
            G.add_edge(user1, user2, weight=weight)

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
print("List of edges:", list(G.edges()))
print("Node degrees:", dict(G.degree()))
