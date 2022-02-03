# Part 2 only

def boardpos(pos, roll, board_size=10):
    off = roll % board_size
    if (pos + off) > 10:
        ret =  (pos + off) % board_size
    else :
        ret = pos + off
    return ret

def day21_run(p1, p2):
    dirac_dice = { 3:1, 4:3, 5:6, 6:7, 7:6, 8:3, 9:1 }
    p1_tt_win, p2_tt_win = 0, 0
    old_universe = { (p1, 0, p2, 0): 1 }
    while len(old_universe) > 0:
        universe1 = {}
        for u in old_universe.keys():
            for d in dirac_dice.keys():
                new_pos = boardpos(u[0], d)
                new_score = u[1] + new_pos
                key = (new_pos, new_score, u[2], u[3])
                prev = universe1.get(key, 0)
                nb_universe = prev + old_universe[u]*dirac_dice[d]
                if new_score >= 21:
                    p1_tt_win += nb_universe
                else:
                    universe1.update( { key: nb_universe } )
        old_universe = universe1
        universe2 = {}
        for u in old_universe.keys():
            for d in dirac_dice.keys():
                new_pos = boardpos(u[2], d)
                new_score = u[3] + new_pos
                key = (u[0], u[1], new_pos, new_score)
                prev = universe2.get(key, 0)
                nb_universe = prev + old_universe[u]*dirac_dice[d]
                if new_score >= 21:
                    p2_tt_win += nb_universe
                else:
                    universe2.update( { key: nb_universe } )
        old_universe = universe2
    return max(p1_tt_win, p2_tt_win)

if __name__ == '__main__':
    ret = day21_run(4, 8)
    print("Got {} (444356092776315)".format(ret))
    ret = day21_run(7, 1)
    print("Got {} (152587196649184)".format(ret))

    