from tqdm import tqdm


#############   0
#12345678901#   1
###B#C#B#D###   2
  #A#D#C#A#     3
  #########

def day23_next(s, cost):
    amphi_costs = { 'A':1, 'B':10, 'C':100, 'D':1000 }
    amphi_rooms = { 'A':3, 'B':5, 'C':7, 'D':9 }
    all_moves = []

    for l, line in enumerate(s):
        if l not in (0, len(s)-1): # Skip 1st and last line of status s
            for c, col in enumerate(line):
                if col in "ABCD":
                    if l==1:        # Managing hallway
                        t = amphi_rooms[col]    # We want to enter Dorm t
                        if all([ s[1][i] == '.' if i!=c else True for i in range(min(t,c), max(t,c)) ]) and all([ s[u][t] in ('.',col) for u in range(2,len(s)-1)]) :
                            u = 1
                            while s[u+1][t] == '.':
                                u += 1
                            if u>1 : # Got room in Dorm
                                new_1 = s[1][0:c] + '.' + s[1][c+1:]
                                new_u = s[u][0:t] + col + s[u][t+1:]                        
                                all_moves.append(([ s[i] if i not in (1,u) else new_1 if i==1 else new_u for i in range(len(s))], cost+(u-1+abs(c-t))*amphi_costs[col]))                        
                    else: # Managing Dorm 
                        if all([ s[v][c]=='.' for v in range(1,l) ]):                 
                            for t in range(1,c): # exit left
                                if t not in (3,5,7,9) and all([ s[1][i] == '.' for i in range(t,c) ]) :
                                    new_1 = s[1][0:t] + col + s[1][t+1:]
                                    new_l = s[l][0:c] + '.' + s[l][c+1:]                        
                                    all_moves.append(([ s[i] if i not in (1,l) else new_1 if i==1 else new_l for i in range(len(s))], cost+(l-1+abs(c-t))*amphi_costs[col]))
                            for t in range(c,12): # exit right
                                if t not in (3,5,7,9) and all([ s[1][i] == '.' for i in range(c,t+1) ]) :
                                    new_1 = s[1][0:t] + col + s[1][t+1:]
                                    new_l = s[l][0:c] + '.' + s[l][c+1:]                        
                                    all_moves.append(([ s[i] if i not in (1,l) else new_1 if i==1 else new_l for i in range(len(s))], cost+(l-1+abs(t-c))*amphi_costs[col]))
    return all_moves


def day23_part1(s, target):
    tk = "".join( [target[i] for i in range(1,len(target)-1) ] )
    todo = [ s ]
    k = "".join( [s[i] for i in range(1,len(s)-1) ] )
    done  = { k: 0 }
    
    with tqdm() as bar:
        while len(todo)>0:
            bar.total = len(todo)+len(done)
            d = todo.pop(0)
            k = "".join( [d[i] for i in range(1,len(d)-1) ] )
            cost = done[k]
            bar.update(1)
            if k != tk:                 
                for e in day23_next(d, cost):                    
                    ek = "".join( [e[0][i] for i in range(1,len(d)-1) ] )
                    if ek not in done:
                        done[ek] = e[1]
                        todo.append(e[0])
                    else:
                        done[ek] = min(e[1], done[ek])
    return done[tk]

if __name__ == "__main__":

    sample1 = [   "#############", 
            "#...........#",
            "###B#C#B#D###",
            "  #A#D#C#A#",
            "  #########"   ]
    sample2 = [   "#############", 
            "#...........#",
            "###B#C#B#D###",
            "  #D#C#B#A#",
            "  #D#B#A#C#",
            "  #A#D#C#A#",
            "  #########"   ]
    target1 = [  "#############", 
                 "#...........#",
                 "###A#B#C#D###",
                 "  #A#B#C#D#",
                 "  #########"   ]
    target2 = [  "#############", 
                 "#...........#",
                 "###A#B#C#D###",
                 "  #A#B#C#D#",
                 "  #A#B#C#D#",
                 "  #A#B#C#D#",
                 "  #########"   ]
    part1 = [   "#############",
                "#...........#",
                "###A#C#B#A###",
                "  #D#D#B#C#",
                "  #########" ]
    part2 = [   "#############",
                "#...........#",
                "###A#C#B#A###",
                "  #D#C#B#A#",
                "  #D#B#A#C#",
                "  #D#D#B#C#",
                "  #########" ]

    ret = day23_part1(sample1, target1)
    print("Sample1 {:d} (12521)".format(ret))
    ret = day23_part1(part1, target1)
    print("Part 1  {:d} (18195)".format(ret))

    ret = day23_part1(sample2, target2)
    print("Sample2 {:d} (44169)".format(ret))
    ret = day23_part1(part2, target2)
    print("Part 2  {:d} (50265)".format(ret))
