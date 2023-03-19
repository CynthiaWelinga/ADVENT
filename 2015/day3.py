"""
Santa is delivering presents to an infinite two-dimensional grid of houses.

He begins by delivering a present to the house at his starting location, 
and then an elf at the North Pole calls him via radio and tells him where to move next. 

Moves are always exactly one house to the north (^), south (v), east (>), or west (<). 

After each move, he delivers another present to the house at his new location.

However, the elf back at the north pole has had a little too much eggnog, 
and so his directions are a little off, and Santa ends up visiting some houses more than once. 

How many houses receive at least one present?

For example:

> delivers presents to 2 houses: one at the starting location, and one to the east.
^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.
"""


file_path = 'C:/Users/CynthiaWelinga/DEVELOPMENT/ADVENT/2015/day3.txt'
puzzle_input = open(file_path).read()

visited = []
coordinates = ['^', 'v', '>', '<']
pos = (0,0)

for i in puzzle_input:
    if i=='^':
        pos = (pos[0], pos[1]+1)
    elif i=='v':
        pos = (pos[0], pos[1]-1)
    elif i=='>':
        pos = (pos[0]+1, pos[1])
    else:
        pos = (pos[0]-1, pos[1])
    
    if pos not in visited: visited.append(pos)

print(len(visited))

"""
The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, 
to deliver presents with him.

Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), 
then take turns moving based on instructions from the elf, 
who is eggnoggedly reading from the same script as the previous year.

This year, how many houses receive at least one present?
"""

visited = []
santa_pos = (0,0)
robo_pos = (0,0)
for i in puzzle_input:

