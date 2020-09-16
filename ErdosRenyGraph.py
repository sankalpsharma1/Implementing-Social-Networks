import networkx as nx
import matplotlib.pyplot as plt
import random

#Distribution graph for Erdos_Renyi model.

def distribution_graph(g):
    print(nx.degree(g))
    all_node_degree = list(dict((nx.degree(g))).values())

    unique_degree = list(set(all_node_degree))
    unique_degree.sort()
    nodes_with_degree = []
    for i in unique_degree:
        nodes_with_degree.append(all_node_degree.count(i))

    plt.plot(unique_degree, nodes_with_degree)
    plt.xlabel("Degrees")
    plt.ylabel("No. of nodes")
    plt.title("Degree distribution")
    plt.show()
# 1. Take N number of nodes from user.

print("Enter number of nodes")
N = int(input())

# 2. Take P probability value for edges.

print("Enter value of probability of every node")
P = float(input())

# 3. Create a empty graph.
g = nx.Graph()

# 4. Add nodes to it.

g.add_nodes_from(range(1, N + 1))

# 5. Add edges to the graph randomly.

for i in g.nodes():
    for j in g.nodes():
        if (i < j):
            # 6. Take random number R.
            R = random.random()
            # 7. Check if R<P add the edge to the graph else ignore.
            if (R < P):
                g.add_edge(i, j)
    pos=nx.circular_layout(g)
    nx.draw(g,pos,with_labels=1)
    plt.show()
distribution_graph(g)