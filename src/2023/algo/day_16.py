NEXT_DIR = {
    "|": {1: [1j, -1j], -1: [1j, -1j], 1j: [1j], -1j: [-1j]},
    "-": {1: [1], -1: [-1], 1j: [1, -1], -1j: [1, -1]},
    "\\": {1: [1j], -1: [-1j], 1j: [1], -1j: [-1]},
    "/": {1: [-1j], -1: [1j], 1j: [-1], -1j: [1]},
    ".": {1: [1], -1: [-1], 1j: [1j], -1j: [-1j]},
}


def parse(input_data):
    input_data = list(input_data)
    height = len(input_data)
    width = len(input_data[0])
    contraption = {
        x + y * 1j: c for y, row in enumerate(input_data) for x, c in enumerate(row)
    }
    return contraption, height, width


def count_energized(contraption, height, width, x_0, delta_0):
    visited = set()
    stack = [(x_0, delta_0)]
    while stack:
        x, delta = stack.pop()
        if x.real < 0 or x.real >= width or x.imag < 0 or x.imag >= height:
            continue
        if (x, delta) in visited:
            continue
        visited.add((x, delta))
        for d in NEXT_DIR[contraption[x]][delta]:
            stack.append((x + d, d))

    return len({x for x, _ in visited})


def part_1(input_data):
    return count_energized(*parse(input_data), 0, 1)


def part_2(input_data):
    contraption, height, width = parse(input_data)
    return max(
        *[count_energized(contraption, height, width, x, 1j) for x in range(width)],
        *[
            count_energized(contraption, height, width, x + (height - 1) * 1j, -1j)
            for x in range(width)
        ],
        *[
            count_energized(contraption, height, width, y * 1j, 1)
            for y in range(height)
        ],
        *[
            count_energized(contraption, height, width, width - 1 + y * 1j, -1)
            for y in range(height)
        ],
    )
