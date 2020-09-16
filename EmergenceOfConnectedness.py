import networkx as nx
import matplotlib.pyplot as plt
import random
# Add N number of nodes in graph g and return the graph


def add_nodes(N):
    g = nx.Graph()
    g.add_nodes_from(range(N))
    return g

# Add 1 random edge


def add_random_edge(g):
    z1 = random.choice(g.nodes())
    z2 = random.choice(g.nodes())
    if z1 != z2:
        g.add_edge(z1, z2)
    return g

# Continue adding edges in graph g till it becomes connected


def continue_add_connectivity(g):
    while(nx.is_connected(G) == False):
        g = add_random_edge(g)
    return g

# Creates an object of entire process.Input- number of nodes and Output- number of edges required for graph connectivity.


def create_instance(N):
    g = add_nodes(n)
    g = continue_add_connectivity(g)
    return g.number_of_edges()

# Average it over 100 times


def create_average_instance(N):
    l = []
    for i in range(0, 100):
        l.append(create_instance(N))
    return numpy.average(l)

# Plot the graph for different number of edges


def plot_connectivity():
    a = []
    b = []
    j = 10  # j is the number of nodes
    while (j <= 1000):
        a.append(j)
        b.append(create_average_instance(j))
        i += 10
    plt.xlabel('Number of nodes')
    plt.ylabel('Number of edges required')
    plt.title('Emergence of connectivity')
    plt.plot(a, b)
    plt.show()

    a1 = []
    b1 = []
    j = 10
    while (j <= 400):
        a1.append(j)
        b1.append(j*float(numpy.log(j)/2))
        j += 10
    plt.plot(a1, b1)
    plt.show()


# main
plot_connectivity()