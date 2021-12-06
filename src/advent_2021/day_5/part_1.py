from collections import defaultdict

from advent_2021.helpers import get_input


if __name__ == "__main__":
    floor_map: dict[int, dict[int, int]] = defaultdict(lambda: defaultdict(int))
    for line in get_input():
        start, end = line.split(" -> ")
        x1, y1 = map(int, start.split(","))
        x2, y2 = map(int, end.split(","))
        if x1 != x2 and y1 != y2:
            continue
        x1, x2 = sorted([x1, x2])
        y1, y2 = sorted([y1, y2])
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                floor_map[y][x] += 1

    print(sum(n > 1 for row in floor_map.values() for n in row.values()))
