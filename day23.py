import math
from collections import defaultdict
import string
from sortedcontainers import SortedKeyList, SortedSet
from tqdm import tqdm
import networkx as nx
import matplotlib.pyplot as plt

def day23_load() -> nx.Graph:
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

def day23_load2() -> nx.Graph:
    G = nx.Graph()
    G.add_nodes_from(range(23))
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
                        (13, 14, {'weight': 1}),
                        (15, 3, {'weight': 1}),
                        (16, 15, {'weight': 1}),
                        (17, 6, {'weight': 1}),
                        (18, 17, {'weight': 1}),
                        (19, 9, {'weight': 1}),
                        (19, 20, {'weight': 1}),
                        (21, 12, {'weight': 1}),
                        (21, 22, {'weight': 1})
                        ] )
    return G


def day23_show1(G, widths) -> None:
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

def day23_end(state) -> bool:
    finals = {  0: [2, 3, 15, 16],
                1: [5, 6, 17, 18],
                2: [8, 9, 19, 20],
                3: [11, 12, 21, 22] }
    pop = len(state) // 4
    return all([ v in finals[i//pop] for i, v in enumerate(state) ] )


def amphy_type(i, pop=2) -> string:
    amphy = ('A', 'B', 'C', 'D')
    return amphy[i//pop]


def day23_privacy(i, root, a) -> bool:    
    doors = [ 2, 5, 8, 11 ]
    hallway = [ 0, 1, 4, 7, 10, 13, 14 ]
    locks = {   0: 2, 1: 2,
                2: 5, 3: 5,
                4: 8, 5: 8,
                6: 11, 7: 11
    }
    rooms = {   0: [3], 1: [3],
                2: [6], 3: [6],
                4: [9], 5: [9],
                6: [12], 7: [12]
    }
    ret = None
    if root[i] in hallway:
        if a in doors:
            if a == locks[i]:
                colocs = [ k for k in range(len(root)) if root[k] in rooms[i] and k != i ]
                ret = len(colocs) == 0 or all([ amphy_type(i) == amphy_type(coloc) for coloc in colocs ])
            else:
                ret = False
        else:       # Stay in Hallway
            ret = True
    elif root[i] in doors:
        ret = True
    else:           # in rooms
        ret = True
    return ret


def day23_privacy2(i, root, a) -> bool:    
    doors = [ 2, 5, 8, 11 ]
    hallway = [ 0, 1, 4, 7, 10, 13, 14 ]
    locks = {   0: 2, 1: 5,
                2: 8, 3: 11
    }
    rooms = {   0: [3, 15, 16], 
                1: [6, 17, 18], 
                2: [9, 19, 20], 
                3: [12, 21, 22]
    }
    ret = None
    if root[i] in hallway:
        if a in doors:
            if a == locks[i//4]:
                colocs = [ k for k in range(len(root)) if root[k] in rooms[i//4] and k != i ]
                ret = len(colocs) == 0 or all([ amphy_type(i, pop=4) == amphy_type(coloc, pop=4) for coloc in colocs ])
            else:
                ret = False
        else:       # Stay in Hallway
            ret = True
    elif root[i] in doors:
        ret = True
    else:           # in rooms
        ret = True
    return ret


def day23_part1_sub(G, costs, root) -> list:
    ret = []
    for i in range(len(root[0])):
        s = root[0][i]
        avail = [ n for n in list(G.adj[s]) if n not in root[0] and day23_privacy(i, root[0], n) ]
        for a in avail:
            new_cost = root[1] + G.edges[s, a]['weight'] * costs[i]
            new_state = [ a if k==i else root[0][k] for k in range(len(root[0])) ]
            ret.append((tuple(new_state), new_cost))
    return ret


def day23_part1(G, state, costs) -> list:
    start = tuple(state)

    gscore = defaultdict(lambda : math.inf)
    gscore[start] = 0

    fscore = defaultdict(lambda : math.inf)
    fscore[start] = 0

    openSet = SortedSet(key=lambda x:fscore[x])
    openSet.add( start )
    
    #cameFrom = {}
    results = []

    with tqdm() as bar:
        while len(openSet) > 0:
            bar.update(1)
            current = openSet.pop(0)
            
            if day23_end(current):
                results.append((current, fscore[current]))

            neighbors = []
            d = {}
            for i, s in enumerate(current):
                avail = [ n for n in list(G.adj[s]) if n not in current and day23_privacy(i, current, n) ]
                for a in avail:
                    neighbor = tuple([ a if k==i else currentk for k, currentk in enumerate(current) ])
                    neighbors.append(neighbor)
                    d[neighbor] = G.edges[s, a]['weight'] * costs[i]

            for neighbor in neighbors:
                tentative_gScore = gscore[current] + d[neighbor]
                if tentative_gScore < gscore[neighbor]:
                    # This path to neighbor is better than any previous one. Record it!
                    # cameFrom[neighbor] = current
                    gscore[neighbor] = tentative_gScore
                    fscore[neighbor] = tentative_gScore # + h(neighbor, costs)
                    openSet.add(neighbor)
            bar.total = len(openSet) + len(gscore)
    return results


def day23_part2(G, state, costs):
    start = tuple(state)

    gscore = defaultdict(lambda : math.inf)
    gscore[start] = 0

    fscore = defaultdict(lambda : math.inf)
    fscore[start] = 0

    openSet = SortedSet(key=lambda x:fscore[x])
    openSet.add( start )
    results = []

    with tqdm() as bar:
        while len(openSet) > 0:
            bar.update(1)
            current = openSet.pop(0)
            
            if day23_end(current):
                results.append((current, fscore[current]))

            neighbors = []
            d = {}
            for i, s in enumerate(current):
                avail = [ n for n in list(G.adj[s]) if n not in current and day23_privacy2(i, current, n) ]
                for a in avail:
                    new_state = [ a if k==i else current[k] for k in range(len(current)) ]
                    neighbor = tuple(new_state)
                    neighbors.append(neighbor)
                    d[neighbor] = G.edges[s, a]['weight'] * costs[i]


            for neighbor in neighbors:
                tentative_gScore = gscore[current] + d[neighbor]
                if tentative_gScore < gscore[neighbor]:
                    # This path to neighbor is better than any previous one. Record it!                    
                    gscore[neighbor] = tentative_gScore
                    fscore[neighbor] = tentative_gScore # + h(neighbor, costs)
                    openSet.add(neighbor)
            bar.total = len(openSet) + len(gscore)
    return results

def h(neighbor, costs):
    ret = 0
    target = [ 0, 0, 1, 1, 2, 2, 3, 3]
    heuristic = [   [3, 5, 7, 9],
                    [2, 4, 6, 8],
                    [0, 4, 6, 8],
                    [0, 5, 6, 9],
                    [2, 2, 4, 6],
                    [4, 0, 4, 6],
                    [5, 0, 5, 7],
                    [5, 3, 3, 5],
                    [6, 4, 0, 4],
                    [7, 5, 0, 5],
                    [6, 4, 2, 2],
                    [8, 6, 4, 0],
                    [9, 7, 5, 0],
                    [8, 6, 4, 2],                    
                    [9, 7, 5, 3] ]
    #for i in range(len(neighbor)):
    #    ret += heuristic[neighbor[i]][target[i]] * costs[i]
    return sum( [ heuristic[n][target[i]] * costs[i] for i,n in enumerate(neighbor) ] )


def day23_result(s, empty=-1):
    return empty if len(s)==0 else min([n[1] for n in s])


if __name__ == "__main__":

    G = day23_load()
    #s = day23_part1(G, [ 3, 12, 2, 8, 5, 9, 6, 11 ], [ 1, 1, 10, 10, 100, 100, 1000, 1000 ])
    #ret = day23_result(s)
    #print("Part 1  {:d} (12521)".format(ret))
    #s = day23_part1(G, [ 2, 11, 8, 9, 5, 12, 3, 6 ], [ 1, 1, 10, 10, 100, 100, 1000, 1000 ])
    #ret = day23_result(s)
    #print("Part 1  {:d} (18195)".format(ret))



    G = day23_load2()
    s = day23_part2(G, [ 16, 12, 22, 19, 2, 17, 8, 9, 5, 6, 20, 21, 3, 15, 18, 11 ], [ 1, 1, 1, 1, 10, 10, 10, 10, 100, 100, 100, 100, 1000, 1000, 1000, 1000 ])
    ret = day23_result(s)
    print("Part 2  {:d} (44169)".format(ret))

#############
#...........#
###A#C#B#A###
  #D#C#B#A#
  #D#B#A#C#
  #D#D#B#C#
  #########    
    s = day23_part2(G, [ 2,19,11,12, 17,8,9,20, 5,6,21,22, 3,15,16,18 ], [ 1, 1, 1, 1, 10, 10, 10, 10, 100, 100, 100, 100, 1000, 1000, 1000, 1000 ])
    ret = day23_result(s)
    print("Part 2  {:d} (??????)".format(ret))



    G = day23_load()
    s = day23_part1(G, [ 3, 12, 2, 8, 5, 9, 6, 11 ], [ 1, 1, 10, 10, 100, 100, 1000, 1000 ])
    ret = day23_result(s)
    print("Part 1  {:d} (12521)".format(ret))
    s = day23_part1(G, [ 2, 11, 8, 9, 5, 12, 3, 6 ], [ 1, 1, 10, 10, 100, 100, 1000, 1000 ])
    ret = day23_result(s)
    print("Part 1  {:d} (18195)".format(ret))

    