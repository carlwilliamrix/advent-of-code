with open("input.txt") as f:
    raw_grid, moves = f.read().strip().split("\n\n")

directions = {"^": -1, "v": 1, "<": -1j, ">": 1j}

grid = [list(l) for l in raw_grid.split("\n")]
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
            ij = complex(i + j * 2j)
            if cell == "#":
                walls.update({ij, ij+1j})
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
            # box_left = next_move - 1j
            # if box_left in boxes:
            #     is_box_right = True
            #     i += 1
            # else:
            #     is_box_right = False
            is_box_right = (box_left := next_move - 1j) in boxes
            if move_z in boxes or is_box_right:
                next_moves.append(next_move + move_z)

                if is_box_right:
                    cur_move.add(box_left)
                else:
                    cur_move.add(move_z)

                # #if move_z.real != 0:
                # if move_z.real:
                #     if is_box_right:
                #         next_moves.append(box_left + move_z)
                #     else:
                #         next_moves.append(move_z + next_move + 1j)

                if move_z.real:
                    side = box_left if is_box_right else move_z + 1j
                    cur_move.add(side)
            elif next_move in walls:
                break

        else:
            robot += move_z
            boxes.difference_update(cur_move)
            for cm in cur_move:
                boxes.add(cm + move_z)

    total = sum(boxes)

    return total.real * 100 + total.imag


def solve():
    robot, walls, boxes = walls_and_boxes()

    for move_z in moves:
        cur_moves = set()
        check_moves = [robot + move_z]

        while check_moves:
            next_move = check_moves.pop()
            is_box_right = (box_left := next_move - 1j) in boxes

            if next_move in boxes or is_box_right:
                cur_moves.add(box_left if is_box_right else next_move)
                check_moves.append(next_move + move_z)

                if move_z.real:
                    other = box_left if is_box_right else next_move + 1j
                    check_moves.append(other + move_z)
            elif next_move in walls:
                break

        else:
            robot += move_z
            boxes.difference_update(cur_moves)
            for cm in cur_moves:
                boxes.add(cm + move_z)

    tot = sum(boxes)
    return tot.real * 100 + tot.imag


print(f"part two: {solve()}")
#1554058.0