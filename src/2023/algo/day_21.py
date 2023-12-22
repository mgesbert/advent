def part_1(input_data):
    rocks = set()
    height = width = start = 0

    for j, line in enumerate(input_data):
        height += 1
        width = len(line)
        for i, c in enumerate(line):
            if c == "#":
                rocks.add(i + j * 1j)
            if c == "S":
                start = i + j * 1j

    positions = {start}
    for _ in range(64):
        positions = {
            pos + 1j**i
            for pos in positions
            for i in range(4)
            if pos + 1j**i not in rocks
            and 0 <= (pos + 1j**i).real < width
            and 0 <= (pos + 1j**i).imag < height
        }

    return len(positions)


def is_rock(pos, rocks, width, height):
    return (pos.real % width) + (pos.imag % height) * 1j in rocks


def part_2(input_data):
    rocks = set()

    start = 0
    for j, line in enumerate(input_data):
        width = len(line)
        for i, c in enumerate(line):
            if c == "#":
                rocks.add(i + j * 1j)
            if c == "S":
                start = i + j * 1j

    DIM = 131

    positions = {start}
    results = []
    for i in range(DIM // 2 + 2 * DIM):
        positions = {
            pos + 1j**i
            for pos in positions
            for i in range(4)
            if (pos + 1j**i).real % DIM + ((pos + 1j**i).imag % DIM) * 1j
            not in rocks
        }
        if (i + 1) % DIM == DIM // 2:
            results.append(len(positions))

    nb_rounds = 26501365
    n = (nb_rounds - (DIM - 1) // 2) // DIM
    nb_odd_inner_diamonds = (n + 1) ** 2
    nb_even_inner_diamonds = n**2
    nb_outer_diamonds = 2 * n**2 + 2 * n
    n1, n2, n3 = results
    O = n1
    E = 3 * n1 - 3 * n2 + n3
    X = (-21 * n1 + 12 * n2 - 3 * n3) // 12
    return (
        nb_odd_inner_diamonds * O + nb_even_inner_diamonds * E + nb_outer_diamonds * X
    )
