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


def part2_addlength(data):
    if len(data) == 0:
        return 0
    elif len(data[-1]) == 0:
        return 0
    else:
        return data[-1][0]
    #elif len(data) == 1:
    #    return data[0][1] - data[0][0] + 1
    
    xaxis = []
    for x in data:
        xaxis.append(x[0])
        xaxis.append(x[1])
    xaxis = sorted(set(xaxis))
    l = 0
    x_ndx = 0
    while(x_ndx < len(xaxis) -1):
        x = xaxis[x_ndx]
        x_extent = x
        for i in range(len(data)):
            if data[i][0] == x:
                x_extent = max(data[i][1], x_extent)
            if data[i][1] == x:
                x_ndx += 1
                break
        if x != x_extent:
            l += (x_extent - x) +1
            x_ndx = xaxis.index(x_extent)
    return l


def part2_length(lines):
    if len(lines[0]) == 0:
        return 0
    if len(lines[0]) == 1:
        return (lines[0][0][1] - lines[0][0][0])*lines[1][0]
    start = 0
    while start<len(lines[1]) and lines[1][start] == 0:
        start += 1
    if start == len(lines[1]):
        return 0
    line = lines[0][start]
    xaxis = [ line.copy() ]
    for i in range(start+1, len(lines[0])):
        line = lines[0][i]
        if len(xaxis) == 0:
            if lines[1][i] == 1:
                xaxis.append(line.copy())
        else:
            for x_ndx, x in enumerate(xaxis):
                if (x[0] <= line[0] <= x[1]) and (x[0] <= line[1] <= x[1]):
                    if lines[1][i] == 0:
                        if (x[0] == line[0]) and (x[1] == line[1]): 
                            xaxis.remove(x)
                        else:
                            tmp = xaxis[x_ndx][1]
                            xaxis[x_ndx][1] = line[0]-1
                            xaxis.insert(x_ndx+1, [line[1]+1, tmp])
                elif (x[0] <= line[0] <= x[1]) :
                    if lines[1][i] == 1:
                        xaxis[x_ndx][1] = line[1]
                    else:
                        xaxis[x_ndx][1] = line[0]-1
                elif (x[0] <= line[1] <= x[1]) :
                    if lines[1][i] == 1:
                        xaxis[x_ndx][0] = line[0]
                    else:
                        xaxis[x_ndx][0] = line[1]+1
                else:
                    if lines[1][i] == 1:
                        xaxis[x_ndx][0] = line[0]
                        xaxis[x_ndx][1] = line[1]
    return part2_addlength(xaxis)


def part2_sub(data, ax):
    if len(data[0]) == 0:
        return 0
    if len(data[0]) == 1:
        return prod([ 1+r[0][1]-r[0][0] for r in data[:-1]]) * data[-1][0]
        
    axis = SortedSet([data[ax][x][i] for x,i in product(range(len(data[ax])), range(2))])
    s = 0
    x_ndx = 0
    while(x_ndx < len(axis)):
        pc = 0
        x = axis[x_ndx]
        lines = [ [] for _ in range(len(data)-1) ]
        for i in range(len(data[0])):
            if data[ax][i][0] <= x <= data[ax][i][1]:
                for j in range(len(data)-1):
                    lines[j].append(data[j if j<ax else j+1][i])
            if data[ax][i][0] == x:
                pc += 1
            if data[ax][i][1] == x:
                pc += -1
        if pc > 0:
            l = part2_addlength(lines) if ax == 0 else part2_sub(lines, ax-1)
            dx = 1
            if x_ndx < len(axis)-1 : 
                dx = axis[x_ndx+1] - x
            s += dx * l
        x_ndx += 1
    return s


def part2(data, axis = 2):
    return part2_sub(data, axis)


if __name__ == "__main__":
    data = day22_load('day22-bs.txt')
    ret = part1(data)
    print("Part 1  {:d} (590784)".format(ret))

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
    print("Part 2  {:d} (??????????????????)".format(ret))


