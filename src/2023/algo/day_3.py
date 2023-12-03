from collections import defaultdict


def keep_digits(input_data):
    return ["".join(c if c.isdigit() else "." for c in line) for line in input_data]


def compute_symbol_neighbors(input_data, symbols):
    symbol_neighbors = defaultdict(list)

    for j, line in enumerate(keep_digits(input_data)):
        tokens = line.split(".")
        i = 0
        for token in tokens:
            i += len(token) + 1
            if token == "" or not token.isdigit():
                continue
            for x in range(i - len(token) - 2, i):
                for y in range(j - 1, j + 2):
                    if (x, y) in symbols:
                        symbol_neighbors[(x, y)].append(int(token))

    return symbol_neighbors


def part_1(input_data):
    input_data = list(input_data)
    symbols = {
        (i, j)
        for j, line in enumerate(input_data)
        for i, c in enumerate(line)
        if not c.isdigit() and c != "."
    }

    return sum(
        sum(values) for values in compute_symbol_neighbors(input_data, symbols).values()
    )


def part_2(input_data):
    input_data = list(input_data)

    gears = {
        (i, j)
        for j, line in enumerate(input_data)
        for i, c in enumerate(line)
        if c == "*"
    }

    gear_neighbors = compute_symbol_neighbors(input_data, gears)

    return sum(
        numbers[0] * numbers[1]
        for numbers in gear_neighbors.values()
        if len(numbers) == 2
    )
