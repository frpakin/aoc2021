import math
from tqdm import tqdm
from sortedcontainers import SortedDict
import networkx as nx
import matplotlib.pyplot as plt

def day23_load():
    G = nx.Graph()
    G.add_nodes_from(range(15))
    G.add_edges_from( [ (0, 1, {'weight': 1}), 
                        (1, 2, {'weight': 2}),
                        (1, 4, {'weight': 2}),
                        (2, 3, {'weight': 1}),
                        (2, 4, {'weight': 2}),
                        (4, 5, {'weight': 2}),
                        (4, 7, {'weight': 2}),
                        (5, 6, {'weight': 1}),
                        (5, 7, {'weight': 2}),
                        (7, 8, {'weight': 2}),
                        (7, 10, {'weight': 2}),
                        (8, 9, {'weight': 1}),
                        (8, 10, {'weight': 2}),
                        (10, 11, {'weight': 2}),
                        (10, 13, {'weight': 2}),
                        (11, 13, {'weight': 2}),
                        (11, 12, {'weight': 1}),
                        (13, 14, {'weight': 1}) ] )
    return G


def day23_show1(G, widths):
    esizes = []
    for w in widths:
        esizes.append([(u, v) for (u, v, d) in G.edges(data=True) if w[0] <= d["weight"] < w[1]])
    
    ax = plt.subplots()
    # nodes
    pos = nx.spring_layout(G, seed=7)
    nx.draw_networkx_nodes(G, pos, node_size=700)
    # edges
    for i in range(len(widths)):
        w = widths[i]
        nx.draw_networkx_edges(G, pos, edgelist=esizes[i], width=w[2], edge_color=w[3], style=w[4])
    # labels
    nx.draw_networkx_labels(G, pos, font_size=8, font_family="sans-serif")

    ax = plt.gca()
    ax.margins(0.08)
    plt.axis("off")
    plt.tight_layout()
    plt.show()


def day23_end(state):
    return state[0] in [2, 3] and state[1] in [2, 3] and state[2] in [5, 6] and state[3] in [5, 6] and state[4] in [8, 9] and state[5] in [8, 9] and state[6] in [11, 12] and state[7] in [11, 12]


def day23_part1_sub(G, costs, rootcost):
    ret = []
    root = rootcost[0]
    for i in range(len(root)):
        s = root[i]
        avail = [ n for n in list(G.adj[s]) if n not in root ]
        for a in avail:
            new_cost = rootcost[1] + G.edges[s, a]['weight'] * costs[i]
            new_state = list(root)
            new_state[i] = a
            new_root = tuple(new_state)
            ret.append((new_root, new_cost))
    return ret


def day23_part1(G, state, costs, limit_iter = 1000000):
    bar = tqdm(total=limit_iter)
    todo = [ (tuple(state), 0) ]
    done = {}
    success = []
    while len(todo)>0 and bar.n<limit_iter:
        bar.update(1)
        root = todo.pop(0)
        done[root[0]] = min(root[1], done.get(root[0], math.inf))
        if day23_end(root[0]):
            success.append(root)
        else:
            for n in day23_part1_sub(G, costs, root):
                if not n[0] in done:
                    todo.append(n)
    return success


def day23_result(s):
    ret = -1 if len(s)>0 else math.inf
    for n in s:
        ret = min(ret, n[1])
    return ret


if __name__ == "__main__":
    G = day23_load()
    s = day23_part1(G, [ 2, 3, 5, 6, 8, 9, 11, 12 ], [ 1, 1, 10, 10, 100, 100, 1000, 1000 ])
    ret = day23_result(s)
    print("Part 1  {:d} (0)".format(ret))
    s = day23_part1(G, [ 3, 12, 2, 8, 5, 9, 6, 11 ], [ 1, 1, 10, 10, 100, 100, 1000, 1000 ])
    ret = day23_result(s)
    print("Part 1  {:d} (12521)".format(ret))
    s = day23_part1(G, [ 2, 11, 8, 9, 5, 12, 3, 6 ], [ 1, 1, 10, 10, 100, 100, 1000, 1000 ])
    ret = day23_result(s)
    print("Part 1  {:d} (???)".format(ret))