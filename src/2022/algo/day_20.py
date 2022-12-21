def part_1(input_data):
    data = list(enumerate(map(int, input_data)))
    for i, n in [*data]:
        index = data.index((i, n))
        data.remove((i, n))
        data.insert((index + n) % len(data) or len(data), (i, n))

    mixed_data = [n for _, n in data]
    zero_index = mixed_data.index(0)
    return (
        mixed_data[(1000 + zero_index) % len(mixed_data)]
        + mixed_data[(2000 + zero_index) % len(mixed_data)]
        + mixed_data[(3000 + zero_index) % len(mixed_data)]
    )


def part_2(input_data):
    data = [(i, int(line) * 811589153) for i, line in enumerate(input_data)]
    for _ in range(10):
        for i, n in sorted(data):
            index = data.index((i, n))
            data.remove((i, n))
            data.insert(
                (index + n) % len(data) or (0 if index + n == 0 else len(data)), (i, n)
            )

    mixed_data = [n for _, n in data]
    zero_index = mixed_data.index(0)
    return (
        mixed_data[(1000 + zero_index) % len(mixed_data)]
        + mixed_data[(2000 + zero_index) % len(mixed_data)]
        + mixed_data[(3000 + zero_index) % len(mixed_data)]
    )
