import re

import numpy as np

BUTTON_A_PATTERN = r"Button A: X\+(\d+), Y\+(\d+)"
BUTTON_B_PATTERN = r"Button B: X\+(\d+), Y\+(\d+)"
PRIZE_PATTERN = r"Prize: X=(\d+), Y=(\d+)"


def parse_input(input_data, offset=0):
    while True:
        x1, y1 = map(int, re.match(BUTTON_A_PATTERN, next(input_data)).groups())
        x2, y2 = map(int, re.match(BUTTON_B_PATTERN, next(input_data)).groups())
        x3, y3 = map(int, re.match(PRIZE_PATTERN, next(input_data)).groups())

        yield np.array([[x1, x2], [y1, y2]]), np.array([x3 + offset, y3 + offset])

        try:
            next(input_data)
        except StopIteration:
            return


def solve(input_data, offset=0):
    tokens = 0
    for x, y in parse_input(input_data, offset=offset):
        a, b = np.linalg.solve(x, y)
        if abs(a - round(a)) > 1e-4 or abs(b - round(b)) > 1e-4:
            continue
        tokens += int(round(a)) * 3 + int(round(b))
    return tokens


def part_1(input_data):
    return solve(input_data)


def part_2(input_data):
    return solve(input_data, offset=10000000000000)
