with open("input.txt") as f:
    raw_grid, moves = f.read().strip().split("\n\n")


# https://networkx.org/documentation/stable/tutorial.html
# Continue with library from day 12

directions = {"^": -1, "v": 1, "<": -1j, ">": 1j}

# 1j represents imaginary unit in Python, which is used to encode 2D coordinates as complex numbers
# it simpilifies working with grid based problems as comlpex numbers can represent a 2D coordinate in a single value
# a + bj
# a is real part (horizontal coordinate)
# b is imaginary part (vertical coordinate)
# https://www.audiolabs-erlangen.de/resources/MIR/FMP/C2/C2_ComplexNumbers.html

grid = [list(l) for l in raw_grid.split("\n")]
#moves = [list(l) for l in moves.split("\n")]
moves = moves.replace("\n", "")

moves = [
    directions[c]
    for c in moves
]

def walls_and_boxes():
    walls = set()
    boxes = set()
    robot = None

    for i, line in enumerate(grid):
        for j, cell in enumerate(line):
            ij = complex(i + j * 1j)
            if cell == "#":
                walls.add(ij)
            elif cell == "O":
                boxes.add(ij)
            elif cell == "@":
                robot = ij
    return robot, walls, boxes


def simulate():
    robot, walls, boxes = walls_and_boxes()

    for move_z in moves:
        cur_move = set()
        next_moves = [robot + move_z]

        while next_moves:
            next_move = next_moves.pop()
            if next_move in boxes:
                cur_move.add(next_move)
                next_moves.append(next_move + move_z)
            elif next_move in walls:
                break
            else:
                robot += move_z
                boxes.difference_update(cur_move)
                for m in cur_move:
                    boxes.add(m + move_z)

    total = sum(boxes)
    return total.real * 100 + total.imag

print(f"part one: {simulate()}")
#1552463.0
