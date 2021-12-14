from tqdm import tqdm

def day14_load(fname):
    rules = {}
    vals = []
    with open(fname) as f:        
        l = f.readline().strip()
        seed = [ l[i:i+2] for i in range(len(l)-1) ]
        l = f.readline()    # skip new line
        l = f.readline()    # Read rules
        while l != '':
            key = l.strip().split('->')[0].strip()
            v = l.strip().split('->')[1].strip()
            rules[key] = [ key[0]+v, v+key[1] ]
            vals.append(v)
            l = f.readline()
    return seed, rules, list(set(vals))


def part1(seed, rules, max_step=1):
    for _ in tqdm(range(max_step)):
        ret = []
        for s in seed:
            ret += rules[s]
        seed = ret
    return ret


def part2(seed, rules, vals, max_step=40):
    counts = dict.fromkeys(vals, 0)
    r10 = {}
    for r in rules.keys():
        r10[r] = part1([r], rules, 20)
        day14_print(r10[r], vals)
    r40 = part1(seed, r10, 2)
    ret = part1(seed, r40, 1)
    return ret


def day14_print(pairs, vals):
    counts = dict.fromkeys(vals, 0)
    for p in pairs:
        counts[p[0]] += 1
    counts[pairs[-1][1]] += 1
    print(counts)
    return counts


def part1_result(prot):
    alpha = {}
    for p in prot:
        alpha[p[0]] = alpha.get(p[0], 0) + 1
    alpha[prot[-1][1]] += 1
    alpha_max = max(alpha.values())
    alpha_min = min(alpha.values())
    
    return alpha_max - alpha_min


if __name__ == "__main__":
    fname = "day14-bs.txt";
    SEED, RULES, VALS = day14_load(fname)
    prot = part1(SEED, RULES, 10)
    print("Part 1 {:s} {:d} {:d} (1588)".format(fname, len(prot)+1, part1_result(prot)))
    fname = "day14-s.txt";
    SEED, RULES, VALS = day14_load(fname)
    prot = part1(SEED, RULES, 10)
    print("Part 1 {:s} {:d} {:d} (2010)".format(fname, len(prot)+1, part1_result(prot)))

    fname = "day14-bs.txt";
    SEED, RULES, VALS = day14_load(fname)
    prot = part2(SEED, RULES, VALS, 40)
    print("Part 2 {:s} {:d} {:d} (1588)".format(fname, len(prot)+1, part1_result(prot)))
    fname = "day14-s.txt";
    SEED, RULES, VALS = day14_load(fname)
    prot = part2(SEED, RULES, VALS, 40)
    print("Part 2 {:s} {:d} {:d} (2010)".format(fname, len(prot)+1, part1_result(prot)))


