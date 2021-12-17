import numpy as np
from numpy.core.fromnumeric import shape
from numpy.lib.function_base import i0
from tqdm import tqdm

def day15_load(fname):
    with open(fname) as f:        
        ll = f.readlines()
    return np.array([ [ int(c) for c in l.strip() ] for l in ll ], dtype=np.int8)


def adj_finder(m, l, c):
    adj = []
    if l > 0:
        adj.append((l-1,c))
    if l+1 < m.shape[0]:
        adj.append((l+1,c))
    if c > 0:
        adj.append((l,c-1))
    if c+1 < m.shape[1]:
        adj.append((l,c+1))
    return adj



def part1(m):
    costs = [ 0 for _ in range(m.shape[0])]
    for i in range(m.shape[0]):
        costs[i] = np.sum(M, axis=0)[i]
        for j in range(i):
            costs[i] += m[0, j]
        for j in range(i, m.shape[1]):
            costs[i] += m[0, j]
    GLOBAL_MIN = min(costs)
    for i in range(m.shape[1]):
        costs[i] = np.sum(M, axis=1)[i]
        for j in range(i):
            costs[i] += m[j, 0]
        for j in range(i, m.shape[0]):
            costs[i] += m[j, 0]
    GLOBAL_MIN = min(GLOBAL_MIN, min(costs))
    start=(0,0)
    end = (m.shape[0]-1, m.shape[1]-1)
    results = {}
    next = [ [start] ]
    costs = [ 0 ]
    while len(next) != 0:
        new = []
        costs_new = []
        for i in range(len(next)):
            cost = costs[i]
            if cost < GLOBAL_MIN:
                path = next[i]
                if path[-1] == end:
                    results[cost] = path
                    if cost < GLOBAL_MIN:
                        print("Part 1 {:d} -> {:d}".format(GLOBAL_MIN, cost))
                        GLOBAL_MIN = cost
                else:
                    for a in adj_finder(m, path[-1][0], path[-1][1]):
                        if a not in path:
                            new.append(path + [a])
                            costs_new.append(cost + m[path[-1]])
        next = new
        costs = costs_new
        print("       len: {:d} GLOBAL_MIN: {:d}".format(len(next), GLOBAL_MIN))
    return GLOBAL_MIN


def part2(m):
    ret = 0
    return ret


if __name__ == "__main__":
    fname = "day15-bs.txt";
    M = day15_load(fname)
    ret = part1(M)
    print("Part 1 {:s} {:d} (40)".format(fname, ret))
    fname = "day15-s.txt";
    M = day15_load(fname)
    ret = part1(M)
    print("Part 1 {:s} {:d} (?)".format(fname, ret))
