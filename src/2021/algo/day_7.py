def part_1(input_data):
    positions = list(map(int, next(input_data).split(",")))
    return min(
        sum(abs(position - target) for position in positions)
        for target in range(min(positions), max(positions))
    )


def part_2(input_data):
    positions = list(map(int, next(input_data).split(",")))
    return min(
        sum(
            abs(position - target) * (abs(position - target) + 1) // 2
            for position in positions
        )
        for target in range(min(positions), max(positions))
    )
