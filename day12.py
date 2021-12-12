from tqdm import tqdm


def day12_load(fname):    
    nodes = {}
    vertex = []
    with open(fname) as f:        
        l = f.readline()
        while l != '':
            v = l.strip().split('-')
            vertex.append(v)
            for n in v: 
                if n not in nodes.keys():
                    nodes[n] = [ True if n.upper() == n else False, list(filter(lambda a: a != n, v)), 1 ]
                else:
                    for a in v:
                        if a != n and a not in nodes[n][1]:
                            nodes[n][1].append(a)
            l = f.readline()
    return (nodes, vertex)


def part1(G, s = 'start', e = 'end', path = []):
    nodes = G[0]
    paths = []
    for n in nodes[s][1]:
        if n == e:
            paths.append([s, e])
        elif path.count(n) < nodes[n][2] or nodes[n][0]:
            next = part1(G, n, e, path + [s])
            for m in next:
                paths.append([s] + m)
    return paths


def part2(G, s = 'start', e = 'end'):
    paths = []
    for n in tqdm(G[0].keys()):
        if n not in [s, e] and G[0][n][0] == False:
            G[0][n][2] = 2
            paths += part1(G)
            G[0][n][2] = 1

    return list(set([ ",".join(p) for p in paths]))


if __name__ == "__main__":
    fname = "day12-bs.txt";
    G = day12_load(fname)
    ret = part1(G)
    print("Part 1 {:s} {:d} (10)".format(fname, len(ret)))
    fname = "day12-bs2.txt";
    G = day12_load(fname)
    ret = part1(G)
    print("Part 1 {:s} {:d} (19)".format(fname, len(ret)))
    fname = "day12-s.txt";
    G = day12_load(fname)
    ret = part1(G)
    print("Part 1 {:s} {:d} (4411)".format(fname, len(ret)))
    
    fname = "day12-bs.txt";
    G = day12_load(fname)
    ret = part2(G)
    print("Part 2 {:s} {:d} (36)".format(fname, len(ret)))
    fname = "day12-s.txt";
    G = day12_load(fname)
    ret = part2(G)
    print("Part 1 {:s} {:d} (136767)".format(fname, len(ret)))
