from tqdm import tqdm
from itertools import product

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


def intersect2(incube, cube, d):
    return []


def intersect3(incube, cube, d):
    return []


def intersect4(incube, cube, d):
    v = {}
    w = {}
    for c, k in product(range(3), range(2)):
        if incube[(c,k)] == True:
            v[(c,k)] = min(d[c][k], cube[c][k]) if k == 0 else max(d[c][k], cube[c][k])
        else:
            w[(c,k)] = min(d[c][k], cube[c][k]) if k == 0 else max(d[c][k], cube[c][k])
    return []


def part2(data):
    start = 0
    while data[start][1] == 0:
        start += 1
    cubes = [ data[start] ]

    for d in tqdm (data[start+1:]):
        for i in range(len(cubes)):
            incube = {}
            for c, k in product(range(3), range(2)):
                incube[(c,k)] = (d[0][c][k] >= cubes[i][0][c][0]) and (d[0][c][k] <= cubes[i][0][c][1])
            if True in incube.values():
                if not False in incube.values():
                    # Case 1: fully included and 1 -> nothing to do
                    if d[1] == 0:
                        # Case 2: That is a hollow, we need to replace cube with 8 cubes
                        cubes_new = intersect2(incube, cubes[i][0], d[0])
                        cubes.remove(i)
                        for cube_new in cubes_new:
                            cubes.insert(cube_new, i)
                else:
                    #intersection
                    if d[1] == 0:
                        # Case 3: That is a hollow, we need to break down cuboid cubes[i] into 6 cubes
                        cubes_new = intersect3(incube, cubes[i][0], d[0])
                        cubes.remove(i)
                        for cube_new in cubes_new:
                            cubes.insert(cube_new, i)
                    else:
                        # Case 4: that is a partial add, we need to break d[0] in 3 cuboids
                        cubes_new = intersect4(incube, cubes[i][0], d[0])
                        cubes += cubes_new
            else:
                # Case 5: No intersect full add
                if d[1] == 1:
                    cube = [ [ d[0][c][0], d[0][c][1] ] for c in range(3) ]
                    cubes.append([ cube, d[1] ])
    
    ret = 0
    for i in tqdm(range(len(cubes))):
        ret += (cubes[i][0][0][1]-cubes[i][0][0][0]) * (cubes[i][0][1][1]-cubes[i][0][1][0]) * (cubes[i][0][2][1]-cubes[i][0][2][0])
    return ret


def part2test(data):
    cubes = data
    ret = 0
    for i in tqdm(range(len(cubes))):
        v = (cubes[i][0][0][1]-cubes[i][0][0][0]) * (cubes[i][0][1][1]-cubes[i][0][1][0]) * (cubes[i][0][2][1]-cubes[i][0][2][0])
        if cubes[i][1] == 1:
            ret += v
        else:
            ret -= v
    return ret


if __name__ == "__main__":
    data = day22_load('day22-bs.txt')
    ret = part1(data)
    print("Part 1  {:d} (590784)".format(ret))

    data = day22_load('day22-bs.txt')
    ret = part2(data[0:20])
    print("Part 2/1  {:d} (590784)".format(ret))

    data = day22_load('day22-s.txt')
    ret = part1(data)
    print("Part 1  {:d} (527915)".format(ret))

    data = day22_load('day22-s.txt')
    ret = part2(data)
    print("Part 2  {:d} (?)".format(ret))


