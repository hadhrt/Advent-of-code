import timeit
from numpy import base_repr


def snafuize(num):
    snafu = { 0:( 0,'0'), 
              1:( 0,'1'), 
              2:( 0,'2'), 
              3:( 1,'='), 
              4:( 1,'-'),
              5:( 1,'0')} 

    snafu_num_str = ""
    numlist = list( base_repr(num,5))
    carry = 0
    val = 0
    #print(f"digit list: {list(reversed(base_repr(num,5)))}")
    for base5_digit in list(map(int,list(reversed(base_repr(num,5)))+[0])):
        #print(f"base5_digit: {base5_digit}, carry: {carry}")
        base5_digit += carry
        carry, val_char = snafu[base5_digit]
        #print(f"val_char: {val_char}, new carry: {carry} snafu_num_str: {snafu_num_str}")
        snafu_num_str = val_char+snafu_num_str
    if snafu_num_str[0] == "0":
        snafu_num_str = snafu_num_str[1:]
        
    return snafu_num_str

def unsnafuize(snafu_num_str):
    unsnafu = {'2':2, '1': 1, '0':0, '-': -1, '=':-2}
    num = 0
    for idx,snafu_digit in enumerate(reversed(snafu_num_str)):
        num += unsnafu[snafu_digit] * pow(5,idx)

    return num
        
        
        
def p1(lines):
    values = 0
    for line in lines:
        values += unsnafuize(line)

        
    return snafuize(values)
    
def p2(lines):
    values = 0
    for line in lines:
        pass
    return values
    

f = open("input25.txt", "r")
lines = [line.strip() for line in f]
  

start = timeit.default_timer()
print (f"Part 1: {p1(lines)}")
stop = timeit.default_timer()
print('Time: ', stop - start)

start = timeit.default_timer()
print (f"Part 2: {p2(lines)}")
stop = timeit.default_timer()
print('Time: ', stop - start)