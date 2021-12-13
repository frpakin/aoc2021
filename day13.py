import numpy as np

def day13_load(fname):
    coords = []
    pliages = []
    with open(fname) as f:        
        l = f.readline()
        while l != '\n':
            coords.append([int(c) for c in l.strip().split(sep=',')])
            l = f.readline()
        l = f.readline()   # skip new line
        while l != '':
            args = l.strip().split()
            arg=args[-1].split(sep='=')
            pliages.append([ arg[0], int(arg[1])])
            l = f.readline()

    min_x, min_y = 0, 0
    max_x, max_y = 0, 0
    for c in coords:
        min_x = min(min_x, c[0])
        max_x = max(max_x, c[0])
        min_y = min(min_y, c[1])
        max_y = max(max_y, c[1])
    
    m = np.zeros((max_x+1, max_y+1), dtype = np.bool)
    for c in coords:
        m[c[0], c[1]] = True

    return m, pliages        
        

def fold_x(m, p):
    s = m.shape
    n = np.zeros((p, s[1]), dtype = np.bool)
    coords = np.nonzero(m)
    for i in range(len(coords[0])):
        if coords[0][i] > p:
            coords[0][i] = p - (coords[0][i] - p)
    n[coords] = True
    return n


def fold_y(m, p):
    s = m.shape
    n = np.zeros((s[0], p), dtype = np.bool)
    coords = np.nonzero(m)
    for i in range(len(coords[0])):
        if coords[1][i] > p:
            coords[1][i] = p - (coords[1][i] - p)
    n[coords] = True
    return n


def part1(M, pliages):
    m = M
    p = pliages[0]
    if p[0] == 'x':
        m = fold_x(m, p[1])
    elif p[0] == 'y':
        m = fold_y(m, p[1])
    else:
        print("Error !")
    return m


def part2(M, pliages):
    m = M
    for p in pliages:
        if p[0] == 'x':
            m = fold_x(m, p[1])
        elif p[0] == 'y':
            m = fold_y(m, p[1])
        else:
            print("Error !")
    return m
    

def pprint(m):
    for l in range(m.shape[1]):
        s = ''
        for c in range(m.shape[0]):
            s+= '#' if m[c, l] else '.'
        print(s)
    print()

if __name__ == "__main__":
    fname = "day13-bs.txt";
    M, pliages = day13_load(fname)
    M = part1(M, pliages)
    ret = (M==True).sum()
    print("Part 1 {:s} {:d} (17)".format(fname, ret))
    fname = "day13-s.txt";
    M, pliages = day13_load(fname)
    M = part1(M, pliages)
    ret = (M==True).sum()
    print("Part 1 {:s} {:d} (706)".format(fname, ret))
    
    fname = "day13-bs.txt";
    M, pliages = day13_load(fname)
    M = part2(M, pliages)
    pprint(M)
    fname = "day13-s.txt";
    M, pliages = day13_load(fname)
    M = part2(M, pliages)
    pprint(M) # LRFJBJEH

    

