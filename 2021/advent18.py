import timeit


class SN:
    def __init__(self, parent = None, sn_list = None):
        self.parent = parent
        if sn_list == None:
            self.left = None
            self.right = None
        else:
            if isinstance(sn_list[0], int):
                self.left = NN(self,sn_list[0])
            else:
                self.left = SN(self, sn_list[0])
            if isinstance(sn_list[1], int):
                self.right = NN(self, sn_list[1])
            else:
                self.right = SN(self, sn_list[1])
    def __str__(self) -> str:
        return f"[{str(self.left)}, {str(self.right)}]"
    def __repr__(self) -> str:
        return str(self)
    def get_magnitude(self):
        return (3 * self.left.get_magnitude()) + (2*self.right.get_magnitude())

class NN:
    def __init__(self, parent, value):
        self.parent = parent
        self.value = value
    def __str__(self) -> str:
        return str(self.value)
    def __repr__(self) -> str:
        return str(self)
    def get_magnitude(self):
        return self.value


def explode_next(root):
    explodable = get_explodable(root)
    if explodable == None:
        return False
    left_NN = get_left_NN(explodable)
    if left_NN != None:
        left_NN.value += explodable.left.value
    right_NN = get_right_NN(explodable)
    if right_NN != None:
        right_NN.value += explodable.right.value
    if explodable.parent.left == explodable:
        explodable.parent.left = NN(explodable.parent,0)
    else:
        explodable.parent.right = NN(explodable.parent,0)
    return True

def get_explodable(node , level = 0):
    # check if current node is explodable
    if level >= 4:
        if isinstance(node.left, NN) and isinstance(node.right, NN):
            return node
    # check left node for explodabels, then right node
    if isinstance(node.left, SN):
        ge_left = get_explodable(node.left, level+1)
        if ge_left != None:
            return ge_left
    if isinstance(node.right, SN):
        return get_explodable(node.right, level+1)
    return None

def get_left_NN(node):
    current = node
    # move up the tree until there is a left sibling or root is reached
    while True:
        if current.parent == None:
            return None
        if current.parent.left == current:
            current = current.parent
        else:
            current = current.parent.left
            break
    # now move down right children until leaf
    while not isinstance(current, NN):
        current = current.right
    return current

def get_right_NN(node):
    current = node
    # move up the tree until there is a right sibling or root is reached
    while True:
        if current.parent == None:
            return None
        if current.parent.right == current:
            current = current.parent
        else:
            current = current.parent.right
            break
    # now move down left children until leaf
    while not isinstance(current, NN):
        current = current.left
    return current

def split(node):
    split_sn = [node.value//2, (node.value+1)//2 ]
    new_node = SN(node.parent, split_sn)
    if node.parent.left == node:
        node.parent.left = new_node
    else:
        node.parent.right = new_node

def split_next(node):
    if isinstance(node, NN):
        if node.value >=10:
            split(node)
            return True
        else:
            return False
    #  check left node for for splittable, then right node
    split_left = split_next(node.left)
    if split_left != False:
        return split_left
    return split_next(node.right)

def reduce_sn(node):
    while True:
        while explode_next(node):
            pass
            #print(f"After explode: {node}")
        if not split_next(node):
            break

def add_sn(sn1,sn2):
    new_root = SN()
    sn1.parent = new_root
    sn2.parent = new_root
    new_root.left = sn1
    new_root.right = sn2
    return new_root
    
def p1(lines):
    values = 0
    sn = SN(None, eval(lines[0]))
    for line in lines[1:]:
        sn2 = SN(None, eval(line))
        sn = add_sn(sn,sn2)
        reduce_sn(sn)


    print(sn)
    return sn.get_magnitude()


def p2(lines):
    max_val = 0
    for sn1_line in lines:
        for sn2_line in lines:
            if sn1_line == sn2_line:
                continue
            sn1 = SN(None, eval(sn1_line))
            sn2 = SN(None, eval(sn2_line))
            sn1 = add_sn(sn1,sn2)
            reduce_sn(sn1)
            val = sn1.get_magnitude()
            if val > max_val:
                max_val = val

    return max_val


f = open("input18.txt", "r")
lines = [line.strip() for line in f]


start = timeit.default_timer()
print(f"Part 1: {p1(lines)}")
stop = timeit.default_timer()
print('Time: ', stop - start)

start = timeit.default_timer()
print(f"Part 2: {p2(lines)}")
stop = timeit.default_timer()
print('Time: ', stop - start)
