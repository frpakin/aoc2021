from copy import deepcopy


def explode(elem, father, depth):
    if depth == 0:
        for i in range(len(father)):
            if father[i] == elem:
                father[i] = 0
"""  """        return deepcopy(elem)
    else:
        for a in elem:
            if isinstance(a, list):
                e = explode(a, elem, depth-1)
                for i in range(len(elem)):
                    if e[i] != None and not isinstance(elem[i], list):
                        elem[i] += e[i]
                        e[i] = None
                return e


def reduce(val):
    for elem in val:
        if isinstance(elem, list):
            e=explode(elem, val, 3)

    return 0


def addition(arg1, arg2):
    val = [ arg1, arg2]
    return reduce(val)


def part1(numbers):
    return 1


if __name__ == "__main__":
    
    val = eval('[[[[[9,8],1],2],3],4]')
    ret = reduce(val)
    print("Part 1 {:d} (45)".format(ret))
