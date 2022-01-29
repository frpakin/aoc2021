from tqdm import trange

def day24_gen(fname_in='day24.txt', fname_out='day24_gen.py'):
    with open(fname_in) as f:
        with open(fname_out, mode='w') as g:
            lexed = [ l.split() for l in f.read().split('\n') ]
            coded = []
            for c in lexed:
                if c[0] == 'inp':
                    trans = "    {} = inputs.pop()".format(c[1])
                elif c[0] == 'add':
                    trans = "    {0} += {1}".format(c[1], c[2])
                elif c[0] == 'mul':
                    trans = "    {0} *= {1}".format(c[1], c[2])
                elif c[0] == 'div':
                    trans = "    {0} = {0}//{1}".format(c[1], c[2])
                elif c[0] == 'mod':
                    trans = "    {0} = {0}%{1}".format(c[1], c[2])
                elif c[0] == 'eql':
                    trans = "    {0} = 1 if {0}=={1} else 0".format(c[1], c[2])
                coded.append(trans)
            g.write('\n'.join(coded))


def day24_load(fname_in='day24.txt'):
    ret = []
    n = 0
    with open(fname_in) as f:
        lexed = [ l.split() for l in f.read().split('\n') ]
        coded = []
        for c in lexed:
            if c[0] == 'inp':
                if len(coded) >0:
                    comp = compile('\n'.join(coded), "day24_stage_{:02d}.py".format(n), 'exec')
                    ret.append(comp)
                    coded = []
                    n += 1
                trans = "{} = inputs".format(c[1])
            elif c[0] == 'add':
                trans = "{0} += {1}".format(c[1], c[2])
            elif c[0] == 'mul':
                trans = "{0} *= {1}".format(c[1], c[2])
            elif c[0] == 'div':
                trans = "{0} = {0}//{1}".format(c[1], c[2])
            elif c[0] == 'mod':
                trans = "{0} = {0}%{1}".format(c[1], c[2])
            elif c[0] == 'eql':
                trans = "{0} = 1 if {0}=={1} else 0".format(c[1], c[2])
            coded.append(trans)
        if len(coded) >0:
            comp = compile('\n'.join(coded), "day24_stage_{:2d}.py".format(n), 'exec')
            ret.append(comp)
    return ret


def day24_sub(code, i, v, s=(0, 0, 0, 0)):
    global inputs, w, x, y, z
    w, x, y, z = s
    inputs = v
    exec(code[i])
    _locals = locals()
    return _locals['w'], _locals['x'], _locals['y'], _locals['z']


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

def day24_run(code):    # Part 2
    stages = [ {(0, 0, 0, 0): 0} ]
    for i in trange(len(code)):
        results = {}
        for state in stages[i].keys():
            for v in [9,8,7,6,5,4,3,2,1]:
                results[ day24_sub(code, i, v, state) ] = stages[i][state] *10 + v
        stages.append(results)
       
    ret = []
    for l in stages[-1].keys():
        if l[3] == 0:
            print("{0} -> {1}".format(l, stages[-1][l]))
            ret.append(stages[-1][l])
    ret.sort()
    return ret


if __name__ == '__main__':
    inputs, w, x, y, z = 0, 0, 0, 0, 0
    code = day24_load()
    ret = day24_run(code)
    print(min(ret))