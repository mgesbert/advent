def part_1(input_data):
    return sum(
        y1 <= x1 <= x2 <= y2 or x1 <= y1 <= y2 <= x2
        for x1, x2, y1, y2 in (
            map(int, line.replace(",", "-").split("-")) for line in input_data
        )
    )


def part_2(input_data):
    return sum(
        x1 <= y2 and y1 <= x2
        for x1, x2, y1, y2 in (
            map(int, line.replace(",", "-").split("-")) for line in input_data
        )
    )
