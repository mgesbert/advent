def in_bounds(c, x, y):
    return 0 <= c.real < x and 0 <= c.imag < y


def roll(balls, cubes, x, y, delta):
    result = set()
    for c in sorted(
        balls, key=lambda x: x.real * delta.real + x.imag * delta.imag, reverse=True
    ):
        steps = 0
        while c + (steps + 1) * delta not in cubes | result and in_bounds(
            c + (steps + 1) * delta, x, y
        ):
            steps += 1
        result.add(c + steps * delta)
    return result


def parse_input(input_data):
    balls = set()
    cubes = set()
    x = y = 0
    for j, line in enumerate(input_data):
        x = len(line)
        y += 1
        for i, c in enumerate(line):
            if c == "#":
                cubes.add(i + j * 1j)
            if c == "O":
                balls.add(i + j * 1j)
    return balls, cubes, x, y


def load(balls, y):
    return int(sum((y - c.imag) for c in balls))


def part_1(input_data):
    balls, cubes, x, y = parse_input(input_data)
    balls = roll(balls, cubes, x, y, -1j)
    return load(balls, y)


def part_2(input_data):
    balls, cubes, x, y = parse_input(input_data)
    visited = []
    while True:
        for d in [-1j, -1, 1j, 1]:
            balls = roll(balls, cubes, x, y, d)
        if balls not in visited:
            visited.append(balls)
            continue
        cycle_start = visited.index(balls)
        cycle_length = len(visited) - cycle_start
        final_state = visited[
            cycle_start + (1000000000 - cycle_start) % cycle_length - 1
        ]
        return load(final_state, y)
