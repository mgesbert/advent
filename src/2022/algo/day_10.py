def part_1(input_data):
    acc = 0
    cycle = 0
    value = 1
    for line in input_data:
        cycle += 1
        if cycle % 40 == 20:
            acc += value * cycle
        if line == "noop":
            continue
        cycle += 1
        if cycle % 40 == 20:
            acc += value * cycle
        value += int(line[5:])
    return acc


def part_2(input_data):
    acc = ""
    cycle = -1
    value = 1
    for line in input_data:
        cycle += 1
        if cycle % 40 == 0:
            acc += "\n"
        acc += "#" if value - 1 <= cycle % 40 <= value + 1 else "."
        if line == "noop":
            continue
        cycle += 1
        if cycle % 40 == 0:
            acc += "\n"
        acc += "#" if value - 1 <= cycle % 40 <= value + 1 else "."
        value += int(line[5:])
    return acc
