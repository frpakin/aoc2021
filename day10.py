
def day10_load(fname):
    with open(fname) as f:        
        ll = [ l.strip() for l in f]
    return ll


def part1_check(l):
    matchedchars = {
        ')': '(',
        ']': '[',
        '}': '{',
        '>': '<',
    }
    stack = []
    for c in l:
        if c in '([{<':
            stack.append(c)
        elif c in ')]}>':
            if matchedchars[c] != stack.pop():
                return ('ILLEGAL', c)
    if len(stack) > 0:
        return ('INCOMPLETE', "".join(stack))
    return ('OK', 0)


def part1(ll):
    ret = []
    for l in ll:
        ret.append(part1_check(l))
    score = 0
    for r in ret:
        if r[0] == 'ILLEGAL':
            if r[1] == ')':
                score += 3
            elif r[1] == ']':
                score += 57
            elif r[1] == '}':
                score += 1197
            elif r[1] == '>':
                score += 25137
            else:
                print("Error")
    return score


def part2(ll):
    ret = []
    for l in ll:
        ret.append(part1_check(l))
    scores = []
    for r in ret:
        if r[0] == 'INCOMPLETE':
            score = 0
            for i in r[1][::-1]:
                score = 5*score
                if i == '(':
                    score += 1
                elif i == '[':
                    score += 2
                elif i == '{':
                    score += 3
                elif i == '<':
                    score += 4
                else:
                    print("Error")
            scores.append(score)
    sorted_scores=sorted(scores)        
    return sorted_scores[len(sorted_scores)//2]


if __name__ == "__main__":
    fname = "day10-bs.txt";
    PROG = day10_load(fname)
    ret = part1(PROG)
    print("Part 1 {:s} {:d} (26397)".format(fname, ret))
    ret = part2(PROG)
    print("Part 2 {:s} {:d} (288957)".format(fname, ret))
    fname = "day10-s.txt";
    PROG = day10_load(fname)
    ret = part1(PROG)
    print("Part 1 {:s} {:d} (216297)".format(fname, ret))
    ret = part2(PROG)
    print("Part 2 {:s} {:d} (2165057169)".format(fname, ret))