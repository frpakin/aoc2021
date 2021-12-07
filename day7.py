import progressbar


with open("day7-s.txt") as f:
    DATA = [ list(map(int, "16,1,2,0,4,2,7,1,2,14".split(','))),
             list(map(int, f.readline().strip().split(','))) ]


def part1(data):
    crabs = {}

    def part1_sub(crabs, p):
        fuel = 0
        for c in crabs.keys():
            fuel += abs(c-p)*crabs[c]
        return fuel

    for d in data:
        v=crabs.get(d,0)
        crabs[d]=v+1
    pos_min, pox_max = min(crabs.keys()), max(crabs.keys())
    fuels = {}
    with progressbar.ProgressBar(min_value = pos_min, max_value=pox_max+1) as bar:
        for p in range(pos_min, pox_max+1):
            fuels[p] = part1_sub(crabs, p)
            bar.update(p)
    return min(fuels.values())


def part2(data):
    crabs = {}

    def part2_sub(crabs, p):
        fuel = 0
        for c in crabs.keys():
            cpt = 0
            for i in range(0, max(c, p)-min(c, p) + 1):
                cpt += i
            fuel += cpt*crabs[c]
        return fuel

    for d in data:
        v=crabs.get(d,0)
        crabs[d]=v+1
    pos_min, pox_max = min(crabs.keys()), max(crabs.keys())
    fuels = {}
    with progressbar.ProgressBar(min_value = pos_min, max_value=pox_max+1) as bar:
        for p in range(pos_min, pox_max+1):
            fuels[p] = part2_sub(crabs, p)
            bar.update(p)
    return min(fuels.values())

if __name__ == "__main__":
    ret = part1(DATA[0])
    print("Part 1 {:d} (37)".format(ret))
    ret = part1(DATA[1])
    print("Part 1 {:d} (328262)".format(ret))

    ret = part2(DATA[0])
    print("Part 2 {:d} (168)".format(ret))
    ret = part2(DATA[1])
    print("Part 2 {:d} (90040997)".format(ret))