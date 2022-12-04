def part_1(input_data):
    data = list(map(int, input_data))
    return sum(a < b for a, b in zip(data[:-1], data[1:]))


def part_2(input_data):
    data = list(map(int, input_data))
    return sum(
        sum(data[i : i + 3]) < sum(data[i + 1 : i + 4]) for i in range(len(data) - 3)
    )
