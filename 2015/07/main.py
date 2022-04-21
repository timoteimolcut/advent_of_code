
"""
assembly interpretor

special cases: asignare ... 123 -> x
               NOT ... NOT e -> f
binary: AND ... x AND y -> z
        OR
        LSHIFT ... p LSHIFT 2 -> q
        RSHIFT

"""

from calendar import firstweekday


f = open('input.txt', 'r')
assembly = f.read()
f.close()

assembly = assembly.split('\n')
assembly.pop()

signal_dict = {}


def assign(x):
    print(f'enter assign, {x}')
    global signal_dict
    if x.isnumeric():
        print(x)
        return int(x)
    else:
        print('call assign again')
        return assign(signal_dict[x])

def not_(x):
    print(f'enter not, {x}')
    global signal_dict
    if x.isnumeric():
        return ~int(x)
    else:
        return not_(signal_dict[x])

def and_(a, b):
    print(f'enter and, {a} {b}')
    global signal_dict
    if a.isnumeric():
        if b.isnumeric():
            return int(a) & int(b)
        else:
            return and_(a, signal_dict[(b)])
    elif b.isnumeric():
        return and_(signal_dict[(a)], b)
    else:
        return and_(signal_dict[(a)], signal_dict[(b)])

def or_(a, b):
    print(f'enter or, {a} {b}')
    global signal_dict
    if a.isnumeric():
        if b.isnumeric():
            return int(a) | int(b)
        else:
            return or_(a, signal_dict[(b)])
    elif b.isnumeric():
        return or_(signal_dict[(a)], b)
    else:
        return or_(signal_dict[(a)], signal_dict[(b)])

def lshift(a, b):
    print(f'enter lshift, {a} {b}')
    global signal_dict
    if a.isnumeric():
        if b.isnumeric():
            return int(a) << int(b)
        else:
            return lshift(a, signal_dict[(b)])
    elif b.isnumeric():
        return lshift(signal_dict[(a)], b)
    else:
        return lshift(signal_dict[(a)], signal_dict[(b)])

def rshift(a, b):
    print(f'enter rshift, {a} {b}')
    global signal_dict
    if a.isnumeric():
        if b.isnumeric():
            return int(a) >> int(b)
        else:
            return rshift(a, signal_dict[(b)])
    elif b.isnumeric():
        return rshift(signal_dict[(a)], b)
    else:
        return rshift(signal_dict[(a)], signal_dict[(b)])

class BinaryTreeNode:
    def __init__(self):
        self.name = None
        self.data = None
        self.op = None
        self.leftChild = None
        self.rightChild = None
    def setName(self, name):
        self.name = name
    def setData(self, data): # valoarea finala a semnalului
        self.data = data
    def setOp(self, op):
        self.op = op
    def addLeft(self, node):
        self.leftChild = node
    def addRight(self, node):
        self.rightChild = node





# for k, v in signal_dict.items():
#     tree.setName() # numele variabilei/cheia din arbore
#     tree.addLeft() 
#     tree.addRight()


def parse_assembly(assembly):
    global signal_dict
    for i in assembly:
        i = i.split(' ')        
        if i[1] == '->': 
            signal_dict[i[2]] = ['assign', i[0]]
        elif i[2] == '->':
            signal_dict[i[3]] = ['not', i[1]] # not_(i[1])
        elif i[3] == '->':
            if i[1] == 'AND':
                signal_dict[i[4]] = ['and', i[0], i[2]]  #and_(i[0], i[2])
            elif i[1] == 'OR':
                signal_dict[i[4]] = ['or', i[0], i[2]] # or_(i[0], i[2])
            elif i[1] == 'LSHIFT':
                signal_dict[i[4]] = ['lshift', i[0], i[2]] # lshift(i[0], i[2])
            elif i[1] == 'RSHIFT':
                signal_dict[i[4]] = ['rshift', i[0], i[2]] # rshift(i[0], i[2])
        else:
            raise Exception('wrong assembly')


def eval(expr):
    global signal_dict
    if not isinstance(expr, list):
        if isinstance(expr, int) or expr.isnumeric():
            # print(f'{expr} is numeric')
            return int(expr)
        else:
            # print(f'{expr} is literal')
            return eval(signal_dict[expr])
    else:
        # print(f'{expr} is a list')
        if expr[0] == 'assign':
            val = eval(expr[1])
            return val
        elif expr[0] == 'not':
            val = eval(expr[1])
            return ~val
        elif expr[0] == 'and':
            val1 = eval(expr[1])
            val2 = eval(expr[2])
            return val1 & val2
        elif expr[0] == 'or':
            val1 = eval(expr[1])
            val2 = eval(expr[2])
            return val1 | val2
        elif expr[0] == 'lshift':
            val1 = eval(expr[1])
            val2 = eval(expr[2])
            return val1 << val2
        elif expr[0] == 'rshift':
            val1 = eval(expr[1])
            val2 = eval(expr[2])
            return val1 >> val2
        else:
            raise Exception('somethin wrong')



parse_assembly(assembly)


# print(signal_dict[])

firstKey = list(signal_dict.items())[0][0]
# print(firstKey)
# print(signal_dict[firstKey][0])


def createTree(key):
    global signal_dict
    # print(key)
    tree = BinaryTreeNode()
    tree.setName(key)
    if key.isnumeric():
        return tree
    # print(signal_dict[key][0], signal_dict[key][1], signal_dict[key][2])

    tree.setOp(signal_dict[key][0])
    tree.addLeft(createTree(signal_dict[key][1]))
    if len(signal_dict[key]) == 3:
        tree.addRight(createTree(signal_dict[key][2]))
    return tree

def printKey(tree, key):
    if tree == None:
        return
    
    print(tree.name == key)
    # if tree != None and tree.name == key:    
    #     print('here: ', tree.data)
    #     return
    printKey(tree.leftChild, key)
    printKey(tree.rightChild, key)
    

tree = createTree(firstKey)



def evaluate_tree(tree):
    if tree == None:
        return
    if tree.op == 'assign':
        tree.setData(int(tree.leftChild.name))
    evaluate_tree(tree.leftChild)
    evaluate_tree(tree.rightChild)


evaluate_tree(tree)

printKey(tree, 'a')


# tree = BinaryTreeNode()
# tree.setName()
# left = BinaryTreeNode()
# tree.addLeft(left)
# right = BinaryTreeNode()
# tree.addRight(left)



# print(list(signal_dict.items())[0][0])



# print('signal dictionary')
# for k, v in signal_dict.items():
    # print(f'{k}: {v}')
    # signal_dict[k] = eval(v)
    # print(f'{k} {signal_dict[k]}')

