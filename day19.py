import numpy as np
from tqdm import tqdm
from itertools import combinations

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
            data.append(scan)
            i += 1
            s = f.readline()
    return data


def generate(d):
    results = {}
    for i,j,k in [(0,1,2), (0,2,1), (1,2,0), (1,0,2), (2,0,1), (2,1,0)]:
        for op in [(1, 1, 1), (-1, 1, 1), (1, -1, 1), (1, 1, -1)]:
            ret = [ [], [], [] ]
            for e in range(len(d[0])):                            
                ret[0].append( op[0] * d[i][e])
                ret[1].append( op[1] * d[j][e])
                ret[2].append( op[2] * d[k][e])
            results[(i, j, k, op[0], op[1], op[2])] = np.array(ret)
    return results


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


def day19_match(base, scanner):
    t = [ None, None, None, None, None, None]
    orig = base[(0, 1, 2, 1, 1, 1)]

    for o in scanner.keys():
        i, j, k = o[0], o[1], o[2]
        op = (o[3], o[4], o[5])
        beacon = scanner[o]
        for l in range(3):
            matched = day19_matchaxis(orig[l], beacon[l])
            trans = list(matched.keys())
            if len(trans) > 0:
                #print("Axis 0 Rot:({:d},{:d},{:d}) Pol:({:d},{:d},{:d}) T[0]:{:d}  matched:{:d}".format(i, j, k, op[0], op[1], op[2], matched[0][0], matched[0][1]))
                t[l] = i
                t[3+l] = op[l] * trans[0]
        if not None in t:
            return t
    return t


def day19_compose(m, n):
    pm = m[2]
    pn = n[2]
    p = [ 0 for _ in range(6) ]
    p[0] = pm[pn[0]]
    p[1] = pm[pn[1]]
    p[2] = pm[pn[2]]
    p[3] = pm[3+pn[0]] + pn[3]
    p[4] = pm[3+pn[1]] + pn[4]
    p[5] = pm[3+pn[2]] + pn[5]
    return [ n[0], m[1], p]


def day19_getPath(matched, i):
    path = None
    for m in matched:
        if m[1] == i:
            if m[0] == 0:
                path = m
                break
            else:
                n = day19_getPath(matched, m[0])
                if n != None:
                    path = day19_compose(m,  n)
                    break
    return  path


def day19_invert(m):
    return [ m[1], m[0], 
            [ m[2][0], m[2][1], m[2][2], -m[2][3], -m[2][4], -m[2][5]] ]


def day19_apply(op, points):
    m = [[], [], []]
    for i in range(3):
        for j in range(len(points[0])):
            m[i].append(points[op[i]][j] + op[i+3])
    return m


def part1(data):
    orientations = []
    for d in data:
        orientations.append(generate(d))

    matched = []
    for c in tqdm(list(combinations(range(len(orientations)), 2))):
        i, j = c[0], c[1]
        ret = day19_match(orientations[i], orientations[j])
        if not None in ret:
            #print("Scanner {:d} and {:d} matched".format(i, j))
            matched.append([i, j, ret])


    inverted = []
    for m in matched:
        n = day19_invert(m)
        inverted.append(n)
    matched = matched + inverted

    beacons = {}
    for i in range(len(data)):
        if i != 0:
            op = day19_getPath(matched, i)
            moved = day19_apply(op[2], data[i])
            for j in range(len(moved[0])):
                beacons[(moved[0][j], moved[1][j], moved[2][j])] = (i, j)

    return beacons.keys()


if __name__ == "__main__":
    data = day19_load('day19-bs.txt')
    ret = len(part1(data))
    print("Part 1  {:d} (79)".format(ret))        


