import itertools


def manhattan(p1, p2):
    return sum(abs(c1 - c2) for c1, c2 in zip(p1, p2))


def parse_input(input_data, spread_factor):
    universe = list(input_data)
    galaxies = [
        (x, y)
        for y, line in enumerate(universe)
        for x, c in enumerate(line)
        if c == "#"
    ]
    galaxy_x = {x for x, _ in galaxies}
    galaxy_y = {y for _, y in galaxies}

    for x in range(len(universe[0]))[::-1]:
        if x not in galaxy_x:
            galaxies = [
                (i, j) if i < x else (i + spread_factor - 1, j) for i, j in galaxies
            ]

    for y in range(len(universe))[::-1]:
        if y not in galaxy_y:
            galaxies = [
                (i, j) if j < y else (i, j + spread_factor - 1) for i, j in galaxies
            ]

    return galaxies


def part_1(input_data):
    return sum(
        manhattan(g1, g2)
        for g1, g2 in itertools.combinations(parse_input(input_data, 2), 2)
    )


def part_2(input_data):
    return sum(
        manhattan(g1, g2)
        for g1, g2 in itertools.combinations(parse_input(input_data, 1_000_000), 2)
    )
