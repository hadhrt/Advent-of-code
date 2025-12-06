import timeit

def p1(lines):
    values = 0
    games = get_games(lines)
    cube_max_amount = (12,13,14)
    for id,game in games:
        if all([amount[0]>=amount[1] for amount in zip(cube_max_amount,game)]):
           values += id
            
    return values

def get_games(lines):
    games = []
    colors = ((0,"red"),(1,"green"),(2,"blue"))
    for line in lines:
        game_id_string, cube_set_strings = line.split(":")
        game_id = int(game_id_string[5:])
        max_cubes = [0,0,0] #[r,g,b]
        for cube_set_string in cube_set_strings.split(";"):
            for cube_string in cube_set_string.split(","):
                for color_id, color_name in colors:
                    if color_name in cube_string:
                        cube_amount = int(cube_string.replace(color_name,""))
                        max_cubes[color_id] = max(max_cubes[color_id], cube_amount)
        games.append((game_id,tuple(max_cubes)))
    return games

def p2(lines):
    values = 0
    games = get_games(lines)
    for _id,cubes in games:
        values += (cubes[0]*cubes[1]*cubes[2])
    return values
    

f = open("input2.txt", "r")
lines = [line.strip() for line in f]
  
start = timeit.default_timer()
print (f"Part 1: {p1(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')

start = timeit.default_timer()
print (f"Part 2: {p2(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')