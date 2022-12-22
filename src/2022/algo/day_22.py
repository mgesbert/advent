import re


def part_1(input_data):
    DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    *world, _, instructions = list(input_data)
    width = max(len(l) for l in world)
    height = len(world)
    world = [l.ljust(width) for l in world]

    x = world[0].index(".")
    y = 0
    dx, dy = DIRECTIONS[0]

    for instruction in re.findall(r"(\d+|[RL])", instructions):
        if instruction.isdigit():
            for _ in range(int(instruction)):
                next_x, next_y = (x + dx) % width, (y + dy) % height
                while world[next_y][next_x] == " ":
                    next_x, next_y = (next_x + dx) % width, (next_y + dy) % height
                if world[next_y][next_x] == "#":
                    break
                x, y = next_x, next_y
        else:
            dx, dy = DIRECTIONS[
                (DIRECTIONS.index((dx, dy)) + (1 if instruction == "R" else -1))
                % len(DIRECTIONS)
            ]

    return 1000 * (y + 1) + 4 * (x + 1) + DIRECTIONS.index((dx, dy))


# using a class is over-engineered in the end, but I'm too tired to simplify it
# idea: points are (x, y), DIRECTIONS = {'up': {(x1,y1): (x2,y2), ...}, 'right': ...}
class Point:
    right = down = left = up = None

    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value

    def __repr__(self):
        return f"{self.x} {self.y} {self.value}"

    def __hash__(self) -> int:
        return self.x * 1000000 + self.y


def part_2(input_data):
    DIRECTIONS = ["right", "down", "left", "up"]
    *world, _, instructions = list(input_data)
    width = max(len(l) for l in world)
    world = [l.ljust(width) for l in world]

    points = {}
    for y, line in enumerate(world):
        for x, value in enumerate(line):
            if value == " ":
                continue
            point = Point(x, y, value)
            if (x - 1, y) in points:
                point.left = points[x - 1, y]
                points[x - 1, y].right = point
            if (x, y - 1) in points:
                point.up = points[x, y - 1]
                points[x, y - 1].down = point
            points[x, y] = point

    change_dir = {}
    if len(world) == 12:  # sample
        for n in range(4):
            points[11, n].right = points[15, 11 - n]
            points[11, 4 + n].right = points[15 - n, 8]
            points[15, 11 - n].right = points[11, n]

            points[8, n].left = points[4 + n, 4]
            points[0, 4 + n].left = points[15 - n, 11]
            points[8, 8 + n].left = points[7 - n, 7]

            points[n, 4].up = points[8 + n, 0]
            points[4 + n, 4].up = points[8, n]
            points[8 + n, 0].up = points[n, 4]
            points[15 - n, 8].up = points[11, 4 + n]

            points[n, 7].down = points[11 - n, 11]
            points[7 - n, 7].down = points[8, 8 + n]
            points[11 - n, 11].down = points[n, 7]
            points[15 - n, 11].down = points[0, 4 + n]

        change_dir = (
            {(points[11, y], "right"): "left" for y in range(4)}
            | {(points[11, y], "right"): "down" for y in range(4, 8)}
            | {(points[15, y], "right"): "left" for y in range(8, 12)}
            | {(points[8, y], "left"): "down" for y in range(4)}
            | {(points[0, y], "left"): "up" for y in range(4, 8)}
            | {(points[8, y], "left"): "up" for y in range(8, 12)}
            | {(points[x, 4], "up"): "down" for x in range(4)}
            | {(points[x, 4], "up"): "right" for x in range(4, 8)}
            | {(points[x, 0], "up"): "down" for x in range(8, 12)}
            | {(points[x, 8], "up"): "left" for x in range(12, 16)}
            | {(points[x, 7], "down"): "up" for x in range(4)}
            | {(points[x, 7], "down"): "right" for x in range(4, 8)}
            | {(points[x, 11], "down"): "up" for x in range(8, 12)}
            | {(points[x, 11], "down"): "right" for x in range(12, 16)}
        )
    else:  # data
        for n in range(50):
            points[149, n].right = points[99, 149 - n]
            points[99, 50 + n].right = points[100 + n, 49]
            points[99, 149 - n].right = points[149, n]
            points[49, 150 + n].right = points[50 + n, 149]

            points[50, n].left = points[0, 149 - n]
            points[50, 50 + n].left = points[n, 100]
            points[0, 149 - n].left = points[50, n]
            points[0, 150 + n].left = points[50 + n, 0]

            points[n, 100].up = points[50, 50 + n]
            points[50 + n, 0].up = points[0, 150 + n]
            points[100 + n, 0].up = points[n, 199]

            points[n, 199].down = points[100 + n, 0]
            points[50 + n, 149].down = points[49, 150 + n]
            points[100 + n, 49].down = points[99, 50 + n]

        change_dir = (
            {(points[149, y], "right"): "left" for y in range(50)}
            | {(points[99, y], "right"): "up" for y in range(50, 100)}
            | {(points[99, y], "right"): "left" for y in range(100, 150)}
            | {(points[49, y], "right"): "up" for y in range(150, 200)}
            | {(points[50, y], "left"): "right" for y in range(50)}
            | {(points[50, y], "left"): "down" for y in range(50, 100)}
            | {(points[0, y], "left"): "right" for y in range(100, 150)}
            | {(points[0, y], "left"): "down" for y in range(150, 200)}
            | {(points[x, 100], "up"): "right" for x in range(50)}
            | {(points[x, 0], "up"): "right" for x in range(50, 100)}
            | {(points[x, 0], "up"): "up" for x in range(100, 150)}
            | {(points[x, 199], "down"): "down" for x in range(50)}
            | {(points[x, 149], "down"): "left" for x in range(50, 100)}
            | {(points[x, 49], "down"): "left" for x in range(100, 150)}
        )

    point = [x for x in points.values()][0]
    direction = "right"

    for instruction in re.findall(r"(\d+|[RL])", instructions):
        if instruction.isdigit():
            for _ in range(int(instruction)):
                next_point = getattr(point, direction)
                if next_point.value == "#":
                    break
                direction = change_dir.get((point, direction), direction)
                point = next_point
        else:
            direction = DIRECTIONS[
                (DIRECTIONS.index(direction) + (1 if instruction == "R" else -1))
                % len(DIRECTIONS)
            ]

    return 1000 * (point.y + 1) + 4 * (point.x + 1) + DIRECTIONS.index(direction)
