import itertools
import math


def parse_input(input_data):
    area = {
        x + 1j * y: c for y, row in enumerate(input_data) for x, c in enumerate(row)
    }
    antennas = {
        c: [z for z in area.keys() if area[z] == c]
        for c in set(area.values())
        if c not in "#."
    }
    width = int(max(x.real for x in area.keys())) + 1
    height = int(max(x.imag for x in area.keys())) + 1
    return antennas, width, height


def in_area(z, width, height):
    return 0 <= z.real < width and 0 <= z.imag < height


def part_1(input_data):
    antennas, width, height = parse_input(input_data)
    antinodes = {
        a + (a - b)
        for _, coords in antennas.items()
        for a, b in itertools.product(coords, repeat=2)
        if a != b and in_area(a + (a - b), width, height)
    }
    return len(antinodes)


def part_2(input_data):
    antennas, width, height = parse_input(input_data)
    antinodes = set()
    for coords in antennas.values():
        for a, b in itertools.combinations(coords, 2):
            vector = (b - a) / math.gcd(int((b - a).real), int((b - a).imag))
            pos = a
            while in_area(pos := pos + vector, width, height):
                antinodes.add(pos)
            pos = b
            while in_area(pos := pos - vector, width, height):
                antinodes.add(pos)
    return len(antinodes)
