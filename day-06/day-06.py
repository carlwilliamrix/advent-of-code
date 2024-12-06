with open("input.txt") as f:
    data = f.read().strip().split("\n")

def simulate_guard_patrol(grid):
    directions = {"^": (-1, 0), "v": (1, 0), ">": (0, 1), "<": (0, -1)}
    right_turn = {"^": ">", "v": "<", ">": "v", "<": "^"}

    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell in directions:
                guard_position = (r, c)
                guard_direction = cell
                break

    visited_positions = set()

    while True:
        dr, dc = directions[guard_direction]
        next_pos = (guard_position[0] + dr, guard_position[1] + dc)

        if not 0 <= next_pos[0] < len(grid) and 0 <= next_pos[1] < len(grid[0]):
            visited_positions.add(next_pos)
            return len(visited_positions), visited_positions

        if grid[next_pos[0]][next_pos[1]] == "#":
            guard_direction = right_turn[guard_direction]
            #print(guard_position[0],guard_position[1])
            #print(data[guard_position[0][:guard_position[1]-1]])
            #grid_line = data[guard_position[0]]
            #data[guard_position[0]] = str(grid_line[:guard_position[1]]) + "X" + str(data[guard_position[1]+1:])
            #print(str(grid_line[:guard_position[1]]) + "X" + str(data[guard_position[1]+1:]))
            #distinct_positions += 1
        else:
            guard_position = next_pos
            visited_positions.add(guard_position)
            #data[guard_position[0]][guard_position[1]] = "X"
            #grid_line = data[guard_position[0]]
            #data[guard_position[0]] = grid_line[:guard_position[1]] , 'X' , data[guard_position[1]+1:]

l, l2 = simulate_guard_patrol(data)
print(f"Unique positions covered by the guard {l}")
# Part 1: 4890

def print_path(grid, visited):
    for r in range(len(grid)):
        row = ""
        for c in range(len(grid[0])):
            if (r, c) in visited:
                row += "X"
            else:
                row += grid[r][c]
        print(row)

# Print the path
#print_path(data, l2)

def find_obstruction_positions(grid):
    directions = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
    right_turn = {"^": ">", ">": "v", "v": "<", "<": "^"}

    # Find guard's starting position and direction
    guard_start = None
    guard_dir = None
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell in directions:
                guard_start = (r, c)
                guard_dir = cell
                break

    # Function to simulate the guard's movement and detect loops
    def simulate(grid, start_pos, start_dir):
        visited_states = set()
        guard_pos = start_pos
        guard_dir = start_dir

        while True:
            # Record the current state
            state = (guard_pos, guard_dir)
            if state in visited_states:
                return True  # Loop detected
            visited_states.add(state)

            # Calculate the next position
            dr, dc = directions[guard_dir]
            next_pos = (guard_pos[0] + dr, guard_pos[1] + dc)

            # Check if the next position is within bounds
            if not (0 <= next_pos[0] < len(grid) and 0 <= next_pos[1] < len(grid[0])):
                return False  # Guard leaves the grid

            # Check for an obstacle
            if grid[next_pos[0]][next_pos[1]] == "#":
                guard_dir = right_turn[guard_dir]  # Turn right
            else:
                guard_pos = next_pos  # Move forward

    # Find all valid obstruction positions
    valid_positions = set()
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            # Skip the guard's starting position
            if (r, c) == guard_start:
                continue

            # Temporarily add an obstruction
            original_cell = grid[r][c]
            grid[r][c] = "#"

            # Simulate guard's movement with the obstruction
            if simulate(grid, guard_start, guard_dir):
                valid_positions.add((r, c))

            # Restore the original cell
            grid[r][c] = original_cell

    return len(valid_positions), valid_positions

# Run the function
count, positions = find_obstruction_positions([list(row) for row in data])
print("Number of valid positions:", count)
print("Valid positions:", positions)