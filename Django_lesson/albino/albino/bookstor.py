import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Add nodes
nodes = ["Customer", "Online Bookstore", "Payment Processor", "Supplier"]
G.add_nodes_from(nodes)

# Add edges with labels
edges = [
    ("Customer", "Online Bookstore", "Book Requests"),
    ("Customer", "Online Bookstore", "Order Placement"),
    ("Customer", "Online Bookstore", "Account Management"),
    ("Online Bookstore", "Customer", "Book Information"),
    ("Online Bookstore", "Customer", "Order Confirmation"),
    ("Online Bookstore", "Customer", "Account Details"),
    ("Online Bookstore", "Payment Processor", "Payment Details"),
    ("Payment Processor", "Online Bookstore", "Payment Confirmation"),
    ("Online Bookstore", "Supplier", "Inventory Orders"),
    ("Supplier", "Online Bookstore", "Inventory Updates"),
]

# Add edges to the graph
for edge in edges:
    G.add_edge(edge[0], edge[1], label=edge[2])

# Draw the graph
pos = nx.spring_layout(G, seed=42)
labels = nx.get_edge_attributes(G, "label")

plt.figure(figsize=(10, 8))
nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=3000,
    node_color="lightblue",
    font_size=10,
    font_weight="bold",
    arrows=True,
)
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Level 0 Data Flow Diagram for Online Bookstore")
plt.show()
