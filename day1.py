with open("day1-sample.txt") as f:
    DATA = [ list(map(int, "199 200 208 210 200 207 240 269 260 263".split())),
             [ int(x.strip()) for x in f ]    ]

def pb1(data):
    cpt = 0
    for i in range(1,len(data)):
        if data[i] > data[i-1]:
            cpt += 1
    return cpt

def pb2(data):
    d2 = []
    for i in range(2,len(data)):
        d2.append(data[i]+data[i-1]+data[i-2])
    return pb1(d2)

if __name__ == "__main__":
    ret = pb1(DATA[0])
    print("Ret=%d" % ret)
    ret = pb1(DATA[1])
    print("Ret=%d" % ret)

    ret = pb2(DATA[0])
    print("Ret=%d" % ret)

    ret = pb2(DATA[1])
    print("Ret=%d" % ret)
