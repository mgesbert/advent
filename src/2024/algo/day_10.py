def _get_valid_neighbors(area, x, y, z):
    height, width = len(area), len(area[0])
    return [
        (x + dx, y + dy)
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]
        if 0 <= x + dx < width
        and 0 <= y + dy < height
        and area[y + dy][x + dx] == z + 1
    ]


def list_summits(area, x, y) -> set[tuple[int, int]]:
    z = area[y][x]
    if z == 9:
        return {(x, y)}

    return {
        summit
        for next_x, next_y in _get_valid_neighbors(area, x, y, z)
        for summit in list_summits(area, next_x, next_y)
    }


def count_paths(area, x, y):
    z = area[y][x]
    if z == 9:
        return 1

    return sum(
        count_paths(area, next_x, next_y)
        for next_x, next_y in _get_valid_neighbors(area, x, y, z)
    )


def parse_input(input_data) -> list[list[int]]:
    return [[int(cell) for cell in row] for row in list(input_data)]


def part_1(input_data):
    area = parse_input(input_data)
    return sum(
        len(list_summits(area, x, y))
        for y, row in enumerate(area)
        for x, cell in enumerate(row)
        if cell == 0
    )


def part_2(input_data):
    area = parse_input(input_data)
    return sum(
        count_paths(area, x, y)
        for y, row in enumerate(area)
        for x, cell in enumerate(row)
        if cell == 0
    )
