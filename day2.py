with open('day2-s.txt') as f:
    DATA = [
        "forward 5,down 5,forward 8,up 3,down 8,forward 2".split(','),
        f.readlines()
    ]

def part1(data):
    horiz, depth = 0, 0
    for d in data:
        c = d.split()
        v = int(c[1])
        if c[0] == 'forward':
            horiz += v
        elif c[0] == 'down':
            depth += v
        elif c[0] == 'up':
            depth -= v
    return horiz*depth

def part2(data):
    aim, horiz, depth = 0, 0, 0
    for d in data:
        c = d.split()
        v = int(c[1])
        if c[0] == 'forward':
            horiz += v
            depth += aim * v
        elif c[0] == 'down':
            aim += v
        elif c[0] == 'up':
            aim -= v
    return horiz*depth

ret = part1(DATA[0])
print("Part 1 {:d}".format(ret))
ret = part1(DATA[1])
print("Part 1 {:d}".format(ret))
ret = part2(DATA[0])
print("Part 2 {:d}".format(ret))
ret = part2(DATA[1])
print("Part 2 {:d}".format(ret))