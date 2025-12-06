import timeit
import math

def p1(lines):
    for line in lines:
        monkey,op = line.split(":")
        op = op.strip()
        # number
        if len(op) < 10:
            ret = op
        else:
            ret = op[:4] + "()" + op[4:11] + "()"
        func = f"global {monkey}\ndef {monkey}():\n\treturn {ret}\n"
        exec(func)

    return int(root())

def p1_alt(lines):
    functs = {}
    for line in lines:
        monkey,op = line.split(":")
        op = op.strip()     
        functs[monkey] = op
    func = resolve(functs, "root")
    #print(func)
    return int(eval(func))


class Node:
    
    is_leaf = False
    val = None
    op = None
    item1 = None
    item2 = None
    
    def __init__(self, val = None):
        self.val = val
        if val != None: 
            self.is_leaf = True   
        
    def __str__(self):
        if self.is_leaf == True:
            return str(self.val)
        else:
            return f"({str(self.item1)}{self.op}{str(self.item2)})"
        
    def fill_node(self, op, item1, item2):
        self.op = op
        self.item1 = item1
        self.item2 = item2
    
    def eval_node(self):
        if self.is_leaf:
            return self.val
        else:
            match self.op:
                case "+":
                    return self.item1.eval_node() + self.item2.eval_node()
                case "-":
                    return self.item1.eval_node() - self.item2.eval_node()
                case "*":
                    return self.item1.eval_node() * self.item2.eval_node()
                case "/":
                    return self.item1.eval_node() / self.item2.eval_node()
                case _:
                    return "ERROR"
    def collapse_node(self):
        if self.is_leaf:
            if self.val != "X":
                return True
            else:
                return False
        else:
            #print(f"self: {self}")
            #print(f"collapsing item1: {self.item1}")
            item1_collapsed = self.item1.collapse_node()
            #print(f"collapsing item2: {self.item2}")
            item2_collapsed = self.item2.collapse_node()
            if item1_collapsed and item2_collapsed:
                # This node is now a leaf, update val
                match self.op:
                    case "+":
                        self.val = self.item1.val + self.item2.val
                    case "-":
                        self.val = self.item1.val - self.item2.val
                    case "*":
                        self.val = self.item1.val * self.item2.val
                    case "/":
                        self.val = self.item1.val / self.item2.val
                    case _:
                        assert(False)
                self.is_leaf = True
                return True
            else:
                return False
    def reverse_tree(self, val = None):
        #print(f"Val: {val} op: {self.op} item1: {self.item1}, item2: {self.item2}")
        if self.val == "X":
            return val
        #starting at root, get value of collapsed tree
        if val == None:
            if self.item1.is_leaf:
                return self.item2.reverse_tree(self.item1.val)
            if self.item2.is_leaf:
                return self.item1.reverse_tree(self.item2.val)            
            assert(False)  
        if self.item2.is_leaf:
            match self.op:
                case "+":
                    #print(f"{self.item1} = {val} - {self.item2.val}")
                    return self.item1.reverse_tree( val - self.item2.val)
                case "-":
                    #print(f"{self.item1} = {val} + {self.item2.val}")
                    return self.item1.reverse_tree( val + self.item2.val)
                case "*":
                    #print(f"{self.item1} = {val} / {self.item2.val}")
                    return self.item1.reverse_tree( val / self.item2.val)
                case "/":
                    #print(f"{self.item1} = {val} * {self.item2.val}")
                    return self.item1.reverse_tree( val * self.item2.val)
                case _:
                    assert(False)
        if self.item1.is_leaf:
            match self.op:
                case "+":
                    #print(f"{self.item2} = {val} - {self.item1.val}")
                    return self.item2.reverse_tree( val - self.item1.val )
                case "-":
                    #print(f"{self.item2} = {self.item1.val} - {val}")
                    return self.item2.reverse_tree( self.item1.val - val )
                case "*":
                    #print(f"{self.item2} = {val} / {self.item1.val}")
                    return self.item2.reverse_tree( val / self.item1.val)
                case "/":
                    assert(False)
                    #print(f"{self.item2} = {val} * {self.item1.val}")
                    return self.item2.reverse_tree( val * self.item1.val)
                case _:
                    assert(False)        
        assert(False)

def p1_tree(lines):
    items = {}
    #create prototype nodes
    for line in lines:
        monkey,expr = line.split(":")
        if len(expr) < 10:
            items[monkey] = Node(int(expr))
        else:
            items[monkey] = Node()
            
    for line in lines:
        monkey,expr = line.split(":")
        if len(expr) > 10:
            item1,op,item2 = expr.split()
            items[monkey].fill_node(op, items[item1], items[item2])

    items["root"].collapse_node()
    return items["root"]


def p2_tree(lines):

    items = {}
    #create prototype nodes
    for line in lines:
        monkey,expr = line.split(":")
        if monkey == "humn":
            items[monkey] = Node("X")
        elif len(expr) < 10:
            items[monkey] = Node(int(expr))
        else:
            items[monkey] = Node()
            
    for line in lines:
        monkey,expr = line.split(":")
        if len(expr) > 10:
            item1,op,item2 = expr.split()
            if monkey == "root":
                op = "="
            items[monkey].fill_node(op, items[item1], items[item2])
            
    #print(items["root"])
    items["root"].collapse_node()
    
    return items["root"].reverse_tree()
    

    
    
    
def p2(lines):
    values = 0
    functs = {}

    for line in lines:
        monkey,op = line.split(":")
        op = op.strip()
        
        if monkey == "root":
            op = op[:5]+"="+op[6:]
        if monkey == "humn":
            op = "humn"
        
        functs[monkey] = op
    
    eq1,eq2 = resolve(functs,"root")[1:-1].split("=")
    if eq1.find("humn") > 0:
        eq = eq1
        val = eval(eq2)
    else:
        eq = eq2
        val = eval(eq1)
    
    lower = 1
    upper = 1
    diff = math.inf
    
    #find upper bound
    while True:
        new_eq = eq.replace("humn", str(upper))
        new_val = eval(new_eq)
        new_diff = abs(new_val-val)
        if new_diff > diff:
            break
        else: 
            diff = new_diff
            upper *= 1000
            
    #binary search now    
    for i in range(100):
        med = (lower + upper) //2
        new_eq = eq.replace("humn", str(med))
        new_val = eval(new_eq)
        new_diff = abs(new_val-val)
        if new_val > val:
            lower = med + 1
        elif new_val < val:
            upper = med -1
        else:
            break

    return med
    
def resolve(functs, item):
    op = functs.get(item) 
    if len(op) < 10:
        return op
    else:
        op1, operation, op2 = op.split()
        return f"({resolve(functs, op1)} {operation} {resolve(functs, op2)})".replace(" ","")
        
        
f = open("input21.txt", "r")
lines = [line.strip() for line in f]


start = timeit.default_timer()
print (f"Part 1: {p1(lines)}") 
stop = timeit.default_timer()
print(f'Time:{stop-start}\n')

start = timeit.default_timer()
print (f"Part 1 alt: {p1_alt(lines)}")
stop = timeit.default_timer()
print(f'Time:{stop-start}\n')

start = timeit.default_timer()
print (f"Part 1 p1 Tree: {p1_tree(lines)}")
stop = timeit.default_timer()
print(f'Time:{stop-start}\n')

start = timeit.default_timer()
print (f"Part 2: {p2(lines)}")
stop = timeit.default_timer()
print(f'Time:{stop-start}\n')

start = timeit.default_timer()
print (f"Part 2 tree: {p2_tree(lines)}")
stop = timeit.default_timer()
print(f'Time:{stop-start}\n')

