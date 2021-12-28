

prog_sample = '..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#'
imag_sample = [ '#..#.',
                '#....',
                '##..#',
                '..#..',
                '..###' ]


def day20_pixvalpad(imag, l, c):
    if c == 0:
        v = '.' + imag[l][max(0,c-1):1+min(c+1, len(imag[l])-1)]
    elif c>=len(imag[0])-1:
        v = imag[l][max(0,c-1):1+min(c+1, len(imag[l])-1)] + '.'
    else:
        v = imag[l][max(0,c-1):1+min(c+1, len(imag[l])-1)]
    return v


def day20_pixval(imag, l, c):
    v = ['...', '.', '...']
    if l > 0:
        v[0] = day20_pixvalpad(imag, l-1, c)
    v[1] = day20_pixvalpad(imag, l, c)
    if l<len(imag)-1:
        v[2] = day20_pixvalpad(imag, l+1, c)

    return "".join(v)


def day20_decode(valstr):
    vs = valstr.replace('.','0').replace('#', '1')
    return int(vs, 2)


def day20_extend(imag):
    pad = '.'  * (2+len(imag[0]))
    ret = [ pad ]
    for l in range(len(imag)):
        ret.append('.' + imag[l] +'.')
    ret.append(pad)
    return ret


def part1_count(imag):
    ret = 0
    for l in range(len(imag)):
        ret += imag[l].count('#')
    return ret


def part1(prog, imag, max_step):
    img = imag
    for _ in range(max_step):
        img = day20_extend(img)
        img_next = []
        for l in range(len(img)):
            line = ''
            for c in range(len(img[0])):
                s = day20_pixval(img, l, c)
                ndx = day20_decode(s)
                line += prog[ndx]
            img_next.append(line)
        img = img_next
    return part1_count(img)


def day20_load(fname):
    data = [ None, None ]
    with open(fname) as f:
        lines = f.readlines()
        data[0] = lines[0].strip()
        data[1] = [ l.strip() for l in lines[2:]]
    return data


if __name__ == "__main__":
    #data = day20_load('day20-s.txt')
    ret = part1(prog_sample, imag_sample, 2)
    print("Part 1  {:d} (35)".format(ret))

    DATA = day20_load('day20-s.txt')
    ret = part1(DATA[0], DATA[1], 2)
    print("Part 1  {:d} (?)".format(ret))
