from math import copysign

# target area: x=20..30, y=-10..-5
# target area: x=48..70, y=-189..-148


def part1_range(v_in, trange, max_step = 2**10):
    x, y, ymax, step = 0, 0, 0, 0
    vx = v_in[0]
    vy = v_in[1]
    while(x<max(trange[0])) and y>min(trange[1]) and (step<max_step):
        x += vx
        vx += - int(copysign(1, vx)) if vx != 0 else 0
        if vy == 0:
            ymax = y
        y += vy
        vy += -1
        step += 1
        if (x>=min(trange[0])) and (x<=max(trange[0])) and (y>= min(trange[1])) and (y<= max(trange[1])) :
            return True, ymax
    return (x>=min(trange[0])) and (x<=max(trange[0])) and (y>= min(trange[1])) and (y<= max(trange[1])), ymax


def part1(target):
    results = []
    for vx in range(1, max(target[0])+1):
        for vy in range(min(target[1]), 1+max(abs(target[1][0]), abs(target[1][1]))):
            ret, ymax = part1_range((vx, vy), target)
            if ret:
                results.append((vx, vy, ymax))

    ymax = 0
    for r in results:
        ymax = max(ymax, r[2])

    return ymax, len(results)

if __name__ == "__main__":
    #ret, ymax = part1_range((6,9), [[20, 30], [-10, -5]])
    ret, nb = part1([[20, 30], [-10, -5]])
    print("Part 1 {:d} (45)".format(ret))
    print("Part 2 {:d} (112)".format(nb))

    ret, nb = part1([[48, 70], [-189, -148]])
    print("Part 1 {:d} (17766)".format(ret))
    print("Part 2 {:d} (1733)".format(nb))