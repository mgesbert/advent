def parse_input(input_data):
    return {
        x + 1j * y: c for y, row in enumerate(input_data) for x, c in enumerate(row)
    }


def traverse(area):
    z = next(z for z, c in area.items() if c == "^")
    direction = -1j
    while True:
        yield z, direction
        if (z + direction) not in area:
            return
        while area[z + direction] == "#":
            direction *= 1j
        z += direction


def is_loop(base_area, pos):
    area = {
        **base_area,
        pos: "#",
    }
    visited = set()
    for z, direction in traverse(area):
        if (z, direction) in visited:
            return True
        visited.add((z, direction))
    return False


def part_1(input_data):
    area = parse_input(input_data)
    return len({z for z, _ in traverse(area)})


def part_2(input_data):
    area = parse_input(input_data)
    path_positions = {z for z, _ in traverse(area)}
    return sum(is_loop(area, pos) for pos in path_positions if area[pos] == ".")
