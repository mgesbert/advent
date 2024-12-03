def is_safe(levels):
    return all(1 <= b - a <= 3 for a, b in zip(levels[:-1], levels[1:])) or all(
        -3 <= b - a <= 1 for a, b in zip(levels[:-1], levels[1:])
    )


def part_1(input_data):
    return sum(is_safe(list(map(int, row.split()))) for row in input_data)


def part_2(input_data):
    count = 0
    for row in input_data:
        levels = list(map(int, row.split()))
        count += is_safe(levels) or any(
            is_safe(levels[:i] + levels[i + 1 :]) for i in range(len(levels))
        )
    return count
