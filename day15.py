import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra

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
    smat = [ [], [], [] ]
    for i in range(m.shape[0]):
        for j in range(m.shape[1]):            
            k = i * m.shape[0] + j
            for a in adj_finder(m, i, j):            
                l = a[0] * m.shape[0] + a[1]
                smat[0].append(k)
                smat[1].append(l)
                smat[2].append(m[a])
                
    graph = csr_matrix((smat[2], (smat[0], smat[1])), dtype=np.int8)
    #print(graph)
    dist_matrix = dijkstra(csgraph=graph, directed=True, indices=0, return_predecessors=False, min_only=True)
    #print(dist_matrix)
    return dist_matrix[-1]


def part2(m):
    full =  np.zeros((m.shape[0]*5, 5*m.shape[1]), dtype=np.int8)
    for i in range(5):
        for j in range(5):
            if i == 0 and j == 0:
                full[ 0:m.shape[0], 0:m.shape[1]  ] = m
            elif i == 0:
                full[ 0:m.shape[0], j*m.shape[1]:(j+1)*m.shape[1]  ] = full[ 0:m.shape[0], (j-1)*m.shape[1]:(j)*m.shape[1]  ] + 1
                a = full[ 0:m.shape[0], j*m.shape[1]:(j+1)*m.shape[1]  ] > 9
                full[ 0:m.shape[0], j*m.shape[1]:(j+1)*m.shape[1]  ] [a] = 1
            elif j == 0:
                full[ i*m.shape[0]:(i+1)*m.shape[0], 0:m.shape[1]  ] = full[ (i-1)*m.shape[0]:(i)*m.shape[0], 0:m.shape[1]  ] + 1
                a = full[ i*m.shape[0]:(i+1)*m.shape[0], 0:m.shape[1]  ] > 9
                full[ i*m.shape[0]:(i+1)*m.shape[0], 0:m.shape[1]  ] [a] = 1
            else:
                full[ i*m.shape[0]:(i+1)*m.shape[0], j*m.shape[1]:(j+1)*m.shape[1]  ] = full[ (i)*m.shape[0]:(i+1)*m.shape[0], (j-1)*m.shape[1]:(j)*m.shape[1]  ] + 1
                a = full[ i*m.shape[0]:(i+1)*m.shape[0], j*m.shape[1]:(j+1)*m.shape[1]  ] > 9
                full[ i*m.shape[0]:(i+1)*m.shape[0], j*m.shape[1]:(j+1)*m.shape[1]  ] [a] = 1
    ret = part1(full)
    return ret


if __name__ == "__main__":
    fname = "day15-bs.txt";
    M = day15_load(fname)
    ret = part1(M)
    print("Part 1 {:s} {:d} (40)".format(fname, int(ret)))
    fname = "day15-s.txt";
    M = day15_load(fname)
    ret = part1(M)
    print("Part 1 {:s} {:d} (592)".format(fname, int(ret)))

    fname = "day15-bs.txt";
    M = day15_load(fname)
    ret = part2(M)
    print("Part 2 {:s} {:d} (315)".format(fname, int(ret)))
    fname = "day15-s.txt";
    M = day15_load(fname)
    ret = part2(M)
    print("Part 2 {:s} {:d} (2897)".format(fname, int(ret)))