from itertools import cycle, islice


class Dice:
    def __init__(self):
        self.sides = cycle([i+1 for i in range(100)])
        self.cpt = 0

    def roll(self):
        self.cpt += 3
        return next(self.sides) + next(self.sides) + next(self.sides)


def boardpos(pos, roll, board_size=10):
    off = roll % board_size
    if (pos + off) > 10:
        ret =  (pos + off) % board_size
    else :
        ret = pos + off
    return ret


def part1(pos1, pos2, max_score):
    dice = Dice()
    winner, looser = None, None
    powns = [ pos1 , pos2 ]
    scores = [ 0, 0 ]
    while(winner == None):
        powns[0] = boardpos(powns[0], dice.roll())
        scores[0] += powns[0]
        if scores[0] >= max_score:
            winner = 0
            looser = 1
        if winner == None:
            powns[1] = boardpos(powns[1], dice.roll())
            scores[1] += powns[1]
            if scores[1] >= max_score:
                winner = 1
                looser = 0

    return scores[looser]*dice.cpt


def part2(pos1, pos2, max_score=21):
    scores = [ [ 0 ] * 21, [ 0 ] * 21 ] 

    powns =  [ [ 0 ] * 10, [ 0 ] * 10 ] 
    powns[0][pos1-1] = 1
    powns[1][pos2-1] = 1

    dirac_dice = [ [3, 4, 5, 6 ,7, 8, 9], [1, 3, 6, 7, 6, 3, 1] ]

    winner = None
    while scores[0][20] + scores[1][20] == 0:
        for player in range(2):
            next_powns = [ 0 ] * 10
            for pos in range(10):
                for d in range(len(dirac_dice[0])):
                    next_powns[ boardpos(pos+1, dirac_dice[0][d]) - 1 ] += powns[player][pos] * dirac_dice[1][d]
            powns[player] = next_powns

            next_scores = scores[player]
            for pos in range(10):
                for d in range(len(dirac_dice[0])):
                    score = min(20, pos + dirac_dice[0][d] - 1)
                    next_scores[score] += dirac_dice[1][d]
            scores[player] = next_scores

            if scores[player][20] > 0:
                winner = player
                break

    return scores[winner][20]


if __name__ == "__main__":
    ret = part1(4, 8, 1000)
    print("Part 1  {:d} (739785)".format(ret))

    ret = part1(7, 1, 1000)
    print("Part 1  {:} (684495)".format(ret))

    ret = part2(4, 8)
    print("Part 2  {:d} (444356092776315)".format(ret))
