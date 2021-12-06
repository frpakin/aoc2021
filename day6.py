with open("day6-s.txt") as f:
    DATA = [ list(map(int, "3,4,3,1,2".split(','))),
             list(map(int, f.readline().strip().split(',')))    ]


def part1(data, nb_days=80):
    fishes = [ 0 for _ in range(10)]
    for d in data:
        fishes[d] += 1
    for day in range(nb_days):
        next_gen = [0 for _ in range(10)]
        next_gen[8] = fishes[0]
        next_gen[7] = fishes[8]
        next_gen[6] = fishes[7] + fishes[0]
        next_gen[5] = fishes[6]
        next_gen[4] = fishes[5]
        next_gen[3] = fishes[4]
        next_gen[2] = fishes[3]
        next_gen[1] = fishes[2]
        next_gen[0] = fishes[1]
        fishes = next_gen
    return sum(fishes)


if __name__ == "__main__":
    ret = part1(DATA[0])
    print("Part 1 {:d} (5934)".format(ret))
    ret = part1(DATA[1], 80)
    print("Part 1 {:d} (?)".format(ret))
    ret = part1(DATA[0], 256)
    print("Part 2 {:d} (26984457539)".format(ret))
    ret = part1(DATA[1], 256)
    print("Part 2 {:d} (1653559299811)".format(ret))