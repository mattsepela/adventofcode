import re
games = open("values.txt").read()
possible = 0
max_val = {"red": 12, "green": 13, "blue": 14}
for game_num, game in enumerate(games.split("\n"), start=1):
    for num, color in re.findall("(\d+)\s(red|green|blue)", game):
        if int(num) > max_val[color]:
            break
    else:
        possible += int(game_num)
print(possible)

import math
cube_power = 0
for game_num, game in enumerate(games.split("\n"), start=1):
    max_cubes = {"red": 0, "green": 0, "blue": 0}
    for num, color in re.findall("(\d+)\s(red|green|blue)", game):
        if int(num) > max_cubes[color]:
            max_cubes[color] = int(num)
    cube_power += math.prod(max_cubes.values())
print(cube_power)
