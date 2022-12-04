def part_1(input_data):
    lines = list(input_data)
    return sum(
        int(c) + 1
        for y, line in enumerate(lines)
        for x, c in enumerate(line)
        if (x == 0 or c < line[x - 1])
        and (x == len(line) - 1 or c < line[x + 1])
        and (y == 0 or c < lines[y - 1][x])
        and (y == len(lines) - 1 or c < lines[y + 1][x])
    )


def part_2(input_data):
    def is_low_point(lines: list[str], x: int, y: int):
        line = lines[y]
        c = line[x]
        return (
            (x == 0 or c < line[x - 1])
            and (x == len(line) - 1 or c < line[x + 1])
            and (y == 0 or c < lines[y - 1][x])
            and (y == len(lines) - 1 or c < lines[y + 1][x])
        )

    def basin(
        lines: list[str],
        x: int,
        y: int,
        visited: set[tuple[int, int]] | None = None,
    ) -> set[tuple[int, int]]:
        if visited is None:
            visited = set()

        visited |= {(x, y)}
        if x > 0 and lines[y][x] < lines[y][x - 1] < "9":
            visited |= basin(lines, x - 1, y, visited)
        if x + 1 < len(lines[0]) and lines[y][x] < lines[y][x + 1] < "9":
            visited |= basin(lines, x + 1, y, visited)
        if y > 0 and lines[y][x] < lines[y - 1][x] < "9":
            visited |= basin(lines, x, y - 1, visited)
        if y + 1 < len(lines) and lines[y][x] < lines[y + 1][x] < "9":
            visited |= basin(lines, x, y + 1, visited)
        return visited

    lines = list(input_data)
    flow: dict[tuple[int, int], int] = {}
    low_points = [
        (x, y)
        for y, line in enumerate(lines)
        for x in range(len(line))
        if is_low_point(lines, x, y)
    ]

    result = 1
    for basin_size in sorted((len(basin(lines, x, y)) for (x, y) in low_points))[-3:]:
        result *= basin_size

    return result
