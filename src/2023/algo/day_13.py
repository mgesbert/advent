def get_columns(lines):
    return ["".join(line[i] for line in lines) for i in range(len(lines[0]))]


def parse_input(input_data):
    lines = []
    for line in input_data:
        if line.strip():
            lines.append(line)
            continue
        yield lines, get_columns(lines)
        lines = []
    yield lines, get_columns(lines)


def is_reflection(lines, i, diff):
    return sum(
        c1 != c2
        for l1, l2 in zip(lines[:i][::-1], lines[i:])
        for c1, c2 in zip(l1, l2)
    ) == diff


def get_score(lines, diff):
    for i in range(1, len(lines)):
        if is_reflection(lines, i, diff):
            return i
    return 0


def part_1(input_data):
    return sum(100 * get_score(lines, 0) or get_score(cols, 0) for lines, cols in parse_input(input_data))


def part_2(input_data):
    return sum(100 * get_score(lines, 1) or get_score(cols, 1) for lines, cols in parse_input(input_data))
