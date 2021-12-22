from tqdm import tqdm
from copy import deepcopy


explode_samples = [ '[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]',
                    '[7,[6,[5,[4,[3,2]]]]]',
                    '[[[[[9,8],1],2],3],4]',
                    '[[6,[5,[4,[3,2]]]],1]' ]


magnitude_samples = [   '[[1,2],[[3,4],5]]',
                        '[[[[0,7],4],[[7,8],[6,0]]],[8,1]]',
                        '[[[[1,1],[2,2]],[3,3]],[4,4]]',
                        '[[[[3,0],[5,3]],[4,4]],[5,5]]',
                        '[[[[5,0],[7,4]],[5,5]],[6,6]]',
                        '[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]' ]

homework_sample = [     '[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]',
                        '[[[5,[2,8]],4],[5,[[9,9],0]]]',
                        '[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]',
                        '[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]',
                        '[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]',
                        '[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]',
                        '[[[[5,4],[7,7]],8],[[8,3],8]]',
                        '[[9,3],[[9,9],[6,[4,9]]]]',
                        '[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]',
                        '[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]' ]

def fish_explode_1(father, depth):
    ret = None
    if depth == 0:
        for i in range(len(father)):
            if isinstance(father[i], list) and ret == None:
                ret = deepcopy(father[i])
                father[i] = None
    for i in range(len(father)):
        if isinstance(father[i], list) and ret == None:
            ret = fish_explode_1(father[i], depth-1)        
    return ret


def fish_explode(father, depth):
    elem = fish_explode_1(father, depth)
    if elem != None:
        s = str(father)
        k = s.index('None')
        if k!=-1:
            sleft = s[0:k]
            i = 0
            while i<len(sleft) and sleft[-i].isdigit() == False:
                i += 1
            j = i
            while j<len(sleft) and sleft[-j].isdigit() == True:
                j += 1
            if j < len(sleft):
                v = sleft[-j+1:-i+1]
                sleft = sleft[0:1-j] + str(int(v)+elem[0]) + sleft[-(i-1):]
            sright = s[k+4:]
            i = 0
            while i<len(sright) and sright[i].isdigit() == False:
                i += 1
            j = i
            while j<len(sright) and sright[j].isdigit() == True:
                j += 1
            if j < len(sright):
                v = sright[i:j]
                sright = sright[0:i] + str(int(v)+elem[1]) + sright[j:]
            s = sleft + '0' + sright
        tmp = eval(s)
        for i in range(len(tmp)): father[i] = tmp [i]
    return elem

def fish_split(father):
    ret = False
    for i in range(len(father)):
        if isinstance(father[i], list) and ret == False:
            ret = fish_split(father[i])
        else:
            if father[i]>9 and ret == False:
                father[i] = [ father[i]//2, (father[i]+1)//2 ]
                ret = True
        if ret == True: return ret
    return ret


def fish_reduce(val):
    elem=fish_explode(val, 3)
    while elem != None:
        elem=fish_explode(val, 3)
    while (fish_split(val) == True):
        elem=fish_explode(val, 3)
        while elem != None:
            elem=fish_explode(val, 3)
    return val


def fish_addition(arg1, arg2):
    val = [ arg1, arg2 ]
    return fish_reduce(val)


def fish_magnitude(father):
    ret0, ret1 = 0, 0
    if isinstance(father[0], list):
        ret0 = 3 * fish_magnitude(father[0])
    else:
        ret0 = 3 * father[0]
    if isinstance(father[1], list):
        ret1 = 2 * fish_magnitude(father[1])
    else:
        ret1 = 2 * father[1]

    return ret0 + ret1


def part1(numbers):
    cpt = None
    for i in range(len(numbers)):
        if i == 0:
            cpt = eval(numbers[i])
        else:
            cpt = fish_addition(cpt, eval(numbers[i]))
    mag = fish_magnitude(cpt)
    return mag

def part2(numbers):
    results = {}
    for i in tqdm(range(len(numbers))):
        for j in range(len(numbers)):
            if i != j:
                cpt = fish_addition(eval(numbers[i]), eval(numbers[j]))
                mag = fish_magnitude(cpt)
                results[(i,j)] = mag
    m = max(results.values())
    k = list(results.keys())[list(results.values()).index(m)]
    print(numbers[k[0]])
    print('+')
    print(numbers[k[1]])
    return m




if __name__ == "__main__":
    
    #for es in explode_samples:
    #    val = eval(es)
    #    ret = fish_reduce(val)
    #    print(ret)
    #print("Part 1 {:s} ([[[[0,9],2],3],4])".format(ret))

    #for es in magnitude_samples:
    #    val = eval(es)
    #    ret = fish_magnitude(val)
    #    print("Magnitude {:d}".format(ret))


    p2_sample = [  '[[[6,[2,9]],[0,7]],[8,[[7,7],[9,9]]]]',
            '[[[[8,7],4],8],[[[8,9],5],[6,[2,7]]]]' ]

    ret = part1(p2_sample)
    print("Part 1 P2 magnitude {:d} (4812)".format(ret))        

    ret = part1(homework_sample)
    print("Part 1 Sample magnitude {:d} (4140)".format(ret))
    ret = part2(homework_sample)
    print("Part 2 Sample max magnitude {:d} (3993)".format(ret))

    with open('day18-s.txt') as f:        
        part1_sample = f.readlines()
        ret = part1(part1_sample)
        print("Part 1 magnitude {:d} (3051)".format(ret))

        ret = part2(part1_sample)
        print("Part 2 max magnitude {:d} (4812)".format(ret))

