import numpy as np

def day25_load(fname='day25.txt'):
    with open(fname) as f:
        lines = f.read().split('\n')
        a = np.zeros((len(lines), len(lines[0])), dtype=np.int8)
        for i, l in enumerate(lines):
            for j, c in enumerate(l):
                if c=='>':
                    a[i][j]=1
                elif c== 'v':
                    a[i][j]=2
    return a


def day25_subiter(a, v):
    b = np.zeros_like(a)
    for i, e in enumerate(a):
        if e != 0:
            j = i+1 if i<len(a)-1 else 0
            if e == v and a[j] == 0:
                b[j] = e
            else:
                b[i] = e
    return b


def day25_subiter_1(a):
    return day25_subiter(a, 1)


def day25_subiter_2(a):
    return day25_subiter(a, 2)


def day25_step(min):
    tmp = np.apply_along_axis(day25_subiter_1, 1, min) # > 1
    out = np.apply_along_axis(day25_subiter_2, 0, tmp) # v 2
    return out
    


def day25_run(board):
    current = np.copy(board)
    next = np.zeros_like(board)
    step = 0
    done = False
    while done == False and step < 1000:
        #print(step)
        #print(current)
        next = day25_step(current)
        done = np.all(current == next)
        current = next
        step += 1
    return step


if __name__ == '__main__':
    board = day25_load('day25-s.txt')
    ret = day25_run(board)
    print("Part 1 - {0} (58)".format(ret))
    board = day25_load('day25.txt')
    ret = day25_run(board)
    print("Part 1 - {0} (278)".format(ret))
