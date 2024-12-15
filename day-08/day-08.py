from collections import defaultdict
from itertools import permutations

with open("input.txt") as f:
    data = f.read().strip().split("\n")

def find_antennas(board):
    antennas = defaultdict(list)
    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            if cell not in (".", "#"):
                antennas[cell].append((x, y))
    return antennas

def calculate_positions(antennas):
    antinodes = set()
    for coords in antennas.values():
        print(coords)
        for z1, z2 in permutations(coords, 2):
            print(z1, z2)
            antinodes.add(2 * z2 - z1)
    return antinodes



antinodes = calculate_positions(find_antennas(data))
#total = {(x, y) for x, y in total if x in range(len(data)) and y in range(len(data[0])) }

print(f" Part one {len(antinodes)}")

