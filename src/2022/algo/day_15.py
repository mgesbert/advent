import re


def manhattan(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x2 - x1) + abs(y2 - y1)


def parse(input_data):
    sensor_to_beacon = {}
    for line in input_data:
        match = re.match(
            r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)",
            line,
        )
        if not match:
            continue
        sx, sy, bx, by = map(int, match.groups())
        sensor_to_beacon[(sx, sy)] = (bx, by)
    return sensor_to_beacon


def intersect_row_and_diamond(sensor, beacon, y):
    radius = manhattan(sensor, beacon)
    dy = abs(sensor[1] - y)
    if dy > radius:
        return None
    return (
        sensor[0] - (radius - dy),
        sensor[0] + (radius - dy),
    )


def exclude(segment, invalid_positions):
    invalid_positions = sorted(invalid_positions + [segment])
    while True:
        for i, ((a1, a2), (b1, b2)) in enumerate(
            zip(invalid_positions[:-1], invalid_positions[1:])
        ):
            if b1 <= a2:
                invalid_positions = (
                    invalid_positions[:i]
                    + [(a1, max(a2, b2))]
                    + invalid_positions[i + 2 :]
                )
                break
        else:
            return invalid_positions


def compute_invalid_positions(sensor_to_beacon, row):
    invalid_positions = []

    for sensor, beacon in sensor_to_beacon.items():
        segment = intersect_row_and_diamond(sensor, beacon, row)
        if not segment:
            continue
        invalid_positions = exclude(segment, invalid_positions)

    return invalid_positions


def part_1(input_data):
    row = int(next(input_data))
    sensor_to_beacon = parse(input_data)

    invalid_positions = compute_invalid_positions(sensor_to_beacon, row)

    return sum(abs(x2 - x1) + 1 for x1, x2 in invalid_positions) - sum(
        y == row and any(x1 <= x <= x2 for x1, x2 in invalid_positions)
        for x, y in set(sensor_to_beacon.values())
    )


def part_2(input_data):
    row = int(next(input_data))
    max_y = 2 * row
    sensor_to_beacon = parse(input_data)

    for y in range(max_y):
        invalid_positions = compute_invalid_positions(sensor_to_beacon, y)

        if len(invalid_positions) == 2:
            return (invalid_positions[0][1] + 1) * 4000000 + y
