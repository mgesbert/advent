import networkx as nx  # type: ignore
from advent_2021.helpers import get_input


def manhattan_dist(a: tuple[int, int], b: tuple[int, int]):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


if __name__ == "__main__":
    cave = [[int(x) for x in line] for line in get_input()]
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
    print(sum(cave[y][x] for x, y in path[1:]))
