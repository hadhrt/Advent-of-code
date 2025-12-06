import timeit
import numpy as np
from copy import deepcopy
import itertools
MIN_OVERLAP = 12

class Scanner:

    def __init__(self, name) -> None:
        self.name = name
        self.beacons = []
        self.rotate_state = 0
        self.negate_state = 0

    def parse_coords(self, lines) -> None:
        beacons = []
        for line in lines:
            coord = list(map(int,line.split(",")))
            beacons.append(np.array(coord))
        self.beacons = np.array(beacons)

    def swap(self,column1,column2):
        self.beacons [:, [column1, column2]] = self.beacons [:, [column2, column1]]
    
    def negate(self,column):
        a = np.array([1,1,1])
        a[column] = -1
        self.beacons *=a
    
    def shift(self, vector):
        self.beacons +=vector

    def rotate_next(self):
        match (self.rotate_state%3):
            case 0:
                self.swap(0,1)
            case 1:
                self.swap(1,2)
            case 2:
                self.swap(2,0)
        
        if self.rotate_state % 6 == 0:
            if self.negate_state % 1 == 0:
                self.negate(2)
            if self.negate_state % 2 == 0:
                self.negate(1)
            if self.negate_state % 4 == 0:
                self.negate(0)
            self.negate_state += 1
        self.rotate_state += 1

    def __str__(self) -> str:
        #return f"{self.name}:\n{str(self.beacons)}"
        return f"{str(self.beacons)}"
    def __repr__(self) -> str:
        return str(self)

    def rotations24(self,a):
        # Even permutations, (x,y,z), (y,z,x), (z,x,y)
        evens = ([0, 1, 2], [1, 2, 0], [2, 0, 1])
        # Odd permutations, (y,x,z), (z,y,x), (x,z,y)
        odds = ([0, 2, 1], [1, 0, 2], [2, 1, 0])
        even_signs = [(1, 1, 1), (-1, -1, 1), (-1, 1, -1), (1, -1, -1)]
        odd_signs = (np.array(even_signs) * -1).tolist()
        for cols, sign in itertools.product(evens, even_signs):
            yield a[:, cols] * sign
        for cols, sign in itertools.product(odds, odd_signs):
            yield a[:, cols] * sign

    def find_intersection(self, scanner2):
        
        np1 = self.beacons
        set1 = set((tuple(c) for c in np1 ))
        np2 = scanner2.beacons
        for fp1 in np1[:(-MIN_OVERLAP +2)]:                           # <- check here later
            diff_to_orig = fp1.copy() - fp1  #[0,0,0] array
            for i in range(len(np2)):
                diff = fp1 - np2[i]
                np2 = np2 + diff #normalize array to fp2
                diff_to_orig += diff
                set2 = set((tuple(c) for c in np2 ))
                if len(set1&set2) >= MIN_OVERLAP:
                    scanner2.shift(diff_to_orig)
                    return True
        return False

    def find_using_rotations24(self):
        rotations = self.rotations24(self.beacons)
        print(list(rotations))


def p1(filestr):
    values = 0
    scanners = []
    scanner_strings = filestr.split("\n\n")
    for scanner_string in scanner_strings:
        scanner_lines = scanner_string.split("\n")
        name = scanner_lines[0][4:-4]
        scanner = Scanner(name)
        scanner.parse_coords(scanner_lines[1:])
        scanners.append(scanner)

    scanner1 = scanners[0]
    scanner1.find_using_rotations24()
    #scanner2 = scanners[1]
    #scanner2.negate(2)
    #scanner2.negate(0)
    #scanner2.shift(np.array([68,-1246,-43]))

    '''
    for i in range(48):
        scanner2.rotate_next()
        if scanner1.find_intersection(scanner2):
            break



    set1 = set((tuple(c) for c in scanner1.beacons))
    set2 = set((tuple(c) for c in scanner2.beacons))
    print(set1&set2)
    '''
    return values


def p2(filestr):
    values = 0
    for line in filestr:
        pass
    return values
    

f = open("input.txt", "r")
filestr = f.read()
  

start = timeit.default_timer()
print (f"Part 1: {p1(filestr)}")
stop = timeit.default_timer()
print('Time: ', stop - start)

start = timeit.default_timer()
print (f"Part 2: {p2(filestr)}")
stop = timeit.default_timer()
print('Time: ', stop - start)