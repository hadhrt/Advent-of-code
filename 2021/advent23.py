from __future__ import annotations
import timeit
import heapq
from dataclasses import dataclass,field,replace
from functools import cached_property
import sys


ROOM_SPACES = 2

@dataclass(frozen=True, order=True)
class State:

    hallway: tuple[str]
    rooms: tuple[tuple[str]]
    cost: int = field(compare = False)

    @classmethod
    def from_lines(cls, lines: list[str]) -> State:
        hallway = tuple(['.']*11)
        rooms = [[],[],[],[]]
        for row in range(2,len(lines)-1):
            for i in range(4):
                rooms[i].append(lines[row][3+(2*i)])
        '''
        room_A = (lines[2][3],lines[3][3])
        room_B = (lines[2][5],lines[3][5])
        room_C = (lines[2][7],lines[3][7])
        room_D = (lines[2][9],lines[3][9])
        '''
        return cls(hallway, tuple(tuple(room) for room in rooms), 0)

    def __str__(self) -> str:
        print_rooms = list(self.rooms)
        for idx,room in enumerate(print_rooms):
            while len(print_rooms[idx]) < ROOM_SPACES:
                print_rooms[idx] = ('.',) + print_rooms[idx]

        ret = "#############\n#"
        ret += ''.join(self.hallway) + '#\n'
        for row in range(ROOM_SPACES):
            ret += f"###{print_rooms[0][row]}#{print_rooms[1][row]}#{print_rooms[2][row]}#{print_rooms[3][row]}###\n"
        ret += "  #########  \n"
        ret += f"Cost: {self.cost}\n"
        return ret

@dataclass
class Cave:
    starting_state: State
    AMPHI_MOVE_COST = {"A": 1, "B": 10, "C": 100, "D": 1000}
    #TO_NAME = {1: "A", 10: "B", 100: "C", 1000: "D"}
    ROOM_OWNERS = {0: "A", 1: "B", 2: "C", 3: "D" }
    AMPHI_HOME =  {"A": 0, "B": 1, "C": 2, "D": 3 }
    #                 Room: (Pos, moves)
    ROOM_MOVES_LEFT  = {0: ((1,2), (0,3)),
                        1: ((3,2), (1,4), (0,5)),
                        2: ((5,2), (3,4), (1,6), (0,7)),
                        3: ((7,2), (5,4), (3,6), (1,8), (0,9))}
    ROOM_MOVES_RIGHT = {0: ((3,2), (5,4), (7,6), (9,8), (10,9)),
                        1: ((5,2), (7,4), (9,6), (10,7)),                    
                        2: ((7,2), (9,4), (10,5)),
                        3: ((9,2), (10,3))}
    HALLWAY_SPACES = (0,1,3,5,7,9,10)
    # [Amphi, Position] -> (len,pos_to_check)
    PATHS_TO_ROOM = {("A",0): (3,(1,)),
                     ("A",1): (2,()),
                     ("A",3): (2,()),
                     ("A",5): (4,(3,)),
                     ("A",7): (6,(5,3)),
                     ("A",9): (8,(7,5,3)),
                     ("A",10):(9,(9,7,5,3)),
                     ("B",0): (5,(1,3)),
                     ("B",1): (4,(3,)),
                     ("B",3): (2,()),
                     ("B",5): (2,()),
                     ("B",7): (4,(5,)),
                     ("B",9): (6,(7,5)),
                     ("B",10):(7,(9,7,5)),
                     ("C",0): (7,(1,3,5)),
                     ("C",1): (6,(3,5)),
                     ("C",3): (4,(5,)),
                     ("C",5): (2,()),
                     ("C",7): (2,()),
                     ("C",9): (4,(7,)),
                     ("C",10):(5,(9,7)),
                     ("D",0): (9,(1,3,5,7)),
                     ("D",1): (8,(3,5,7)),
                     ("D",3): (6,(5,7)),
                     ("D",5): (4,(7,)),
                     ("D",7): (2,()),
                     ("D",9): (2,()),
                     ("D",10):(3,(9,))}

    @classmethod
    def from_lines(cls, lines: list[str]) -> Cave:
        starting_state = State.from_lines(lines)
        return cls(starting_state)


    def get_new_states(self, state: State) -> list[tuple(State, int)]:
        new_states = []
        # Amphi moves out of a room
        for room_index,room in enumerate(state.rooms):
            room_owner = Cave.ROOM_OWNERS.get(room_index)
            # skip if room is finished
            if all(amphi == room_owner for amphi in room):
                continue
            # skip if room is empty
            if len(room) == 0:
                continue
            # left move
            for new_pos, moves in Cave.ROOM_MOVES_LEFT.get(room_index):
                # occupied position
                if state.hallway[new_pos] != ".":
                    break
                # move valid, create new state

                    # get Amphi out of room
                amphi = room[0]
                changed_room = room[1:]
                new_room_list = list(state.rooms)
                new_room_list[room_index] = changed_room

                    # move Amphi to hallway
                new_hallwaylist = list(state.hallway)
                new_hallwaylist[new_pos] = amphi

                    # calculate move cost (moves + moves inside room) * cost per move
                moves_inside_room = ROOM_SPACES - len(room)
                add_cost = (moves + moves_inside_room) * Cave.AMPHI_MOVE_COST.get(amphi)
                new_states.append(State(hallway=tuple(new_hallwaylist), rooms= tuple(new_room_list) ,cost= state.cost + add_cost ))
                pass
            # right move 
            for new_pos, moves in Cave.ROOM_MOVES_RIGHT.get(room_index):
                # occupied position
                if state.hallway[new_pos] != ".":
                    break
                # move valid, create new state
                    # get Amphi out of room
                amphi = room[0]
                changed_room = room[1:]
                new_room_list = list(state.rooms)
                new_room_list[room_index] = changed_room

                    # move Amphi to hallway
                new_hallwaylist = list(state.hallway)
                new_hallwaylist[new_pos] = amphi

                    # calculate move cost (moves + moves inside room) * cost per move
                moves_inside_room = ROOM_SPACES - len(room)
                add_cost = (moves + moves_inside_room) * Cave.AMPHI_MOVE_COST.get(amphi)
                new_states.append(State(hallway=tuple(new_hallwaylist), rooms= tuple(new_room_list) ,cost= state.cost + add_cost ))

        # Amphi moves into its room
        for starting_pos in Cave.HALLWAY_SPACES:
            if state.hallway[starting_pos] == '.':
                continue
            amphi = state.hallway[starting_pos]
            # check amphis room
            room_index = Cave.AMPHI_HOME.get(amphi)
            if any(occupant != amphi for occupant in state.rooms[room_index]):
                continue
            # check path
            path_len,path = Cave.PATHS_TO_ROOM.get((amphi,starting_pos))
            if any(state.hallway[path_pos] !='.' for path_pos in path):
                continue

            # move valid, create new state
                # get Amphi into room
            new_room_list = list(state.rooms)
            new_room_list[room_index] =  (amphi,) + new_room_list[room_index]

                # remove Amphi from hallway
            new_hallwaylist = list(state.hallway)
            new_hallwaylist[starting_pos] = '.'

                # calculate move cost 
            moves_inside_room = ROOM_SPACES - len(new_room_list[room_index])
            add_cost = (path_len + moves_inside_room) * Cave.AMPHI_MOVE_COST.get(amphi)
            new_states.append(State(hallway=tuple(new_hallwaylist), rooms= tuple(new_room_list) ,cost= state.cost + add_cost ))

        #for state in new_states:
        #    print(str(state))
        return new_states


    def sort_amphis(self):
        finished_hallway = tuple(['.']*11)
        finished_rooms = (tuple(['A']*ROOM_SPACES), tuple(['B']*ROOM_SPACES), tuple(['C']*ROOM_SPACES), tuple(['D']*ROOM_SPACES), )
        finished_cost = float("inf")
        
        finished_state = State(hallway = finished_hallway, rooms= finished_rooms, cost= finished_cost)
        # print(f"Starting State: \n{self.starting_state}")
        # print(f"Finished State: \n{finished_state}")

        # print(f"Starting State == Finished State? {self.starting_state == finished_state}")


        states_todo = []
        finished_states = set()
        heapq.heappush(states_todo,(0 ,self.starting_state))        
        curr_state = None

        while states_todo:
            curr_energy,curr_state = heapq.heappop(states_todo)
            
            if curr_energy > 100000: 
                return -1
            if curr_state in finished_states:
                continue
            # print(f"Finished States: {len(finished_states)} Heap: {len(states_todo)} {curr_energy=}")
            
            finished_states.add(curr_state)
            if curr_state == finished_state: 
                # print(curr_state)
                return curr_state.cost

            for state in self.get_new_states(curr_state):
                if state in finished_states:
                    continue
                heapq.heappush(states_todo,(state.cost, state))

        return -1



def p1(lines):
    cave = Cave.from_lines(lines)
    #print(cave.starting_state)
    cave.get_new_states(cave.starting_state)
    return cave.sort_amphis()


def p2(lines):
    global ROOM_SPACES
    ROOM_SPACES = 4
    lines.insert(3,"  #D#C#B#A#")
    lines.insert(4,"  #D#B#A#C#")
    #lines.insert(3,"  #A#B#C#D#")
    #lines.insert(4,"  #A#B#C#D#")
    cave = Cave.from_lines(lines)
    #print(cave.starting_state)
    #cave.get_new_states(cave.starting_state)
    return cave.sort_amphis()


f = open("input23.txt", "r")
lines = f.read().splitlines()


start = timeit.default_timer()
print(f"Part 1: {p1(lines)}")
stop = timeit.default_timer()
print('Time: ', stop - start)

start = timeit.default_timer()
print(f"Part 2: {p2(lines)}")
stop = timeit.default_timer()
print('Time: ', stop - start)
