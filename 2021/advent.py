
from __future__ import annotations
from dataclasses import dataclass
import timeit

@dataclass
class Grid:
    east_cucu: dict
    south_cucu: dict
    rows: int
    cols: int



    @classmethod
    def from_lines(cls:Grid, lines: str):
        east_cucu = {}
        south_cucu = {}
        for row,line in enumerate(lines):
            for col,val in enumerate(line):
                if val == ">":
                    east_cucu[(row,col)] = val
                if val == "v":
                    south_cucu[(row,col)] = val
        return Grid(east_cucu,south_cucu, len(lines), len(lines[0]))

    def __str__(self) -> str:
        ret = ""
        for row in range(self.rows):
            for col in range(self.cols):
                if (row,col) in self.east_cucu:
                    ret += self.east_cucu[(row,col)]
                else:
                    ret += self.south_cucu.get((row,col),'.')
            ret += "\n"
        return ret
    def __repr__(self) -> str:
        return str(self)

    def move_all(self) -> int:
        moved = 0
        new_east = {}
        new_south = {}
        # move east facing
        for row,col in self.east_cucu.keys():
            new_col = (col+1) % self.cols
            if (row,new_col) in self.south_cucu or (row,new_col) in self.east_cucu:
                new_east[row,col] = ">"
            else:
                new_east[row,new_col] = ">"
                moved +=1
        # move south facing
        for row,col in self.south_cucu.keys():
            new_row = (row+1) % self.rows
            if (new_row,col) in self.south_cucu or (new_row,col) in new_east:
                new_south[row,col] = "v"
            else:
                new_south[new_row,col] = "v"
                moved += 1

        self.east_cucu = new_east
        self.south_cucu = new_south
        return moved





def p1(lines):
    grid = Grid.from_lines(lines)
    moves = 1
    while (grid.move_all() != 0):
        moves += 1

    return moves


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