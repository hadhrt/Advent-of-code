import timeit
from typing import Self

INS = {
            0:"adv",
            1:"bxl",
            2:"bst",
            3:"jnz",
            4:"bxc",
            5:"out",
            6:"bdv",
            7:"cdv"}
OP = {
            0:"0",
            1:"1",
            2:"2",
            3:"3",
            4:"register_A",
            5:"register_B",
            6:"register_C",
            7:"None"}

class Computer():


    def __init__(self, register_A = 0, register_B= 0, register_C= 0):
        self.register_A = [register_A]
        self.register_B = [register_B]
        self.register_C = [register_C]
        self.ins_pointer = 0
        self.output =[]

        
        self.INS = {
            0:self.adv,
            1:self.bxl,
            2:self.bst,
            3:self.jnz,
            4:self.bxc,
            5:self.out,
            6:self.bdv,
            7:self.cdv}
        self.OP = {
            0:[0],
            1:[1],
            2:[2],
            3:[3],
            4:self.register_A,
            5:self.register_B,
            6:self.register_C,
            7:None}

    @classmethod 
    def from_lines(cls,lines) -> Self:
        register_A = int(lines[0].split(" ")[-1])
        register_B = int(lines[1].split(" ")[-1])
        register_C = int(lines[2].split(" ")[-1])
        return cls(register_A, register_B, register_C)
   
    def set_registers(self, register_A, register_B, register_C):
        self.register_A[0] = register_A
        self.register_B[0] = register_B
        self.register_C[0] = register_C
        
    def adv(self,operand):
        operand = self.OP[operand][0]
        self.register_A[0] = self.register_A[0] // (2 ** operand)
        self.ins_pointer += 2
        return    
    def bxl(self,operand):
        operand = operand
        self.register_B[0] = self.register_B[0] ^ operand
        self.ins_pointer += 2
        return
    def bst(self,operand):
        operand = self.OP[operand][0]
        self.register_B[0] = operand % 8
        self.ins_pointer += 2
        return
    def jnz(self,operand):
        operand = operand
        if self.register_A[0] == 0:
            self.ins_pointer += 2
        else:
            self.ins_pointer = operand
        return
    def bxc(self,operand):
        self.register_B[0] = self.register_B[0] ^ self.register_C[0] 
        self.ins_pointer += 2
        return
    def out(self,operand):
        operand = self.OP[operand][0]
        self.output.append(operand % 8)
        self.ins_pointer += 2
        return
    def bdv(self,operand):
        operand = self.OP[operand][0]
        self.register_B[0] = self.register_A[0] // (2 ** operand)
        self.ins_pointer += 2
        return
    def cdv(self,operand):
        operand = self.OP[operand][0]
        self.register_C[0] = self.register_A[0] // (2 ** operand)
        self.ins_pointer += 2
        return
    
    def compute(self, program):
        self.ins_pointer = 0
        self.output = []
        for i in range(1000):
            if self.ins_pointer > len(program) - 2:
                #print(f"Program output: {self.output}")
                return self.output
            else:
                ins = self.INS[program[self.ins_pointer]]
                op = program[self.ins_pointer + 1]
                #if len(self.output)>=1:
                #    print(f"{INS[program[self.ins_pointer]]}({program[self.ins_pointer+1]}[{OP[program[self.ins_pointer+1]]}]) A:{self.register_A[0]}, B:{self.register_B[0]}, C:{self.register_C[0]}, out:{self.output[-1]} ")
                ins(op)
               
        assert False, "Program running to long"
            
    def compute_and_check(self, program):
        self.ins_pointer = 0
        self.output = []
        for i in range(1000):
            if self.ins_pointer > len(program) - 2:
                if self.output == program:
                    return True
                else:
                    return False
            else:
                ins = self.INS[program[self.ins_pointer]]
                op = program[self.ins_pointer + 1]
                ins(op)
                if self.output != program[:len(self.output)]:
                    return False
        assert False, "Program running to long"


def p1(lines):
  
    pl = lines[4].split("Program: ")[-1]
    program = [int(val) for val in pl.split(",") if val.isdigit()]
    my_computer = Computer.from_lines(lines)
    output = my_computer.compute(program)
    return "".join(str(i)+"," for i in output)[:-1]


def p2(lines):
    pl = lines[4].split("Program: ")[-1]
    program = [int(val) for val in pl.split(",") if val.isdigit()]
    A = 0
    valid_As = [[] for _ in program]
    valid_As.append([0])

    for i in range(len(program)-1, -1, -1):
        current_out = program[i]
        for valid_A in valid_As[i+1]:
            for pot_A in range(8*valid_A, 8*valid_A+8):
                if step(pot_A) == current_out:
                    valid_As[i].append(pot_A)

    return min(valid_As[0])


def step(A) -> int:
    B = (A%8)^5
    C = A // (2**B)
    B ^= 6
    # A //= 8
    return ((B^C)%8)


f = open("input17.txt", "r")
lines = [line.strip() for line in f]
  
start = timeit.default_timer()
print (f"Part 1: {p1(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')

start = timeit.default_timer()
print (f"Part 2: {p2(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')