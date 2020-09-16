# cascade pay off
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
            color.append('blue')
    return color


def recalculate(G):
    dict1 = {}
    # payoff(A)=a=4
    # payoff(B)=b=3
    a = 15
    b = 5
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
    while (terminate and count < 10):
        count += 1
        action_dict = recalculate(G)  # action_dict will hold a dictionary
        G = reset_node_attributes(G, action_dict)
        colors = get_colors(G)

        if (colors.count('red') == len(colors) or colors.count('green') == len(colors)):
            terminate = False
            if (colors.count('green') == len(colors)):
                c = 1
        nx.draw(G, with_labels=1, node_color=colors, node_size=800)
        plt.show()
    if (c == 1):
        print('cascade complete')
    else:
        print('cascade incomplete')

G=nx.erdos_renyi_graph(10,0.5)
nx.write_gml(G,"erdos_graph.gml")
G = nx.read_gml('erdos_graph.gml')
print(G.nodes())
G = set_all_B(G)
list1 = ['2', '1','3']  # initial adopters
G = set_A(G, list1)
colors = get_colors(G)
nx.draw(G, with_labels=1, node_color=colors, node_size=800)
plt.show()

Calculate(G)