DIRECTIONS = {"U": -1j, "R": 1, "D": 1j, "L": -1}


def compute_area(instructions):
    x = 0
    area = 0
    perimeter = 0
    for direction, steps in instructions:
        offset = DIRECTIONS[direction]
        # tracking the abscissa of the edge (we only care about vertical edges)
        x += int(offset.real) * int(steps)
        # by summing the area of the rectangles, we get the area of interior plus the top and right edges
        area += int(offset.imag) * int(steps) * x
        perimeter += int(steps)

    # let's add the left and bottom edges, plus the top left corner
    return int(area + perimeter / 2 + 1)


def part_1(input_data):
    return compute_area(
        [[chunk[0], int(chunk[1])] for chunk in [row.split() for row in input_data]]
    )


def part_2(input_data):
    return compute_area(
        [
            ["RDLU"[int(chunk[2][-2])], int(chunk[2][2:-2], base=16)]
            for chunk in [row.split() for row in input_data]
        ]
    )
