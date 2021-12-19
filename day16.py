from math import prod


samples = [ '8A004A801A8002F478', '620080001611562C8802118E34', 'C0015000016115A2E0802F182340', 'A0016C880162017C3686B18A3D4780' ]


def tobin(input):
    scale = 16 ## equals to hexadecimal
    num_of_bits = 4*len(input)
    return bin(int(input, scale))[2:].zfill(num_of_bits)


def decode_val(bits_3):
    return int(bits_3, 2)


def decode_word(bits_in):
    pos = 0
    val = ''
    while bits_in[pos] == '1':
        val += bits_in[pos+1:pos+1+4]
        pos += 5
    val += bits_in[pos+1:pos+1+4]
    pos += 5
    return int(val, 2), pos
    
    
def decode_body(bits_in, versions):
    pos = 0
    while pos < len(bits_in):
        pos += decode_header(bits_in[pos:], versions)
    return pos


def decode_packets(bits_in, nb, versions):
    pos = 0
    for _ in range(nb):
        pos += decode_header(bits_in[pos:], versions)
    return pos


def decode_header(bits_in, versions):
    pos = 0
    h_version = decode_val(bits_in[pos:pos+3])
    versions.append(h_version)
    pos += 3
    h_id = decode_val(bits_in[pos:pos+3])
    pos += 3
    if h_id == 4:
        w, next_pos = decode_word(bits_in[pos:])
        pos += next_pos
    else:  #operators
        mode = bits_in[pos]
        pos += 1
        if mode == '0':
            length = int(bits_in[pos:pos+15], 2)
            pos += 15
            b = decode_body(bits_in[pos: pos+length], versions)
            pos += length
        else:
            length = int(bits_in[pos:pos+11], 2)
            pos += 11
            pos += decode_packets(bits_in[pos:], length, versions)
    return pos

def part1(input):
    bits_in = tobin(input)    
    versions = []
    next_pos=decode_header(bits_in, versions)

    return sum(versions)



def decode_part2_word(bits_in):
    pos = 0
    val = ''
    while bits_in[pos] == '1':
        val += bits_in[pos+1:pos+1+4]
        pos += 5
    val += bits_in[pos+1:pos+1+4]
    pos += 5
    return int(val, 2), pos
    
    
def decode_part2_body(bits_in, root):
    pos = 0
    branch = []
    while pos < len(bits_in):
        pos += decode_part2(bits_in[pos:], branch)
    root.append(branch)
    return pos


def decode_part2_packets(bits_in, nb, root):
    pos = 0
    branch = []
    for _ in range(nb):
        pos += decode_part2(bits_in[pos:], branch)
    root.append(branch)
    return pos


def decode_part2(bits_in, root):
    pos = 0
    h_version = decode_val(bits_in[pos:pos+3])
    pos += 3
    h_id = decode_val(bits_in[pos:pos+3])
    pos += 3
    if h_id == 4:
        w, next_pos = decode_part2_word(bits_in[pos:])
        pos += next_pos
        root.append([4, w])
    else:  #operators
        mode = bits_in[pos]
        pos += 1
        branch = []
        if mode == '0':
            length = int(bits_in[pos:pos+15], 2)
            pos += 15
            decode_part2_body(bits_in[pos: pos+length], branch)
            pos += length
        else:
            length = int(bits_in[pos:pos+11], 2)
            pos += 11
            pos += decode_part2_packets(bits_in[pos:], length, branch)
        root.append([h_id, branch[0]])
    return pos


def eval_part2(a):
    if a[0] == 4:
        ret = a[1]
    elif a[0] == 0:            
        ret = sum([eval_part2(b) for b in a[1]])
    elif a[0] == 1:
        ret = prod([eval_part2(b) for b in a[1]])
    elif a[0] == 2:
        ret = min([eval_part2(b) for b in a[1]])
    elif a[0] == 3:
        ret = max([eval_part2(b) for b in a[1]])
    elif a[0] == 5:
        ret = 1 if eval_part2(a[1][0]) > eval_part2(a[1][1]) else 0
    elif a[0] == 6:
        ret = 1 if eval_part2(a[1][0]) < eval_part2(a[1][1]) else 0
    elif a[0] == 7:
        ret = 1 if eval_part2(a[1][0]) == eval_part2(a[1][1]) else 0
    else:
        ret = -1
    
    return ret


def part2(input):
    bits_in = tobin(input)    
    root = []
    next_pos=decode_part2(bits_in, root)
    ret = eval_part2(root[0])
    return ret


if __name__ == "__main__":
    
    print("tobin D2FE28 {:s} (110100101111111000101000)".format(tobin('D2FE28')))
    part1('D2FE28')
    part1('38006F45291200')
    part1('EE00D40C823060')

    ret = part1(samples[0])
    print("Part 1 {:s} {:d} (16)".format(samples[0], ret))
    ret = part1(samples[1])
    print("Part 1 {:s} {:d} (12)".format(samples[1], ret))
    ret = part1(samples[2])
    print("Part 1 {:s} {:d} (23)".format(samples[2], ret))
    ret = part1(samples[3])
    print("Part 1 {:s} {:d} (31)".format(samples[3], ret))

    with open('day16-s.txt') as f:        
        ll = f.readline().strip()
    ret = part1(ll)
    print("Part 1 {:s}... {:d} (889)".format(ll[0:30], ret))


    ret = part2('C200B40A82')
    print("Part 2 C200B40A82 {:d} (3)".format(ret))
    ret = part2('04005AC33890')
    print("Part 2 04005AC33890 {:d} (54)".format(ret))
    ret = part2('880086C3E88112')
    print("Part 2 880086C3E88112 {:d} (7)".format(ret))
    ret = part2('CE00C43D881120')
    print("Part 2 CE00C43D881120 {:d} (9)".format(ret))
    ret = part2('D8005AC2A8F0')
    print("Part 2 D8005AC2A8F0 {:d} (1)".format(ret))
    ret = part2('F600BC2D8F')
    print("Part 2 F600BC2D8F {:d} (0)".format(ret))

    ret = part2('9C005AC2F8F0')
    print("Part 2 9C005AC2F8F0 {:d} (0)".format(ret))
    ret = part2('9C0141080250320F1802104A08')
    print("Part 2 9C0141080250320F1802104A08 {:d} (1)".format(ret))


    with open('day16-s.txt') as f:        
        ll = f.readline().strip()
    ret = part2(ll)
    print("Part 2 {:s}... {:d} (739303923668)".format(ll[0:30], ret))

    