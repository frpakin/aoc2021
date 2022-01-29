
from itertools import product
from unittest import result
from tqdm import trange    


def alu_run(args)    :
    inputs = list(args)
    w, x, y, z = 0, 0, 0, 0
    w = inputs.pop()
    w = inputs.pop()
    x = 1
    y = 26
    z = 0
    y = 0
    y += w
    y += 9
    y *= x
    z += y
    w = inputs.pop()
    y = 26
    z *= y
    y = 0
    y += w
    y += 8
    y *= x
    z += y
    w = inputs.pop()
    x *= 0
    x += z
    x = x%26
    z = z//26
    x += -8
    x = 1 if x==w else 0
    x = 1 if x==0 else 0
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 3
    y *= x
    z += y
    w = inputs.pop()
    x *= 0
    x += z
    x = x%26
    z = z//1
    x += 11
    x = 1 if x==w else 0
    x = 1 if x==0 else 0
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 0
    y *= x
    z += y
    w = inputs.pop()
    x *= 0
    x += z
    x = x%26
    z = z//1
    x += 11
    x = 1 if x==w else 0
    x = 1 if x==0 else 0
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 11
    y *= x
    z += y
    w = inputs.pop()
    x *= 0
    x += z
    x = x%26
    z = z//1
    x += 14
    x = 1 if x==w else 0
    x = 1 if x==0 else 0
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 10
    y *= x
    z += y
    w = inputs.pop()
    x *= 0
    x += z
    x = x%26
    z = z//26
    x += -11
    x = 1 if x==w else 0
    x = 1 if x==0 else 0
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 13
    y *= x
    z += y
    w = inputs.pop()
    x *= 0
    x += z
    x = x%26
    z = z//1
    x += 14
    x = 1 if x==w else 0
    x = 1 if x==0 else 0
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 3
    y *= x
    z += y
    w = inputs.pop()
    x *= 0
    x += z
    x = x%26
    z = z//26
    x += -1
    x = 1 if x==w else 0
    x = 1 if x==0 else 0
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 10
    y *= x
    z += y
    w = inputs.pop()
    x *= 0
    x += z
    x = x%26
    z = z//26
    x += -8
    x = 1 if x==w else 0
    x = 1 if x==0 else 0
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 10
    y *= x
    z += y
    w = inputs.pop()
    x *= 0
    x += z
    x = x%26
    z = z//26
    x += -5
    x = 1 if x==w else 0
    x = 1 if x==0 else 0
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 14
    y *= x
    z += y
    w = inputs.pop()
    x *= 0
    x += z
    x = x%26
    z = z//26
    x += -16
    x = 1 if x==w else 0
    x = 1 if x==0 else 0
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 6
    y *= x
    z += y
    w = inputs.pop()
    x *= 0
    x += z
    x = x%26
    z = z//26
    x += -6
    x = 1 if x==w else 0
    x = 1 if x==0 else 0
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 5
    y *= x
    z += y
    if z == 0:
        print(args)
    return z

def dummy():
    for n in trange(99999999999999, 0, -1):
        inputs = [ int(c) for c in '{:d}'.format(n)]
        if alu_run(inputs) == 0:
            print(n)
            break




values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l = product(values, repeat=14)

#import multiprocessing
#with multiprocessing.Pool(24) as p:
#    data = p.map(alu_run, l)


import concurrent.futures
#with concurrent.futures.ThreadPoolExecutor(max_workers=2) as p:
#    results = p.map(alu_run, l)
#    finals = []
#    for ret in results:
#        finals.append(ret)

with concurrent.futures.ThreadPoolExecutor(max_workers=16) as executor:
    result_futures = list(map(lambda x: executor.submit(alu_run, x), l))
    for future in concurrent.futures.as_completed(result_futures):
        try:
            print('resutl is', future.result())
        except Exception as e:
            print('e is', e, type(e))

