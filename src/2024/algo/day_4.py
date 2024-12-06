import itertools


def in_range(n, x, y):
    return 0 <= x < n and 0 <= y < n


def part_1(input_data):
    data = list(input_data)
    return sum(
        (dx != 0 or dy != 0)
        and in_range(len(data), x + 3 * dx, y + 3 * dy)
        and data[y][x] == "X"
        and data[y + dy][x + dx] == "M"
        and data[y + 2 * dy][x + 2 * dx] == "A"
        and data[y + 3 * dy][x + 3 * dx] == "S"
        for y in range(len(data))
        for x in range(len(data))
        for dx, dy in itertools.product([-1, 0, 1], [-1, 0, 1])
    )


def part_2(input_data):
    data = list(input_data)
    return sum(
        data[y][x] == "A"
        and (
            data[y - 1][x - 1] in "MS"
            and data[y + 1][x + 1] in "MS"
            and data[y - 1][x - 1] != data[y + 1][x + 1]
        )
        and (
            data[y - 1][x + 1] in "MS"
            and data[y + 1][x - 1] in "MS"
            and data[y - 1][x + 1] != data[y + 1][x - 1]
        )
        for y in range(1, len(data) - 1)
        for x in range(1, len(data) - 1)
    )
