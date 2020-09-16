import networkx as nx
import matplotlib.pyplot as plt


def check(h, d):
    f = 0  # there is no node of deg<=d
    for i in h.nodes():
        if (h.degree(i) <= d):
            f = 1
            break
    return f


def find_nodes(h, it):
    set1 = []
    for i in h.nodes():
        if (h.degree(i) <= it):
            set1.append(i)
    return set1


g = nx.Graph()
g.add_edges_from(
    [(1, 2), (1, 9), (3, 13), (4, 6), (5, 6), (5, 7), (5, 8), (5, 9), (5, 10),(5,11),(5,12), (10, 12), (10, 13), (11, 14), (12, 14),
     (12, 15), (13, 14), (13, 15), (13, 17), (14, 15), (15, 16)])

h = g.copy()
it = 1
# Bucket being filled currently
tmp = []
# list of lists of buckets
buckets = []
while (1):
    flag = check(h, it)
    if (flag == 0):
        it += 1
        buckets.append(tmp)
        tmp = []
    if (flag == 1):
        node_set = find_nodes(h, it)
        for each in node_set:
            h.remove_node(each)
            tmp.append(each)
    if (h.number_of_nodes() == 0):
        buckets.append(tmp)
        break
print(buckets)

nx.draw(g, with_labels=1)
plt.show()