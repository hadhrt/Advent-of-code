
def p1(lines):
    values = 0
    monkeys=[]
    
    #read input
    for i in range(0,len(lines),7):
        items_l = lines[i+1].split(":")[1]
        items = [int(item) for item in items_l.split(",")]
        op_str = lines[i+2][lines[i+2].find("=")+1:]
        op = eval("lambda old: " + op_str)
        test_l = lines[i+3].split()
        val = test_l[-1]
        test = eval(f"lambda x: x % {val} == 0")
        true_monkey = int(lines[i+4].split()[-1])
        false_monkey = int(lines[i+5].split()[-1])
        monkeys.append({"items":items, "op":op, "test":test, "throw_to":{True:true_monkey,False:false_monkey},"items_inspected":0})
    
    '''    
    #1 round:
    for monkey in monkeys:
        print(f"Monkey {monkeys.index(monkey)}:")
        for item in monkey.get("items"):
            monkey["items_inspected"] += 1
            print(f"  Monkey inspects an item with a worry level of {item}.")
            worry_level = monkey.get("op")(item)
            print(f"    Worry level is increased to {worry_level}.")
            worry_level = worry_level // 3
            print(f"    Monkey gets bored with item. Worry level is divided by 3 to {worry_level}.")
            test_res = monkey.get("test")(worry_level)
            print(f"    Current worry level test is {test_res}.")
            throw_to = monkey.get("throw_to").get(test_res)
            monkeys[throw_to].get("items").append(worry_level)
            print(f"    Item with worry level {worry_level} is thrown to monkey {throw_to}.")
        monkey["items"] = []
    
    print("")
    print_monkeys(monkeys,1)
    '''
    
    #rounds:
    for i in range(1,21,1):
        for monkey in monkeys:
            for item in monkey.get("items"):
                monkey["items_inspected"] += 1
                worry_level = monkey.get("op")(item)
                worry_level = worry_level // 3
                test_res = monkey.get("test")(worry_level)
                throw_to = monkey.get("throw_to").get(test_res)
                monkeys[throw_to].get("items").append(worry_level)
            monkey["items"] = []
        #print_monkeys(monkeys,i)
    
    mb = sorted([monkey.get("items_inspected") for monkey in monkeys])
    monkey_business = mb[-1]*mb[-2]
    
    return monkey_business

def print_monkeys(monkeys,round):
    print(f"After round {round}, the monkeys are holding items with these worry levels:")
    for monkey in monkeys:
        item_str = str(monkey.get("items"))[1:-1]
        items_inspected = monkey.get("items_inspected")
        print(f"Monkey {monkeys.index(monkey)} ({items_inspected} items inspected): {item_str}")
    print("")

def p2(lines):
    values = 0
    monkeys=[]
    modulus = 1
    
    #read input
    for i in range(0,len(lines),7):
        items_l = lines[i+1].split(":")[1]
        items = [int(item) for item in items_l.split(",")]
        op_str = lines[i+2][lines[i+2].find("=")+1:]
        op = eval("lambda old: " + op_str)
        test_l = lines[i+3].split()
        val = test_l[-1]
        modulus *= int(val)
        test = eval(f"lambda x: x % {val} == 0")
        true_monkey = int(lines[i+4].split()[-1])
        false_monkey = int(lines[i+5].split()[-1])
        monkeys.append({"items":items, "op":op, "test":test, "throw_to":{True:true_monkey,False:false_monkey},"items_inspected":0})
    
     
    
    #rounds:
    for i in range(1,10001,1):
        for monkey in monkeys:
            for item in monkey.get("items"):
                monkey["items_inspected"] += 1
                worry_level = monkey.get("op")(item) % modulus
                test_res = monkey.get("test")(worry_level)
                throw_to = monkey.get("throw_to").get(test_res)
                monkeys[throw_to].get("items").append(worry_level)
            monkey["items"] = []
        #print_monkeys(monkeys,i)
    
    mb = sorted([monkey.get("items_inspected") for monkey in monkeys])
    monkey_business = mb[-1]*mb[-2]
    
    return monkey_business

f = open("input11.txt", "r")
lines = [line.strip() for line in f]
  

print ("Part 1: " + str(p1(lines)) )
print ("Part 2: " + str(p2(lines)) )