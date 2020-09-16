import networkx as nx
import itertools


def communities_using_brute(gfg):
    nodes = gfg.nodes()
    n = gfg.number_of_nodes()
    first_community = []
    for i in range(1, n / 2 + 1):
        c = [list(a) for a in itertools.combiantions(nodes, i)]
        first_community.extend(c)

    second_community = []

    for i in range(len(first_community)):
        b = list(set(nodes) - set(first_community[i]))
        second_community.append(b)

    # Which division is best...
    intra_edges1 = []
    intra_edges2 = []
    inter_edges = []
    ratio = []  # ratio of number of intra/number of inter community edges

    for i in range(len(first_community)):
        intra_edges1.append(gfg.subgraph(first_community[i]).number_of_edges())

    for i in range(len(second_community)):
        intra_edges2.append(gfg.subgraph(second_community[i]).number_of_edges())

    e = g.number_of_edges()

    for i in range(len(first_community)):
        inter_edges.append(e - intra_edges1[i] - intra_edges2[i])

    # Calculate the Ratio

    for i in range(len(first_community)):
        ratio.append((float)intra_edges1[i] + intra_edges2[i])/inter_edges[i])
        maxV = max(ratio)
        mindex = ratio.index(maxV)

        print
        '[ ', first_community[mindex], ' ] , [ ', second_community[mindex], ' ]'

        # Example graph
        gfg = nx.barbell_graph(5, 0)
        communities_using_brute(gfg)