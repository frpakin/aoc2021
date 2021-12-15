from tqdm import tqdm
import itertools, sys
spinner = itertools.cycle(['-', '/', '|', '\\'])


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
    c20 = {}
    for k in rules.keys():
        r20 = part1([k], rules, 9)
        alpha = {}
        for p in r20:
            alpha[p[0]] = alpha.get(p[0], 0) + 1
        alpha[r20[-1][1]] = alpha.get(r20[-1][1], 0) + 1
        c20[k] = alpha
    ret = part1(seed, rules, 1)
    #ret = seed
    counts = {}
    for p in tqdm(ret):
        for k in c20[p].keys():
            counts[k] = counts.get(k, 0) + c20[p][k]
    for s in seed[1:]:
        counts[s[0]] += -1
        counts[s[1]] += -1
    return counts


def part3(seed, rules, vals, max_step=40):
    counts = dict.fromkeys(vals, 0)
    
    if max_step ==0:
        for p in seed:
            counts[p[0]] += 1
        counts[seed[-1][1]] += 1            
    else :
        for s in seed:
            c = part2(rules[s], rules, vals, max_step-1)
            for k in c.keys():
                counts[k] += c[k]
    if max_step in [20, 30, 32, 35, 36, 37, 38, 39, 40] :
        print(max_step, counts)
    return counts


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


def part2_result(alpha):
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
    prot = part2(SEED, RULES, VALS, 10)
    print("Part 2 {:s} {:d} {:d} (2188189693529)".format(fname, len(prot)+1, part2_result(prot)))
    print(prot)

    fname = "day14-bs.txt";
    SEED, RULES, VALS = day14_load(fname)
    prot = part2(SEED, RULES, VALS, 40)
    print("Part 2 {:s} {:d} {:d} (2188189693529)".format(fname, len(prot)+1, part2_result(prot)))
    print(prot)
    fname = "day14-s.txt";
    SEED, RULES, VALS = day14_load(fname)
    prot = part2(SEED, RULES, 40)
    print("Part 2 {:s} {:d} {:d} (?)".format(fname, len(prot)+1, part2_result(prot)))
    print(prot)

