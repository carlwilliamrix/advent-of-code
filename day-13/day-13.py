import re
import numpy as np
with open("input.txt") as f:
    data = [list(map(int, re.findall("\\d+", d))) for d in f.read().strip().split("\n\n")]

#https://numpy.org/doc/2.1/reference/routines.linalg.html

def calculate_tokens(ax, ay, bx, by, px, py, offset):
    a = np.array([[ax, bx],[ ay, by]])
    p = np.array([px + offset, py + offset])
    tokens = np.linalg.solve(a, p).round()

    if all(a @ tokens == p):
        return int(tokens @ (3, 1))
    return 0

def calculate_overall(plays, offset):
    return sum(calculate_tokens(*p, offset) for p in plays)


print(f"part one: {calculate_overall(data, 0)}")
# 32067

print(f"part two: {calculate_overall(data, 10000000000000)}")