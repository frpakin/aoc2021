from copy import deepcopy


explode_samples = [ '[[[[[9,8],1],2],3],4]',
                    '[7,[6,[5,[4,[3,2]]]]]',
                    '[[6,[5,[4,[3,2]]]],1]',
                    '[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]' ]


def addleft(father, val):
    if isinstance(father[0], list):
        return addleft(father[0], val)
    else:
        father[0] += val[0]
        val[0] = None
    return father

def addright(father, val):
    if isinstance(father[1], list):
        return addleft(father[1], val)
    else:
        father[1] += val[1]
        val[1] = None
    return father


def fish_explode_1(father, depth):
    ret = None
    if depth == 0:
        for i in range(len(father)):
            if isinstance(father[i], list):
                ret = deepcopy(father[i])
                father[i] = None
    for i in range(len(father)):
        if isinstance(father[i], list):
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
                sleft = sleft[0:-j] + str(int(v)+elem[0]) + sleft[-(i-1):]
            sright = s[k+4:]
            i = 0
            while i<len(sright) and sright[i].isdigit() == False:
                i += 1
            j = i
            while j<len(sright) and sright[j].isdigit() == True:
                j += 1
            if j < len(sright):
                v = sright[i:j]
                sright = sright[0:i+1] + str(int(v)+elem[1]) + sright[j+1:]
            s = sleft + '0' + sright
    father = eval(s)
    return father

def fish_split(father):
    ret = False
    for i in range(len(father)):
        if isinstance(father[i], list):
            ret = fish_split(father[i])
        else:
            if father[i]>9:
                father[i] = [ father[i]//2, (father[i]+1)//2 ]
                ret = True
        if ret == True: return ret
    return ret


def fish_reduce(val):
    print('---------------------------------------------')
    print(val)
    val=fish_explode(val, 3)
    print(val)
    while (fish_split(val) == True):
        print(val)
        e=fish_explode(val, 3)
        print(val)
    return val


def fish_addition(arg1, arg2):
    val = [ arg1, arg2 ]
    return fish_reduce(val)


def part1(numbers):
    cpt = None
    for i in range(len(numbers)):
        if i == 0:
            cpt = eval(numbers[i])
        else:
            cpt = fish_addition(cpt, eval(numbers[i]))
    return cpt


if __name__ == "__main__":
    

    for es in explode_samples:
        val = eval(es)
        ret = fish_reduce(val)
        print(ret)
    #print("Part 1 {:s} ([[[[0,9],2],3],4])".format(ret))

    numbers = [ '[[[[4,3],4],4],[7,[[8,4],9]]]', '[1,1]' ]
    ret = part1(numbers)

