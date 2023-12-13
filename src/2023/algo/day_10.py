DIR_CHARS = {
    "|": "NS",
    "-": "EW",
    "L": "NE",
    "J": "NW",
    "7": "SW",
    "F": "SE",
    "S": "NSEW",
    ".": "",
}


def start_neighbours(map_, x, y):
    if x > 0 and "E" in DIR_CHARS[map_[y][x - 1]]:
        yield x - 1, y
    if x < len(map_[0]) - 1 and "W" in DIR_CHARS[map_[y][x + 1]]:
        yield x + 1, y
    if y > 0 and "S" in DIR_CHARS[map_[y - 1][x]]:
        yield x, y - 1
    if y < len(map_) - 1 and "N" in DIR_CHARS[map_[y + 1][x]]:
        yield x, y + 1


def next_node(map_, x, y, prev_x, prev_y):
    if "E" in DIR_CHARS[map_[y][x]] and prev_x != x + 1:
        return x + 1, y
    if "W" in DIR_CHARS[map_[y][x]] and prev_x != x - 1:
        return x - 1, y
    if "S" in DIR_CHARS[map_[y][x]] and prev_y != y + 1:
        return x, y + 1
    return x, y - 1


def part_1(input_data):
    map_ = list(input_data)
    x, y = next(
        (i, j) for j, row in enumerate(map_) for i, c in enumerate(row) if c == "S"
    )
    print(list(start_neighbours(map_, x, y)))
    (x1, y1), (x2, y2) = start_neighbours(map_, x, y)
    prev_x1, prev_y1 = prev_x2, prev_y2 = x, y
    distance = 1
    while (x1, y1) != (x2, y2):
        (x1, y1), (prev_x1, prev_y1) = next_node(map_, x1, y1, prev_x1, prev_y1), (
            x1,
            y1,
        )
        (x2, y2), (prev_x2, prev_y2) = next_node(map_, x2, y2, prev_x2, prev_y2), (
            x2,
            y2,
        )
        distance += 1
    return distance


def part_2(input_data):
    map_ = [[c for c in x] for x in input_data]
    x, y = next(
        (i, j) for j, row in enumerate(map_) for i, c in enumerate(row) if c == "S"
    )
    loop_nodes = set()
    (x1, y1), _ = start_neighbours(map_, x, y)
    map_[y][x] = (
        "F"
        if "W" in DIR_CHARS[map_[y][x + 1]] and "N" in DIR_CHARS[map_[y + 1][x]]
        else "7"
        if "E" in DIR_CHARS[map_[y][x - 1]] and "N" in DIR_CHARS[map_[y + 1][x]]
        else "L"
        if "W" in DIR_CHARS[map_[y][x + 1]] and "S" in DIR_CHARS[map_[y - 1][x]]
        else "J"
        if "E" in DIR_CHARS[map_[y][x - 1]] and "S" in DIR_CHARS[map_[y - 1][x]]
        else "-"
        if "E" in DIR_CHARS[map_[y][x - 1]] and "W" in DIR_CHARS[map_[y][x + 1]]
        else "|"
    )
    prev_x1, prev_y1 = x, y
    while (x1, y1) not in loop_nodes:
        loop_nodes.add((x1, y1))
        (x1, y1), (prev_x1, prev_y1) = next_node(map_, x1, y1, prev_x1, prev_y1), (
            x1,
            y1,
        )
    loop_area = 0
    for y in range(len(map_)):
        inside_loop = False
        looping_dir = None
        for x in range(len(map_[0])):
            c = map_[y][x]
            if (x, y) not in loop_nodes:
                loop_area += inside_loop

            elif c == "|":
                looping_dir = None
                inside_loop = not inside_loop

            elif c == "F":
                looping_dir = "N"

            elif c == "L":
                looping_dir = "S"

            elif c == "J":
                if looping_dir == "N":
                    inside_loop = not inside_loop
                looping_dir = None

            elif c == "7":
                if looping_dir == "S":
                    inside_loop = not inside_loop
                looping_dir = None

    return loop_area
