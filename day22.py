from tqdm import tqdm
from math import prod
from itertools import product
from sortedcontainers import SortedSet


def day22_load(fname):
    data = []
    with open(fname) as f:
        lines = f.readlines()
        for ll in lines:
            l = ll.split(' ')
            op = 1 if l[0] == 'on' else 0
            coords = l[1].strip().split(',')
            vals = []
            for c in coords:
                d = c.split('=')
                v = d[1].split('..')
                vals.append([ int(v[0]), 1+int(v[1]) ])
            data.append([ vals, op])
    return data


def part1(data):
    coords = {}
    for d in tqdm (data[0:20]):
        for c in product(range(*d[0][0]), range(*d[0][1]), range(*d[0][2]) ):
            coords[c] = d[1]
    ret = 0
    for k in coords.keys():
        if coords[k] == 1:
            ret += 1
    return ret


def part2_load(fname):
    data = [[], [], [], []]
    with open(fname) as f:
        lines = f.readlines()
        for ll in lines:
            l = ll.split(' ')
            op = 1 if l[0] == 'on' else 0
            data[3].append(op)
            coords = l[1].strip().split(',')
            for c in range(len(coords)):
                d = coords[c].split('=')
                v = d[1].split('..')
                data[c].append([ int(v[0]), int(v[1]) ])
    return data


def part2_sub(data, ax, bar):
    if len(data[0]) == 0:
        return 0
    if len(data[0]) == 1:
        return prod([ 1+r[0][1]-r[0][0] for r in data[:-1]]) * data[-1][0]
    
    xa=[data[ax][x][i] for x,i in product(range(len(data[ax])), range(2))]
    xb=[data[ax][x][1]+1 for x in range(len(data[ax]))]
    axis = SortedSet(xa + xb)
    s = 0
    for x_ndx in range(len(axis)):
        x = axis[x_ndx]
        lines = [ [] for _ in range(len(data)-1) ]
        for i in range(len(data[0])):
            if data[ax][i][0] <= x <= data[ax][i][1]:
                for j in range(len(data)-1):
                    lines[j].append(data[j if j<ax else j+1][i])
        dx = axis[x_ndx+1] - x if x_ndx < len(axis)-1 else 1
        if ax != 0:
            l = part2_sub(lines, ax-1, bar)
        else :
            if len(lines)>0 and len(lines[-1])>0:
                l = lines[-1][-1]
            else:
                l = 0 
        s += dx * l
        if ax==2:
            bar.update(1)
    return s


def part2(data, axis = 2):
    xa=[data[axis][x][i] for x,i in product(range(len(data[axis])), range(2))]
    xb=[data[axis][x][1]+1 for x in range(len(data[axis]))]
    axis_tmp = SortedSet(xa + xb)
    bar = tqdm(total=len(axis_tmp))
    return part2_sub(data, axis, bar=bar)


if __name__ == "__main__":
    data = day22_load('day22-bs.txt')
    ret = part1(data)
    print("Part 1  {:d} (590784)".format(ret))

    data = part2_load('day22-s5.txt')
    ret = part2([data[i][0:20] for i in range(4)])
    print("Part 2  {:d} (39)".format(ret))

    data = part2_load('day22-bs.txt')
    ret = part2([data[i][0:20] for i in range(4)])
    print("Part 2  {:d} (590784)".format(ret))

    data = part2_load('day22-s3.txt')
    ret = part2(data)
    print("Part 2  {:d} (114660)".format(ret))

    data = part2_load('day22-s4.txt')
    ret = part2(data)
    print("Part 2  {:d} (114661)".format(ret))

    data = part2_load('day22-s2.txt')
    ret = part2(data)
    print("Part 2  {:d} (2758514936282235)".format(ret))

    data = day22_load('day22-s.txt')
    ret = part1(data)
    print("Part 1  {:d} (527915)".format(ret))

    data = part2_load('day22-s.txt')
    ret = part2(data)
    print("Part 2  {:d} (1218645427221987)".format(ret))


