def create_grid_and_trailheads():
    with open("input.txt") as f:
        data = f.read()

    grid = []
    trailheads = []
    for row in data.splitlines():
        grid.append(list(map(int, row)))

    width = len(grid)
    height = len(grid[0])

    for i in range(height):
        for j in range(width):
            if grid[i][j] == 0:
                trailheads.append((i, j))

    return grid, trailheads, width, height

def find_trails(grid, trailhead, x, y, part_two):
    total = 0
    for i, j in trailhead:
        if part_two:
            total += find_individual_trail(grid, i, j, x, y, part_two)
        else:
            total += len(find_individual_trail(grid, i, j, x, y, part_two))
    return total

def find_individual_trail(grid, i, j, x, y, part_two):
    if grid[i][j] == 9:
        return 1 if part_two else {(i, j)}

    trails = 0 if part_two else set()

    for ni, nj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
        if 0 <= ni < x and 0 <= nj < y and grid[ni][nj] == grid[i][j] + 1:
            if part_two:
                trails += find_individual_trail(grid, ni, nj, x, y, part_two)
            else:
                trails |= find_individual_trail(grid, ni, nj, x, y, part_two)

    return trails

grid, trailheads, width, height = create_grid_and_trailheads()
print(f"part one: {find_trails(grid, trailheads, width, height, False)}")
#538

print(f"part two: {find_trails(grid, trailheads, width, height, True)}")
# 1110


