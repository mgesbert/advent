def next_value(values):
    deltas = [b - a for a, b in zip(values[:-1], values[1:])]
    if all(delta == 0 for delta in deltas):
        return values[-1]
    return values[-1] + next_value(deltas)


def part_1(input_data):
    return sum(next_value([int(c) for c in line.split()]) for line in input_data)


def previous_value(values):
    deltas = [b - a for a, b in zip(values[:-1], values[1:])]
    if all(delta == 0 for delta in deltas):
        return values[0]
    return values[0] - previous_value(deltas)


def part_2(input_data):
    return sum(previous_value([int(c) for c in line.split()]) for line in input_data)
