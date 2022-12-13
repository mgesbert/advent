from functools import cmp_to_key


def parse(input_data):
    pairs = []
    for line in input_data:
        if not line:
            line = next(input_data)
        pairs.append([eval(line), eval(next(input_data))])

    return pairs


def compare(x, y):
    if isinstance(x, int) and isinstance(y, int):
        return x - y
    if isinstance(x, int):
        x = [x]
    if isinstance(y, int):
        y = [y]
    for a, b in zip(x, y):
        if compare(a, b) != 0:
            return compare(a, b)
    return len(x) - len(y)


def part_1(input_data):
    pairs = parse(input_data)

    return sum(i for i, pair in enumerate(pairs, start=1) if compare(*pair) <= 0)


def part_2(input_data):
    signals = sorted(
        [x for pair in parse(input_data) for x in pair] + [[[2]], [[6]]],
        key=cmp_to_key(compare),
    )

    return next(
        i * j
        for i, x in enumerate(signals, start=1)
        if x == [[2]]
        for j, y in enumerate(signals, start=1)
        if y == [[6]]
    )
