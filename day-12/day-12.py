import networkx as nx

# import matplotlib as plt

with open("input.txt") as f:
    data = f.read().strip()

data1 = """RRRRIICCFF\n
RRRRIICCCF\n
VVRRRCCFFF\n
VVRCCCJFFF\n
VVVVCJJCFE\n
VVIVCCJJEE\n
VVIIICJJEE\n
MIIIIIJJEE\n
MIIISIJEEE\n
MMMISSJEEE"""


# https://networkx.org/documentation/stable/tutorial.html

def create_grid(raw_grid):
    grid = {}
    for i, line in enumerate(raw_grid.splitlines()):
        for j, char in enumerate(line):
            grid[(i + 1j * j)] = char
    print(grid)
    return grid


def make_graph(board: dict, directions):
    G = nx.Graph()
    # add edges
    for pos in board:
        for direction in directions:
            # calculate potential neighbor by adding the direction offset
            neighbors = pos + direction
            # only add if exists in the boards
            if board[pos] == board.get(neighbors):
                G.add_edge(pos, neighbors)
    # add all n "nodes" from the board so they are included at least explicitly as they are not part of the edges
    G.add_nodes_from(board.keys())
    return G


def get_walls(component, directions):
    walls = set()
    for pos in component:
        for direction in directions:
            neighbors = pos + direction
            if neighbors not in component:
                walls.add((pos, direction * 1j))

    return walls


def calculate_walls(G: nx.Graph, directions):
    price = 0
    price_part_two = 0

    for component in nx.connected_components(G):
        walls = get_walls(component, directions)
        price += len(component) * len(walls)

        internal_walls = 0
        for pos, direction in walls:
            if (pos + direction, direction) not in walls:
                internal_walls += 1

        price_part_two += len(component) * internal_walls

    return price, price_part_two

directions = {1, -1, 1j, -1j}
grid = create_grid(data)
graph = make_graph(grid, directions)
r1, r2 = calculate_walls(graph, directions)
print(f"part one {r1}")
# 1489582

print(f"part two {r2}")
# nx.draw(G)
