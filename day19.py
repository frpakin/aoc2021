import numpy as np


def day19_load(fname):
    data = {}
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
            data[i] = scan
            i += 1
            s = f.readline()
    return data


def part1(data):
    return 0


if __name__ == "__main__":
    data = day19_load('day19-bs.txt')
    ret = part1(data)
    print("Part 1  {:d} (79)".format(ret))        


