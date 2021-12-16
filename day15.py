import numpy as np
from tqdm import tqdm

def day15_load(fname):
    with open(fname) as f:        
        ll = f.readlines()
    return np.array([ [ int(c) for c in l.strip() ] for l in ll ], dtype=np.int8)


def part1(m):
    results = []
    GLOBAL_MIN = 2**20
    def part1_sub(m, start, end, path, cost):
        global GLOBAL_MIN
        if start == end:
            results.append(cost, path)
            if cost < GLOBAL_MIN:
                GLOBAL_MIN = cost
            return m[end]
        else:
            for p in adj and not in path:
                if m[p] + cost < GLOBAL_MIN:
                    part1_sub(m, start, end, path, cost)
        return p

    path = part1_sub(m, (0,0), m.shape, [], 0)
    ret = 0
    return ret


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
