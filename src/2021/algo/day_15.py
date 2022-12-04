import networkx as nx  # type: ignore


def manhattan_dist(a: tuple[int, int], b: tuple[int, int]):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def part_1(input_data):
    cave = [[int(x) for x in line] for line in input_data]
    width = len(cave[0])
    height = len(cave)
    size = width * height

    G = nx.DiGraph()

    for y, line in enumerate(cave):
        for x, dist in enumerate(line):
            if x > 0:
                G.add_edge((x - 1, y), (x, y), weight=dist)  # type: ignore
            if x < width - 1:
                G.add_edge((x + 1, y), (x, y), weight=dist)  # type: ignore
            if y > 0:
                G.add_edge((x, y - 1), (x, y), weight=dist)  # type: ignore
            if y < height - 1:
                G.add_edge((x, y + 1), (x, y), weight=dist)  # type: ignore

    path = nx.astar_path(G, (0, 0), (width - 1, height - 1), manhattan_dist)  # type: ignore
    return sum(cave[y][x] for x, y in path[1:])


def part_2(input_data):
    def get_cave(cave: list[list[int]], cave_x: int, cave_y: int):
        width = len(cave[0])
        height = len(cave)
        return [
            [(cave[y][x] + cave_x + cave_y - 1) % 9 + 1 for x in range(width)]
            for y in range(height)
        ]

    cave = [[int(x) for x in line] for line in input_data]

    whole_cave: list[list[int]] = [[] for _ in range(len(cave) * 5)]
    for cave_y in range(5):
        for cave_x in range(5):
            local_cave = get_cave(cave, cave_x, cave_y)
            for y, line in enumerate(local_cave):
                whole_cave[len(cave) * cave_y + y] += line

    width = len(whole_cave[0])
    height = len(whole_cave)
    size = width * height

    G = nx.DiGraph()

    for y, line in enumerate(whole_cave):
        for x, dist in enumerate(line):
            if x > 0:
                G.add_edge((x - 1, y), (x, y), weight=dist)  # type: ignore
            if x < width - 1:
                G.add_edge((x + 1, y), (x, y), weight=dist)  # type: ignore
            if y > 0:
                G.add_edge((x, y - 1), (x, y), weight=dist)  # type: ignore
            if y < height - 1:
                G.add_edge((x, y + 1), (x, y), weight=dist)  # type: ignore

    path = nx.astar_path(G, (0, 0), (width - 1, height - 1), manhattan_dist)  # type: ignore
    return sum(whole_cave[y][x] for x, y in path[1:])
