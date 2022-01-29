from lark import Lark
from lark import Transformer


grammar = r"""
    prg: cmd (NEWLINE cmd)*
    cmd: ops value value*
    ops: WORD
    value: WORD | SIGNED_INT
         
    %import common.WORD
    %import common.SIGNED_INT
    %import common.WS
    %import common.NEWLINE
    %ignore WS
    """


class TreeToM(Transformer):
    def ops(self, s):
        return s[0]

    def value(self, s):
        return int(s[0][0]) if s[0].type == 'SIGNED_INT' else s[0][0]
    
    def prg(self, items):
        return list(items)
    
    def cmd(self, key_value):
        return key_value



parser = Lark(grammar, start='prg', parser='lalr', transformer=TreeToM())

if __name__ == '__main__':
    with open('day24.txt') as f:
        tree = parser.parse(f.read())
        ret =  TreeToM().transform(tree)
        print("Done")