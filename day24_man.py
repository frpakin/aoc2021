from tqdm import trange, tqdm


def alu_stage_00(w, x, y, z, inputs) :
    w = inputs
    x *= 0
    x += z
    x = x%26
    #z = z//1
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
    y += 12
    y *= x
    z += y
    return w, x, y, z

def alu_stage_01(w, x, y, z, inputs) :
    w = inputs
    x *= 0
    x += z
    x = x%26
    #z = z//1
    x += 10
    x = 1 if x==w else 0
    x = 1 if x==0 else 0
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 9
    y *= x
    z += y
    return w, x, y, z


def alu_stage_02(w, x, y, z, inputs) :    
    w = inputs
    x *= 0
    x += z
    x = x%26
    z = z//1
    x += 13
    x = 1 if x==w else 0
    x = 1 if x==0 else 0
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 8
    y *= x
    z += y
    return w, x, y, z


def alu_stage_03(w, x, y, z, inputs) :    
    w = inputs
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
    return w, x, y, z


def alu_stage_04(w, x, y, z, inputs) :        
    w = inputs
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
    return w, x, y, z


def alu_stage_05(w, x, y, z, inputs) :    
    w = inputs
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
    return w, x, y, z


def alu_stage_06(w, x, y, z, inputs) :        
    w = inputs
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
    return w, x, y, z


def alu_stage_07(w, x, y, z, inputs) :    
    w = inputs
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
    return w, x, y, z


def alu_stage_08(w, x, y, z, inputs) :        
    w = inputs
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
    return w, x, y, z


def alu_stage_09(w, x, y, z, inputs) :        
    w = inputs
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
    return w, x, y, z


def alu_stage_10(w, x, y, z, inputs) :        
    w = inputs
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
    return w, x, y, z


def alu_stage_11(w, x, y, z, inputs) :        
    w = inputs
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
    return w, x, y, z


def alu_stage_12(w, x, y, z, inputs) :    
    w = inputs
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
    return w, x, y, z


def alu_stage_13(w, x, y, z, inputs) :        
    w = inputs
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
    return w, x, y, z


def day24_load():
    return [ alu_stage_00, alu_stage_01, alu_stage_02, alu_stage_03, alu_stage_04, alu_stage_05, alu_stage_06, alu_stage_07, alu_stage_08, alu_stage_09, alu_stage_10, alu_stage_11, alu_stage_12, alu_stage_13 ]


def day24_sub(code, i, v, s=(0, 0, 0, 0)):
    return code[i](*s, v)


def day24_run_part1(code):
    stages = [ {(0, 0, 0, 0): 0} ]
    for i in trange(len(code)):
        results = {}
        for state in stages[i].keys():
            for v in [1,2,3,4,5,6,7,8,9]:
                results[ day24_sub(code, i, v, state) ] = stages[i][state] *10 + v
        stages.append(results)
       
    ret = []
    for l in stages[-1].keys():
        if l[3] == 0:
            print("{0} -> {1}".format(l, stages[-1][l]))
            ret.append(stages[-1][l])
    ret.sort()
    return ret


import concurrent.futures
#with concurrent.futures.ThreadPoolExecutor(max_workers=2) as p:
#    results = p.map(alu_run, l)
#    finals = []
#    for ret in results:
#        finals.append(ret)


def alu_run_thread(i, v, stages):
    result ={}
    for state in stages[i].keys():
        result[ day24_sub(code, i, v, state) ] = stages[i][state] *10 + v
    return result


def day24_run(code):    # Part 2
    stages = [ {(0, 0, 0, 0): 0} ]
    with concurrent.futures.ProcessPoolExecutor(max_workers=9) as executor:
        for i in range(len(code)):
            results = {}
            result_futures = []
            with tqdm(total=9) as bar:
                for v in [9,8,7,6,5,4,3,2,1]:
                    result_futures.append(executor.submit(alu_run_thread, i, v, stages))
                concurrent.futures.wait(result_futures)                
                for future in result_futures:
                    try:                        
                        results.update(future.result())
                        bar.update(1)
                    except Exception as e:
                        print('e is', e, type(e))
                stages.append(results)
    ret = [ stages[-1][k] for k in stages[-1].keys() if k[3] == 0 ]    
    ret.sort()
    return ret


if __name__ == '__main__':
    code = day24_load()
    ret = day24_run(code)
    print(min(ret))
