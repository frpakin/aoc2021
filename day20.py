from tqdm import tqdm

prog_sample = '..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#'
imag_sample = [ '#..#.',
                '#....',
                '##..#',
                '..#..',
                '..###' ]


def day20_pixvalpad(imag, l, c, infinite):
    if c == 0:
        v = infinite + imag[l][max(0,c-1):1+min(c+1, len(imag[l])-1)]
    elif c>=len(imag[0])-1:
        v = imag[l][max(0,c-1):1+min(c+1, len(imag[l])-1)] + infinite
    else:
        v = imag[l][max(0,c-1):1+min(c+1, len(imag[l])-1)]
    return v


def day20_pixval(imag, l, c, infinite):
    v = [infinite*3, infinite, infinite*3]
    if l > 0:
        v[0] = day20_pixvalpad(imag, l-1, c, infinite)
    v[1] = day20_pixvalpad(imag, l, c, infinite)
    if l<len(imag)-1:
        v[2] = day20_pixvalpad(imag, l+1, c, infinite)

    return "".join(v)


def day20_decode(valstr):
    vs = valstr.replace('.','0').replace('#', '1')
    return int(vs, 2)


def day20_extend(imag, ext=1, infi='.'):
    pad = infi  * (2*ext+len(imag[0]))
    pad2 = infi * ext
    ret = [ pad * ext ]
    for l in range(len(imag)):
        ret.append(pad2 + imag[l] + pad2)
    for _ in range(ext):
        ret.append(pad)
    return ret


def part1_count(imag):
    return sum([ l.count('#') for l in imag ])


def part1(prog, imag, max_step):
    infinite = '.'
    img = imag
    for _ in tqdm(range(max_step)):
        img = day20_extend(img, 1, infinite)
        img_next = []
        for l in range(len(img)):
            line = ''
            for c in range(len(img[l])):
                s = day20_pixval(img, l, c, infinite)
                ndx = day20_decode(s)
                line += prog[ndx]
            img_next.append(line)
        img = img_next
        infinite = prog[day20_decode(infinite  * 9)]
    return part1_count(img)


def day20_load(fname):
    with open(fname) as f:
        lines = f.readlines()
        return [ lines[0].strip(), [ l.strip() for l in lines[2:]] ]


if __name__ == "__main__":
    #data = day20_load('day20-s.txt')
    ret = part1(prog_sample, imag_sample, 2)
    print("Part 1  {:d} (35)".format(ret))

    DATA = day20_load('day20-s.txt')
    ret = part1(DATA[0], DATA[1], 2)
    print("Part 1  {:d} (5391)".format(ret))

    ret = part1(prog_sample, imag_sample, 50)
    print("Part 2  {:d} (3351)".format(ret))

    DATA = day20_load('day20-s.txt')
    ret = part1(DATA[0], DATA[1], 50)
    print("Part 2  {:d} (16383)".format(ret))
