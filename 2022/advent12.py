class Node:
    def __init__(self, pos, val):
        self.is_start = False
        self.is_end = False
        self.pos = pos

    
        if val == "S":
            self.is_start = True
            self.val = "abcdefghijklmnopqrstuvwxyz".index("a")
        elif val == "E":
            self.is_end = True
            self.val = "abcdefghijklmnopqrstuvwxyz".index("z")
        else:
            self.val = "abcdefghijklmnopqrstuvwxyz".index(val)
    def __str__(self):
        val_str = "abcdefghijklmnopqrstuvwxyz"[self.val]
        return f"{self.pos}:{val_str}"

def p1(lines):    
    grid = {(r,c): Node((r,c), val) for r,line in enumerate(lines) for c, val in enumerate(line)}

    start_node = [curr_node for curr_node in grid.values() if curr_node.is_start][0]


    visited_nodes = set()
    
    current_nodes = {start_node}
    steps = 0
    
    for i in range(1,500,1):
        #print(f"Step: {i}")
        for node in current_nodes: 
            visited_nodes.add(node)
            #print(node)
        nodes_for_next_step = set()
        steps += 1
        for current_node in current_nodes:
            new_nodes = get_valid_steps(grid, current_node)
            if any([node.is_end for node in new_nodes]):
                #print ("Ende erreicht")
                return i
            valid_nodes = new_nodes - visited_nodes
            for node in valid_nodes:
                nodes_for_next_step.add(node)
        current_nodes = nodes_for_next_step

    return 0

def get_valid_steps(grid, curr_node):

    ret_nodes = set()
    posr,posc = curr_node.pos
    check_pos = [(posr+1,posc), (posr-1,posc), (posr,posc+1), (posr,posc-1)]
    for pos in check_pos:
        node = grid.get(pos)
        if node != None:
            if node.val <= curr_node.val + 1:
                ret_nodes.add(node)
    return ret_nodes

    
    

def p2(lines):
    grid = {(r,c): Node((r,c), val) for r,line in enumerate(lines) for c, val in enumerate(line)}

    all_start_nodes = [curr_node for curr_node in grid.values() if curr_node.val == 0]
    
    min_steps=[]

    for start_node in all_start_nodes:
        end_reached = False
        visited_nodes = set()
        current_nodes = {start_node}
        steps = 0
        
        for i in range(1,1000,1):
            #print(f"Step: {i}")
            for node in current_nodes: 
                visited_nodes.add(node)
                #print(node)
            nodes_for_next_step = set()
            steps += 1
            for current_node in current_nodes:
                new_nodes = get_valid_steps(grid, current_node)
                if any([node.is_end for node in new_nodes]):
                    #print ("Ende erreicht")
                    end_reached = True
                    break
                valid_nodes = new_nodes - visited_nodes
                for node in valid_nodes:
                    nodes_for_next_step.add(node)
            if end_reached: 
                min_steps.append(i)
                break
            current_nodes = nodes_for_next_step
    
    return min(min_steps)

f = open("input12.txt", "r")
lines = [line.strip() for line in f]
  

print ("Part 1: " + str(p1(lines)) )
print ("Part 2: " + str(p2(lines)) )