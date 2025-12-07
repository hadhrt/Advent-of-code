import timeit
import heapq
from dataclasses import dataclass


@dataclass(frozen=True, order = True)
class Coord:
    row: int
    col: int

    def __add__(self, other):
        return Coord(self.row + other.row, self.col + other.col)


ADJ_ALL_OFFSETS = ( Coord(-1,-1), Coord(-1, 0), Coord(-1, 1),
                    Coord( 0,-1),               Coord(-1, 1),
                    Coord( 1,-1), Coord( 1, 0), Coord( 1, 1))

ADJ_ORTH_OFFSETS = (             Coord(-1, 0),   
                    Coord( 0,-1),               Coord(-1, 1),
                                 Coord( 1, 0))


def print_grid(grid):
    print_string = ""
    for coord, val in grid.items():
        if coord.col == 0:
            print_string += "\n"
        print_string += val
    print(print_string)


def add_beam(grid, active_beams, coord, overlaps):
    if grid.get(coord) is None:
        # current beam has reached the end
        finished_particles = overlaps
        return (0,finished_particles)
    elif grid.get(coord) == ".":
        grid[coord] = "|"
        heapq.heappush(active_beams, (coord, overlaps))
        return (0,0) 
    elif grid.get(coord) == "|":
        # multiple beams in same coords will be merged when they are processed from que
        heapq.heappush(active_beams, (coord, overlaps)) 
        return (0,0)      
    elif grid.get(coord) == "^":
        finished_particles = 0
        finished_particles += add_beam(grid, active_beams,coord + Coord(0, -1), overlaps)[1]
        finished_particles += add_beam(grid, active_beams,coord + Coord(0, 1), overlaps)[1]
        return (1,finished_particles)
    else:
        assert(False)


def p1and2(lines):
    number_of_splits = 0
    finished_particles = 0
    grid = {
        Coord(row, col): val
        for row, line in enumerate(lines)
        for col, val in enumerate(line)
    }
    active_beams = [([key for key, val in grid.items() if val == "S"][0],1)]

    # process active beams
    while active_beams:
        current_beam_coord, overlaps = heapq.heappop(active_beams)

        # merge beams at same coord
        if active_beams:
            while active_beams[0][0] == current_beam_coord:
                merge_beam_coord, merge_overlaps = heapq.heappop(active_beams)
                overlaps += merge_overlaps
        
        new_splits, newly_finished_particals  = add_beam(grid, active_beams, current_beam_coord+Coord(1,0), overlaps)
        finished_particles += newly_finished_particals
        number_of_splits += new_splits 
        # print_grid(grid)

    return (number_of_splits,finished_particles)


# f = open(r"2025/Inputs/example.input", "r")
f = open(r"2025/Inputs/07.input", "r")
lines = [line.strip("\n") for line in f]

start = timeit.default_timer()
print(f"Part 1 and 2: {p1and2(lines)}")
stop = timeit.default_timer()
print(f"Time: {(stop - start):.4}")
