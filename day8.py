

def part1_load(fname):
    SEGS = {}
    cpt = 0
    with open(fname) as f:        
        l = f.readline()
        while l != '':
            lr = l.strip().split('|')
            leftl = lr[0].strip().split()
            rightl = lr[1].strip().split()
            for r in rightl:                
                if len(r) in [2,3,4,7]:
                    cpt += 1
                SEGS[r] = leftl.copy()
            l = f.readline()
    return SEGS, cpt


def part2(fname):
    cpt = 0
    with open(fname) as f:        
        l = f.readline()
        while l != '':
            lr = l.strip().split('|')
            leftl = lr[0].strip().split()
            rightl = lr[1].strip().split()
            decode = {}
            encode = [ '' for _ in range(10) ]
            for l in leftl :
                if len(l) == 2:
                    decode[l] = 'l'
                    encode[1] = l
                elif len(l) == 3:
                    decode[l] = '7'
                    encode[7] = l
                elif len(l) == 4:
                    decode[l] = '4'
                    encode[4] = l
                elif len(l) == 7:
                    decode[l] = '8'
                    encode[8] = l
                else: # 0, 2, 3, 5, 6, 9
                    if encode[1] in l: # 0 3 9
                        if 
                    else : # 2 6 9

                
            cpt += int(decode)
    return cpt


if __name__ == "__main__":
    fname = "day8-bs.txt";
    SEGS, ret = part1_load(fname)
    print("Part 1 {:s} {:d} (26)".format(fname, ret))
    ret = part2(SEGS)
    print("Part 2 {:s} {:d} (12)".format(fname, ret))
    fname = "day8-s.txt";
    SEGS, ret = part1_load(fname)
    print("Part 1 {:s} {:d} (?)".format(fname, ret))