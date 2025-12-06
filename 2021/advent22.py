
import timeit
import re
from dataclasses import dataclass
from functools import cached_property


class SlowReactor:
    def __init__(self):
        self.cuboids = {}
        self.steps = []

    def parse_steps(self, lines):
        for line in lines:
            self.steps.append(tuple([line.split(' ')[0]]+[int(d)
                              for d in re.findall(r'-?\d+', line)]))
            pass

    def execute_step(self, step):
        switch, x_min, x_max, y_min, y_max, z_min, z_max = step
        for x in range(max(-50, x_min), min(50, x_max)+1):
            for y in range(max(-50, y_min), min(50, y_max)+1):
                for z in range(max(-50, z_min), min(50, z_max)+1):
                    self.cuboids[(x, y, z)] = switch

    def execute_all_steps(self):
        for idx, step in enumerate(self.steps):
            self.execute_step(step)
            #print(f"After Step {idx+1}: {self.get_number_of_on_cuboids()}")

    def get_number_of_on_cuboids(self):
        return len([cuboid for cuboid in self.cuboids.values() if cuboid == "on"])


@dataclass(frozen=True)
class Cube:
    sign: int
    x1: int
    x2: int
    y1: int
    y2: int
    z1: int
    z2: int

    @cached_property
    def volume(self) -> int:
        return abs(((self.x2-self.x1)+1)*((self.y2-self.y1)+1)*((self.z2-self.z1)+1))*self.sign

    @classmethod
    def from_line(cls, line):
        if line.split(' ')[0] == "on":
            sign = 1
        else:
            sign = -1
        coords = [int(d) for d in re.findall(r'-?\d+', line)]
        return cls(sign, *coords)

    def get_intersection_cube(self, other):
        assert (isinstance(other, Cube))
        x1 = max(self.x1, other.x1)
        x2 = min(self.x2, other.x2)
        y1 = max(self.y1, other.y1)
        y2 = min(self.y2, other.y2)
        z1 = max(self.z1, other.z1)
        z2 = min(self.z2, other.z2)
        if any([x1 > x2, y1 > y2, z1 > z2]):
            return None
        return Cube(other.sign * -1, x1, x2, y1, y2, z1, z2)


@dataclass
class Reactor:
    steps: list[Cube]

    @classmethod
    def from_lines(cls, lines):
        return cls([Cube.from_line(line) for line in lines])

    def startup(self) -> int:
        intersections = []
        for idx,cube in enumerate(self.steps):
            new_intersections = [cube.get_intersection_cube(intersection) for intersection in intersections]
            for new_intersection in new_intersections:
                if new_intersection != None:
                    intersections.append(new_intersection)
            if cube.sign == 1:
                intersections.append(cube)
            #print(f"After Step {idx+1}: {sum([intersection.volume for intersection in intersections])}")
        return sum([intersection.volume for intersection in intersections])


def p1(lines):
    reactor = SlowReactor()
    reactor.parse_steps(lines)
    reactor.execute_all_steps()

    return reactor.get_number_of_on_cuboids()


def p2(lines):
    reactor = Reactor.from_lines(lines)
    return reactor.startup()


f = open("input22.txt", "r")
lines = [line.strip() for line in f]


start = timeit.default_timer()
print(f"Part 1: {p1(lines)}")
stop = timeit.default_timer()
print('Time: ', stop - start)

start = timeit.default_timer()
print(f"Part 2: {p2(lines)}")
stop = timeit.default_timer()
print('Time: ', stop - start)
