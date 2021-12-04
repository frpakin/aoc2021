

def day4_load(fname):
    with open(fname) as f:
        TOKENS = list(map(int, f.readline().strip().split(',')))
        BOARDS = []
    
        while f.readline() != '':
            #board = []
            #for _ in range(5):
            #    board += f.readline().strip().split()
            #BOARDS.append(board)
            BOARDS.append([list(map(int, f.readline().strip().split())) for _ in range(5)])
    return TOKENS, BOARDS
        

def part1(tokens, boards):
    SCORE = [ [[0, 0, 0, 0, 0], [0, 0, 0 ,0, 0]] for _ in range(len(boards))]
    marked = {}
    for token in tokens:
        for b in range(len(boards)):
            board = boards[b]
            for l in range(len(board)):
                line = board[l]
                if token in line:
                    c = line.index(token)
                    SCORE[b][0][l] += 1
                    SCORE[b][1][c] += 1
                    marked[(b,l,c)] = True
                    # check for a winner
                    if SCORE[b][0][l] == 5 or SCORE[b][1][c] == 5:
                        tt= 0
                        for ll in range(len(board)):
                            for cc in range(len(board)):
                                if marked.get((b,ll,cc), False) != True:
                                    tt += board[ll][cc]
                        return token * tt
    return -1


def score(token, boards, b, marked):
    tt= 0
    board = boards[b]
    for ll in range(len(board)):
        for cc in range(len(board)):
            if marked.get((b,ll,cc), False) != True:
                tt += board[ll][cc]
    return token * tt


def part2(tokens, boards):
    SCORE = [ [[0, 0, 0, 0, 0], [0, 0, 0 ,0, 0]] for _ in range(len(boards))]
    marked = {}
    winner = {}
    for token in tokens:
        for b in range(len(boards)):
            board = boards[b]
            for l in range(len(board)):
                line = board[l]
                if token in line:
                    c = line.index(token)
                    SCORE[b][0][l] += 1
                    SCORE[b][1][c] += 1
                    marked[(b,l,c)] = True
                    # check for a winner
                    if SCORE[b][0][l] == 5 or SCORE[b][1][c] == 5:
                        winner[b] = score(token, boards, b, marked)
                        if len(winner) == len(boards):
                            return winner[b]
    return -1


if __name__ == "__main__":
    fname = "day4-bs.txt";
    TOKENS, BOARDS = day4_load(fname)
    ret = part1(TOKENS, BOARDS)
    print("Part 1 {:s} {:d} (4512)".format(fname, ret))
    ret = part2(TOKENS, BOARDS)
    print("Part 2 {:s} {:d} (1924)".format(fname, ret))
    print("----------------")
    fname = "day4-s.txt";
    TOKENS, BOARDS = day4_load(fname)
    ret = part1(TOKENS, BOARDS)
    print("Part 1 {:s} {:d}".format(fname, ret))
    ret = part2(TOKENS, BOARDS)
    print("Part 2 {:s} {:d}".format(fname, ret))