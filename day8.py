

def part1(fname):    
    cpt = 0
    with open(fname) as f:        
        l = f.readline()
        while l != '':
            lr = l.strip().split('|')
            # leftl = lr[0].strip().split()
            rightl = lr[1].strip().split()
            for r in rightl:                
                if len(r) in [2,3,4,7]:
                    cpt += 1         
            l = f.readline()
    return cpt


def part2_sub(leftl, rightl):
    def included(sa, sb):
        for a in sa:
            if not a in sb:
                return False
        return True

    decode = {}
    encode = [ '' for _ in range(10) ]
    for l in leftl :
        if len(l) == 2:
            decode[''.join(sorted(l))] = '1'
            encode[1] = l
        elif len(l) == 3:
            decode[''.join(sorted(l))] = '7'
            encode[7] = l
        elif len(l) == 4:
            decode[''.join(sorted(l))] = '4'
            encode[4] = l
        elif len(l) == 7:
            decode[''.join(sorted(l))] = '8'
            encode[8] = l
    for l in leftl :
        if len(l) == 6: # 0 6 9
            if included(encode[4], l):
                decode[''.join(sorted(l))] = '9'
                encode[9] = l
            elif included(encode[1], l):
                decode[''.join(sorted(l))] = '0'
                encode[0] = l
            else:
                decode[''.join(sorted(l))] = '6'
                encode[6] = l
    for l in leftl :
        if len(l) == 5: # 2 5 3
            if included(encode[1], l):
                decode[''.join(sorted(l))] = '3'
                encode[3] = l
            elif included(l, encode[6]):
                decode[''.join(sorted(l))] = '5'
                encode[5] = l
            else:
                decode[''.join(sorted(l))] = '2'
                encode[2] = l
                
    return ''.join([ decode[''.join(sorted(r))] for r in rightl ])


def part2(fname):
    cpt = 0
    with open(fname) as f:        
        lig = f.readline()
        while lig != '':
            lr = lig.strip().split('|')
            v = part2_sub(lr[0].strip().split(), lr[1].strip().split())
            cpt += int(v)
            lig = f.readline()
    return cpt


if __name__ == "__main__":
    fname = "day8-bs.txt";
    ret = part1(fname)
    print("Part 1 {:s} {:d} (26)".format(fname, ret))
    ret = part2(fname)
    print("Part 2 {:s} {:d} (61229)".format(fname, ret))
    fname = "day8-s.txt";
    ret = part1(fname)
    print("Part 1 {:s} {:d} (514)".format(fname, ret))
    ret = part2(fname)
    print("Part 2 {:s} {:d} (1012272)".format(fname, ret))