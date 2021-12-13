import numpy as np

def day13_load(fname):
    coords = [[], []]
    pliages = []
    with open(fname) as f:        
        l = f.readline()
        while l != '\n':
            c = l.strip().split(sep=',')
            coords[0].append(int(c[0]))
            coords[1].append(int(c[1]))
            l = f.readline()
        l = f.readline()   # skip new line
        while l != '':
            args = l.strip().split()
            arg=args[-1].split(sep='=')
            pliages.append([ 0 if arg[0]=='x' else 1, int(arg[1])])
            l = f.readline()

    # min_x, min_y = np.amin(coords, axis=1)
    max_x, max_y = np.amax(coords, axis=1)
    m = np.zeros((max_x+1, max_y+1), dtype = bool)
    m[coords] = True

    return m, pliages        


def fold(coords, axis=0, p=0):
    for i in range(len(coords[0])):
        if coords[axis][i] > p:
            coords[axis][i] = p - (coords[axis][i] - p)
    return coords


def part1(M, pliages):
    p = pliages[0]
    coords = fold(np.nonzero(M), p[0], p[1])
    max_x, max_y = np.amax(coords, axis=1)
    m = np.zeros((max_x+1, max_y+1), dtype = bool)
    m[coords] = True
    return m


def part2(M, pliages):
    coords = np.nonzero(M)
    for p in pliages:
        coords = fold(coords, p[0], p[1])
    max_x, max_y = np.amax(coords, axis=1)
    m = np.zeros((max_x+1, max_y+1), dtype = bool)
    m[coords] = True
    return m
    

def pprint(m):
    print('\n'.join([''.join(['#' if m[c, l] else '.' for c in range(m.shape[0])]) 
        for l in range(m.shape[1])]))
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
