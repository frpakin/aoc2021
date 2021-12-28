import numpy as np
from tqdm import tqdm
from itertools import combinations, product
from math import copysign


def day19_load(fname):
    data = []
    with open(fname) as f:        
        i = 0
        s = f.readline()
        while len(s)>0:
            scan = [ [], [], [] ]
            s = f.readline()
            while len(s)>0 and s!='\n':
                t = s.strip().split(',')
                for j in range(len(t)):
                    scan[j].append(int(t[j]))
                s = f.readline()
            data.append(np.array(scan))
            i += 1
            s = f.readline()
    return data


def day19_matchaxis(orig, beacon):
    results = {}
    for i in range(len(orig)):
        for j in range(len(beacon)):
            c = beacon[j] - orig[i]
            cpt = 0
            for k in range(len(orig)):
                for l in range(len(beacon)):
                    if c == beacon[l] - orig[k]:
                        cpt += 1
            if cpt > 11:
                results[c]= cpt
                return results
    return results


def day19_compose(m, n):
    pm = m[2]
    pn = n[2]
    p = [ 0 for _ in range(9) ]
    p[0] = pm[pn[0]]
    p[1] = pm[pn[1]]
    p[2] = pm[pn[2]]
    p[3] = pm[3+pn[0]] * pn[3]
    p[4] = pm[3+pn[1]] * pn[4]
    p[5] = pm[3+pn[2]] * pn[5]
    p[6] = pm[6+pn[0]] + pn[6]
    p[7] = pm[6+pn[1]] + pn[7]
    p[8] = pm[6+pn[2]] + pn[8]
    return [ n[0], m[1], p]


def day19_getPath(matched, i, depth):
    path = None
    if depth >= 0:
        for m in matched:
            if m[1] == i:
                if m[0] == 0:
                    path = m
                    break
                else:
                    n = day19_getPath(matched, m[0], depth-1)
                    if n != None:
                        path = day19_compose(m,  n)
                        break
    return  path


def day19_invert(m):
    return  [   m[1], m[0], 
                [ m[2][0], m[2][1], m[2][2], -m[2][3], -m[2][4], -m[2][5], m[2][6], m[2][7], m[2][8]]
            ]


def day19_apply(op, points):
    m = [[], [], []]
    for i in range(3):
        for j in range(len(points[0])):
            m[i].append(points[op[i]][j] * op[i+3] + op[i+6])
    return m




rot_init = [(1, 2, 3), (-2, 1, 3), (-1, -2, 3), (2, -1, 3), (-3, 2, 1), (-2, -3, 1), (3, -2, 1), (2, 3, 1), (-1, 2, -3), (-2, -1, -3), (1, -2, -3), (2, 1, -3), (3, 2, -1), (-2, 3, -1), (-3, -2, -1), (2, -3, -1), (1, -3, 2), (3, 1, 2), (-1, 3, 2), (-3, -1, 2), (1, 3, -2), (-3, 1, -2), (-1, -3, -2), (3, -1, -2)]
rots = []
for r in rot_init:
    rots.append( [ abs(r[0])-1, abs(r[1])-1, abs(r[2])-1, int(copysign(1, r[0])), int(copysign(1, r[1])), int(copysign(1, r[2])) ] )

def day19_match(base, scanner):
    t = [ None, None, None, None, None, None, None, None, None]
    for c in rots:
        t = [ None, None, None, None, None, None, None, None, None]
        for i in range(3):
            matched = day19_matchaxis(base[i], c[3+i] * scanner[c[i]])
            if len(matched.keys()) > 0:
                t[i] = c[i]
                t[3+i] = c[3+i]
                t[6+i] = list(matched.keys())[0]
        if not None in t:
            return t
    return t


def part1(data):
    matched = []
    for c in tqdm(list(combinations(range(len(data)), 2))):
        ret = day19_match(data[c[0]], data[c[1]])
        if not None in ret:
            #print("Scanner {:d} and {:d} matched".format(i, j))
            matched.append([c[0], c[1], ret])
    inverted = []
    for m in matched:
        n = day19_invert(m)
        inverted.append(n)
    matched = matched + inverted
    beacons = {}
    for i in range(len(data)):
        if i != 0:
            op = day19_getPath(matched, i, len(data))
            moved = day19_apply(op[2], data[i])
            for j in range(len(moved[0])):
                beacons[(moved[0][j], moved[1][j], moved[2][j])] = (i, j)

    return beacons.keys()


if __name__ == "__main__":
    data = day19_load('day19-bs.txt')
    ret = len(part1(data))
    print("Part 1  {:d} (79)".format(ret))
    data = day19_load('day19-s.txt')
    ret = len(part1(data))
    print("Part 1  {:d} (?)".format(ret))                
