import timeit
import regex as re

def p1(lines):
    final_value = 0
    for line in lines:
       digits = [int(char) for char in line if char.isdigit()]
       final_value += 10*digits[0] + digits [-1]
    return final_value


def p2(lines):
    final_value = 0
    
    number_dict = {"1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, 
                   "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
    number_word_pattern = "".join([number_word+"|" for number_word in number_dict.keys()]) [:-1]
    for line in lines:
        number_words = re.findall(number_word_pattern,line, overlapped=True) 
        digits = [number_dict.get(number_word) for number_word in number_words]
        final_value += 10*digits[0] + digits[-1]

    return final_value
    

f = open("input1.txt", "r")
lines = [line.strip() for line in f]

  

start = timeit.default_timer()
print (f"Part 1: {p1(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')

start = timeit.default_timer()
print (f"Part 2: {p2(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')