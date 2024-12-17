import re
from math import prod
from itertools import count

with open("input.txt") as f:
    data = [list(map(int, re.findall("-?\\d+", d))) for d in f.read().strip().split("\n")]

width = 101
height = 103
print(data)
def simulate(robots):
    quadrants = [0, 0, 0, 0]

    for px, py, vx, vy in robots:
        px = (px + 100 * vx) % width
        py = (py + 100 * vy) % height
        if px != 50 and py != 51:
            quadrants[(px > 50) + 2 * (py > 51) ] += 1
    return prod(quadrants)

def do_step(px, py, vx, vy, seconds):
    px = (px + vx * seconds) % width
    py = (py + vy * seconds) % height
    return px, py

def part_two(robots):
    for sec in count():
        current_robot_positions = set()
        for robot in robots:
            px, py = do_step(*robot, sec)
            current_robot_positions.add((px, py))
            #print(current)
        grid = []
        for i in range(height):
            line = ""
            for j in range(width):
                if (i, j) in current_robot_positions:
                    line += "X"
                else:
                    line += " "
            grid.append(line)

        for line in grid:
            print(line)
        print(f"--------This is after {sec} seconds--------")


print(f"part one: {simulate(data)}")
# 231019008

print(f"part two: {part_two(data)}")
#8280