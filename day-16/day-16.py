import networkx as nx
with open("input.txt") as f:
    raw_grid = f.read().strip().split("\n")

directions = {-1, 1, -1j, 1j}

# trying with this package again
#https://networkx.org/documentation/stable/reference/algorithms/shortest_paths.html

def make_maze(grid):
    # can hold directed edges
    # spend too long trying to find why I got the wrong result until I found this in the documentation'
    # part one works anyway
    graph = nx.DiGraph()

    for i, line in enumerate(grid):
        for j, char in enumerate(line):
            if char == "#":
                continue
            ij = complex(i + j * 1j)
            if char == "S":
                # add initial direction
                s = (ij, 1j)
            if char == "E":
                e = ij
            for direction in directions:
                # adds node to graph. the tuple consists of ij which is the position on the grid
                # and direction represents a possible direction
                graph.add_node((ij, direction))

    return graph, s, e


def simulate(maze: nx.Graph, start, end):
    for position, direction in maze.nodes:
        # check if next position in current direction exists in the maze
        if (position + direction, direction) in maze.nodes:
            # add directed edge from current node to next node
            # weight is the cost of moving (every step in the maze adds one point)
            maze.add_edge((position, direction), (position + direction, direction), weight=1)
        # two possible rotations right (1j) and left turn (-1j)
        # add edge from current node to the same position but with direction rotated
        # wight of 1000 tells the graph that turning is more expensive than moving forward (again the cost of turning in maze)
        maze.add_edge((position, direction), (position, -1j * direction), weight=1000)
        maze.add_edge((position, direction), (position, 1j * direction), weight=1000)

    # connect the end node, just giving it the end as position does not work
    # also seems like the end does not add a point
    for direction in directions:
        maze.add_edge((end, direction), 'end', weight=0)


    # use the shortest path with length as the goal is getting the length
    # https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.shortest_paths.generic.shortest_path_length.html#networkx.algorithms.shortest_paths.generic.shortest_path_length
    total_part_one = nx.shortest_path_length(maze, start, 'end', weight="weight")

    # use networkx to compute all shortest paths
    paths = nx.all_shortest_paths(maze, start, 'end', weight="weight")
    unique_positions = set()
    for path in paths:

        # [:-1] this actually excludes the end from the path as this is not wanted
        for z, _ in path[:-1]:
            unique_positions.add(z)

    return total_part_one, len(unique_positions)

part_one, part_two = simulate(*make_maze(raw_grid))
print(f"part one {part_one}")
# 73404
print(f"part two {part_two}")
# 449