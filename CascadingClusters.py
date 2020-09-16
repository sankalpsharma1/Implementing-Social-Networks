import networkx as nx
import matplotlib.pyplot as plt


def set_all_B(G):
    for i in G.nodes():
        G.nodes[i]['action'] = 'B'
    return G


def set_A(G, list1):
    for i in list1:
        G.nodes[i]['action'] = 'A'
    return G


def get_colors(G):
    color = []
    for i in G.nodes():
        if (G.nodes[i]['action'] == 'B'):
            color.append('red')
        else:
            color.append('green')
    return color


def recalculate(G):
    dict1 = {}
    a = 3
    b = 2
    for i in G.nodes():
        neigh = G.neighbors(i)
        count_A = 0
        count_B = 0

        for j in neigh:
            if (G.nodes[j]['action'] == 'A'):
                count_A += 1
            else:
                count_B += 1
        payoff_A = a * count_A
        payoff_B = b * count_B

        if (payoff_A >= payoff_B):
            dict1[i] = 'A'
        else:
            dict1[i] = 'B'
    return dict1


def reset_node_attributes(G, action_dict):
    for i in action_dict:
        G.nodes[i]['action'] = action_dict[i]
    return G


def Calculate(G):
    terminate = True
    count = 0
    c = 0
    while (terminate and count < 100):
        count += 1
        action_dict = recalculate(G)  # action_dict will hold a dictionary
        G = reset_node_attributes(G, action_dict)
        colors = get_colors(G)

        if (colors.count('red') == len(colors) or colors.count('green') == len(colors)):
            terminate = False
            if (colors.count('green') == len(colors)):
                c = 1

    if (c == 1):
        print('cascade complete')
    else:
        print('cascade incomplete')
    nx.draw(G, with_labels=1, node_color=colors, node_size=800)
    plt.show()


G = nx.Graph()
G.add_nodes_from(range(13))
G.add_edges_from(
    [(0, 1), (0, 6), (1, 2), (1, 8), (1, 12), (2, 9), (2, 12), (3, 4), (3, 9), (3, 12), (4, 5), (4, 12), (5, 6),
     (5, 10), (6, 8), (7, 8), (7, 9), (7, 10), (7, 11), (8, 9), (8, 10), (8, 11), (9, 10), (9, 11), (10, 11)])

list2 = [[0, 1, 2, 3], [0, 2, 3, 4], [1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 12], [2, 3, 4, 12],
         [0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5, 6, 12]]

for list1 in list2:
    print(list1)
    G = set_all_B(G)

    G = set_A(G, list1)
    colors = get_colors(G)
    nx.draw(G, with_labels=1, node_color=colors, node_size=800)
    plt.show()

    Calculate(G)