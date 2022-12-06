def part_1(input_data):
    line = next(input_data)
    return next(i for i in range(4, len(line)) if len(set(line[i - 4 : i])) == 4)


def part_2(input_data):
    line = next(input_data)
    return next(i for i in range(14, len(line)) if len(set(line[i - 14 : i])) == 14)
