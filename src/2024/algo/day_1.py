def parse_input(input_data):
    return zip(*[(int(a), int(b)) for a, b in [row.split() for row in input_data]])


def part_1(input_data):
    col_a, col_b = parse_input(input_data)
    return sum(abs(a - b) for a, b in zip(sorted(col_a), sorted(col_b)))


def part_2(input_data):
    col_a, col_b = parse_input(input_data)
    return sum(a * col_b.count(a) for a in col_a)
