import re
import math


def day5_load(fname):
    SEGS = []
    p = re.compile(r"(?P<x1>\d+),(?P<y1>\d+) -> (?P<x2>\d+),(?P<y2>\d+)")
    with open(fname) as f:        
        l = f.readline()
        while l != '':
            m=p.match(l)            
            SEGS.append(list(map(int, m.groups())))
            l = f.readline()
    return SEGS
    

def part1(segs, limit=2):
    points = {}
    for s in segs:
        if s[0] == s[2]:
            for y in range(min(s[1], s[3]), max(s[1], s[3])+1):
                v = points.get((s[0],y), 0)
                points[(s[0],y)] = v+1
        if s[1] == s[3]:
            for x in range(min(s[0], s[2]), max(s[0], s[2])+1):
                v = points.get((x, s[1]), 0)
                points[(x, s[1])] = v+1
    cpt = 0
    for k in points.keys():
        if points[k] >= limit:
            cpt += 1

    for l in range(10):
        row = ""
        for c in range(10):
            v=points.get((c,l), 0)
            c = '.' if v==0 else str(v)
            row += c
        print(row)
    return cpt


def part2(segs, limit=2):
    points = {}
    for s in segs:
        if s[0] == s[2]:
            for y in range(min(s[1], s[3]), max(s[1], s[3])+1):
                v = points.get((s[0],y), 0)
                points[(s[0],y)] = v+1
        elif s[1] == s[3]:
            for x in range(min(s[0], s[2]), max(s[0], s[2])+1):
                v = points.get((x, s[1]), 0)
                points[(x, s[1])] = v+1
        else:
            x = s[0]
            y = s[1]
            x_inc = int(math.copysign(1, s[2] - s[0]))
            y_inc = int(math.copysign(1, s[3] - s[1]))
            while x!= s[2]+x_inc:                
                v = points.get((x,y), 0)
                points[(x,y)] = v+1
                x += x_inc
                y += y_inc
    cpt = 0
    for k in points.keys():
        if points[k] >= limit:
            cpt += 1
    return cpt


if __name__ == "__main__":
    fname = "day5-bs.txt";
    SEGS = day5_load(fname)
    ret = part1(SEGS)
    print("Part 1 {:s} {:d} (5)".format(fname, ret))
    ret = part2(SEGS)
    print("Part 2 {:s} {:d} (12)".format(fname, ret))

    fname = "day5-s.txt";
    SEGS = day5_load(fname)
    ret = part1(SEGS)
    print("Part 1 {:s} {:d} (?)".format(fname, ret))
    ret = part2(SEGS)
    print("Part 2 {:s} {:d} (?)".format(fname, ret))