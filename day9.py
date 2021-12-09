import numpy as np
from tqdm import tqdm


def day9_load(fname):
    with open(fname) as f:        
        ll = f.readlines()
    return np.array([ [ int(c) for c in l.strip() ] for l in ll ], dtype=np.int8)


def adj_finder_with_diagonal(m, l, c):
    adj = []
    
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            rangeX = range(0, m.shape[0])  # X bounds
            rangeY = range(0, m.shape[1])  # Y bounds
            
            (newX, newY) = (l+dx, c+dy)  # adjacent cell
            
            if (newX in rangeX) and (newY in rangeY) and (dx, dy) != (0, 0):
                adj.append((newX, newY))
    
    return adj


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


def day9_local_min(m, l, c):
    v = m[l, c]
    for a in adj_finder(m, l, c):
        if m[a] <= v:
            return False
    return True


def part1(m):    
    max_lig, max_col = m.shape
    local_mins = []
    for l in range(max_lig):
        for c in range(max_col):
            if day9_local_min(m, l, c) is True:
                local_mins.append((l,c)) 
    #ret = 0
    #for lm in local_mins:
    #    ret += 1 + m[lm]
    ret = sum(map(lambda lm: 1+m[lm], local_mins))
    return ret, local_mins


def bassin_finder(m, l, b):
    dummy = adj_finder(m, l[0], l[1])
    #filtered = list(filter(lambda c: m[c] != 9 and c not in b, dummy))
    others = [l]
    for f in filter(lambda c: m[c] != 9 and c not in b, dummy):
        others += bassin_finder(m, f, b+others)
    return list(set(others))


def part2(m, lm):
    bassins = [bassin_finder(m, l, [l]) for l in tqdm(lm)]
    #for l in tqdm(lm):
    #    bassins.append(bassin_finder(m, l, [l]))        
        
    bs = sorted(bassins, key=len)
    return len(bs[-1]) * len(bs[-2]) * len(bs[-3])


if __name__ == "__main__":
    fname = "day9-bs.txt";
    M = day9_load(fname)
    ret, LM = part1(M)
    print("Part 1 {:s} {:d} (15)".format(fname, ret))
    ret = part2(M, LM)
    print("Part 2 {:s} {:d} (1134)".format(fname, ret))
    fname = "day9-s.txt";
    M = day9_load(fname)
    ret, LM = part1(M)
    print("Part 1 {:s} {:d} (506)".format(fname, ret))
    ret = part2(M, LM)
    print("Part 2 {:s} {:d} (931200)".format(fname, ret))