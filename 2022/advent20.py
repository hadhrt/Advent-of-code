
DECR_KEY = 811589153

class Decrypt_list:
    def __init__(self):
        self.item_list = []
        self.item_0 = None
        
    def append(self, item):
        if item == 0:
            self.item_0 = (len(self.item_list),item)
        self.item_list.append((len(self.item_list),item))  
        
    def __str__(self):
        return ("".join([str(i)+", " for _,i in self.item_list]))[:-2] 
        
    def __repr__(self):
        return str(self)
        
    def move_item(self, item):
        old_index = self.item_list.index(item)
        self.item_list.remove(item)
        
        new_index = (item[1] + old_index) % (len(self.item_list))
        #if new_index == 0:
        #    new_index = len((self.item_list))

        
        self.item_list.insert(new_index,item)
        
        
    def get_coords(self):
        idx_0 = self.item_list.index(self.item_0)
        idx_1000 = (idx_0 + 1000) % len(self.item_list)
        idx_2000 = (idx_0 + 2000) % len(self.item_list)
        idx_3000 = (idx_0 + 3000) % len(self.item_list)

        return self.item_list[idx_1000][1] + self.item_list[idx_2000][1] + self.item_list[idx_3000][1]
    
def p1(lines):
    values = 0

    decr_list = Decrypt_list()
    for line in lines:
        decr_list.append(int(line))
    for idx,line in enumerate(lines):
        decr_list.move_item((idx,int(line)))
        
    
    return decr_list.get_coords()


def p2(lines):
    values = 0

    decr_list = Decrypt_list()
    for line in lines:
        decr_list.append(int(line)*DECR_KEY)
    
    for i in range(10):
        for idx,line in enumerate(lines):
            decr_list.move_item((idx,int(line)*DECR_KEY))   
    

    return decr_list.get_coords()

    

f = open("input20.txt", "r")
lines = [line.strip() for line in f]
  

print (f"Part 1: {p1(lines)}")
print (f"Part 2: {p2(lines)}")