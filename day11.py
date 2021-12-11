import numpy as np
from scipy import signal
from tqdm import tqdm

def day11_load(fname):
    with open(fname) as f:        
        ll = f.readlines()
    return np.array([ [ int(c) for c in l.strip() ] for l in ll ], dtype=np.int8)


def part1_step(M, step):
    scharr = np.array([ [ 1, 1, 1],
                        [ 1, 0, 1],
                        [ 1, 1, 1] ])

    m = M[step].copy() + 1

    flashing_all = np.zeros_like(m, dtype=bool)
    flashing = m > 9
    while np.count_nonzero(flashing)>0:
        flashing_all = flashing_all + flashing
        flashed = signal.convolve2d(flashing, scharr,  mode='same')
        m += flashed        
        flashing = (m > 9) * (flashing_all == False)

    m[m>9] = 0
    return m

def part1(m, max_step):
    ret = 0
    M = [m]
    for i in tqdm(range(max_step)):        
        m = part1_step(M, i)
        ret += (m==0).sum()
        M.append(m)
    return ret


def part2(m):
    ret = 0
    M = [m]

    def generator():
        while m.sum() != 0:    
            yield

    for _ in tqdm(generator()):
        m = part1_step(M, ret)
        ret += 1
        M.append(m)
       
    return ret


if __name__ == "__main__":
    fname = "day11-bs2.txt";
    M = day11_load(fname)
    ret = part1(M, 2)
    print("Part 1 {:s} {:d} (9)".format(fname, ret))
    fname = "day11-bs.txt";
    M = day11_load(fname)
    ret = part1(M, 10)
    print("Part 1 {:s} {:d} (204)".format(fname, ret))
    M = day11_load(fname)
    ret = part1(M, 100)
    print("Part 1 {:s} {:d} (1656)".format(fname, ret))
    fname = "day11-s.txt";
    M = day11_load(fname)
    ret = part1(M, 100)
    print("Part 1 {:s} {:d} (1667)".format(fname, ret))

    fname = "day11-s.txt";
    M = day11_load(fname)
    ret = part2(M)
    print("Part 2 {:s} {:d} (488)".format(fname, ret))
