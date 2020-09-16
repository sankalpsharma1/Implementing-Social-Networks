import networkx as nx
import random
import numpy as np


def add_edges(G, p):
    for i in G.nodes():
        for j in G.nodes():
            if (i != j):
                r = random.random()
                if (r < p):
                    G.add_edge(i, j)
                else:
                    continue
    return G


def assign(G):
    points = [200 for i in range(G.number_of_nodes())]
    return points


def distribute_points(G, points):
    previous = points
    new = [0 for i in range(len(points))]

    for i in G.nodes():
        neigh = G.out_edges(i)
        # print(i,neigh)
        if (len(neigh) == 0):
            new[i] += previous[i]
        else:
            share = previous[i] / len(neigh)
            for each in neigh:
                new[each[1]] += share

    return G, new


def manage_sink(G, points):
    add = 200 * 0.2
    for i in range(len(points)):
        points[i] *= 0.8
        points[i] += add
    return points


def convergence(G, points):
    while (1):
        G, new = distribute_points(G, points)
        new = manage_sink(G, new)
        new1 = list(np.multiply(new, 10000).astype(int))
        points1 = list(np.multiply(points, 10000).astype(int))
        if (new1 == points1):
            break
        else:
            points = new
        # print(new1)
    return G, points


def nodes_sorted(G, points):
    temp = np.array(points)
    temp = np.argsort(-temp)
    return temp

#Main
# 1. Create a directed graph with N nodes
g = nx.DiGraph()
N = 10
g.add_nodes_from(range(N))

#2. Add edges to graph
g = add_edges(g, 0.4)

# 3. assign 200 points to each node
p = assign(g)
print(p)
# 4. keep distributing points till it reaches converges
g, points = convergence(g, p)
print(points)

# 5. Page Ranking according to their points distribution method
sorted_values = nodes_sorted(g, p)
print(sorted_values)

#6. Inbuilt PageRank Method in NetworkX module
p_dict = nx.pagerank(g)

# p_dict is dictonary of tuples
p_sort = sorted(p_dict.items(), key=lambda x: x[1], reverse=True)
for i in p_sort:
    print(i[0], end=",")


