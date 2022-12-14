def debug(walls, cave):
    min_x = int(min(c.real for c in cave))
    max_x = int(max(c.real for c in cave))
    max_y = int(max(c.imag for c in cave))
    for y in range(max_y + 2):
        for x in range(min_x, max_x + 1):
            print(
                "█" if x + 1j * y in walls else "▒" if x + 1j * y in cave else " ",
                end="",
            )
        print()


def parse(input_data):
    cave = set()
    for line in input_data:
        points = line.split(" -> ")
        for p1, p2 in zip(points[:-1], points[1:]):
            x1, y1 = map(int, p1.split(","))
            x2, y2 = map(int, p2.split(","))
            for x in range(min(x1, x2), max(x1, x2) + 1):
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    cave.add(x + 1j * y)

    return cave


def part_1(input_data):
    elements = parse(input_data)
    walls = {*elements}

    while True:
        sand_grain = 500
        while True:
            if all(x.imag < sand_grain.imag for x in elements):
                # debug(walls, elements)
                return len(elements - walls)
            if sand_grain + 1j not in elements:
                sand_grain += 1j
                continue
            if sand_grain + 1j - 1 not in elements:
                sand_grain += 1j - 1
                continue
            if sand_grain + 1j + 1 not in elements:
                sand_grain += 1j + 1
                continue
            elements.add(sand_grain)
            break


def part_2(input_data):
    elements = parse(input_data)
    walls = {*elements}

    max_y = max(c.imag for c in elements)

    while True:
        sand_grain = 500
        while True:
            if sand_grain.imag == max_y + 1:
                elements.add(sand_grain)
                break
            if sand_grain + 1j not in elements:
                sand_grain += 1j
                continue
            if sand_grain + 1j - 1 not in elements:
                sand_grain += 1j - 1
                continue
            if sand_grain + 1j + 1 not in elements:
                sand_grain += 1j + 1
                continue
            elements.add(sand_grain)
            if sand_grain == 500:
                # debug(walls, elements)
                return len(elements - walls)
            break
