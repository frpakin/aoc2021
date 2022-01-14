import networkx as nx
import matplotlib.pyplot as plt

def day23_load():
    G = nx.Graph()
    G.add_nodes_from(range(15))
    G.add_edges_from( [ (0, 1, {'weight': 1}), 
                        (1, 2, {'weight': 2}),
                        (1, 4, {'weight': 2}),
                        (2, 3, {'weight': 1}),
                        (4, 5, {'weight': 2}),
                        (4, 7, {'weight': 2}),
                        (5, 6, {'weight': 1}),
                        (7, 8, {'weight': 2}),
                        (7, 10, {'weight': 2}),
                        (8, 9, {'weight': 1}),
                        (10, 11, {'weight': 2}),
                        (10, 13, {'weight': 2}),
                        (11, 12, {'weight': 1}),
                        (13, 14, {'weight': 1}) ] )


    return G


def day23_part1(G):
    subax1 = plt.subplot(121)
    nx.draw(G, with_labels=True, font_weight='bold')
    subax2 = plt.subplot(122)
    nx.draw_shell(G, with_labels=True, font_weight='bold')
    plt.show()
    return 0


if __name__ == "__main__":
    G = day23_load()
    ret = day23_part1(G)
    print("Part 1  {:d} (???)".format(ret))