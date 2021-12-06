from collections import defaultdict

from advent_2021.helpers import get_input


if __name__ == "__main__":
    floor_map: dict[int, dict[int, int]] = defaultdict(lambda: defaultdict(int))
    for line in get_input():
        start, end = line.split(" -> ")
        x1, y1 = map(int, start.split(","))
        x2, y2 = map(int, end.split(","))

        if x1 != x2 and y1 != y2 and abs(x2 - x1) != abs(y2 - y1):
            continue

        x_step = -1 if x1 > x2 else 1
        y_step = -1 if y1 > y2 else 1
        x_range = (
            range(x1, x2 + x_step, x_step) if x1 != x2 else [x1] * (abs(y2 - y1) + 1)
        )
        y_range = (
            range(y1, y2 + y_step, y_step) if y1 != y2 else [y1] * (abs(x2 - x1) + 1)
        )

        for x, y in zip(x_range, y_range):
            floor_map[y][x] += 1

    print(sum(n > 1 for row in floor_map.values() for n in row.values()))
