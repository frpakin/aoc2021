with open('day3-s.txt') as f:
    DATA = [
        "00100 11110 10110 10111 10101 01111 00111 11100 10000 11001 00010 01010".split(),
        [ x.strip() for x in f ]
    ]


def sub(data, pos):
    cpt_1, cpt_0 = 0, 0
    for d in data:
        if d[pos] == '1':
            cpt_1 += 1
        elif d[pos] == '0':
            cpt_0 += 1
    return cpt_1, cpt_0

def part1(data):
    gamma = ''
    epsilon = ''
    for i in range(len(data[0])):
        cpt_1, cpt_0 = sub(data, i)        
        gamma += '1' if cpt_1 > cpt_0 else '0'
        epsilon += '0'if cpt_1 > cpt_0 else '1'
    return int(gamma, 2) * int(epsilon, 2)

def part2(data, pos=0):
    cpt_1, cpt_0 = sub(data, pos)
    extracted = []
    for d in data:
        if (d[pos] == '1' and cpt_1 > cpt_0) or (d[pos] == '0' and cpt_0 > cpt_1) or (d[pos] == '1' and cpt_1 == cpt_0):
            extracted.append(d)
    
    return int(extracted[0], 2) if len(extracted)==1 else part2(extracted, pos+1)

def part2b(data, pos=0):
    cpt_1, cpt_0 = sub(data, pos)
    extracted = []
    for d in data:
        if (d[pos] == '1' and cpt_1 < cpt_0) or (d[pos] == '0' and cpt_0 < cpt_1) or (d[pos] == '0' and cpt_1 == cpt_0):
            extracted.append(d)
    
    return int(extracted[0], 2) if len(extracted)==1 else part2b(extracted, pos+1)

def part2c_sub(data, pos=0, mode=0):
    cpt_1, cpt_0 = sub(data, pos)
    extracted = []
    for d in data:
        if mode == 0:
            if (d[pos] == '1' and cpt_1 > cpt_0) or (d[pos] == '0' and cpt_0 > cpt_1) or (d[pos] == '1' and cpt_1 == cpt_0):
                extracted.append(d)
        else:
            if (d[pos] == '1' and cpt_1 < cpt_0) or (d[pos] == '0' and cpt_0 < cpt_1) or (d[pos] == '0' and cpt_1 == cpt_0):
                extracted.append(d)
    
    return int(extracted[0], 2) if len(extracted)==1 else part2c_sub(extracted, pos+1, mode)

def part2c(data):
    return part2c_sub(data, pos=0, mode=0) * part2c_sub(data, pos=0, mode=1)

ret = part1(DATA[0])
print("Part 1 {:d}".format(ret))
ret = part1(DATA[1])
print("Part 1 {:d}".format(ret))
ret = part2(DATA[0])
print("Part 2 {:d}".format(ret))
ret = part2b(DATA[0])
print("Part 2b {:d}".format(ret))
ret = part2(DATA[1]) * part2b(DATA[1])
print("Part 2 {:d}".format(ret))
ret = part2c(DATA[1])
print("Part 2c {:d}".format(ret))