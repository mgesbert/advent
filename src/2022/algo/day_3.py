ITEM_TOKENS = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def part_1(input_data):
    return sum(
        ITEM_TOKENS.index(
            next(c for c in line[: len(line) // 2] if c in line[len(line) // 2 :])
        )
        for line in input_data
    )


def part_2(input_data):
    return sum(
        ITEM_TOKENS.index(next(c for c in l1 if c in l2 and c in l3))
        for [l1, l2, l3] in zip(input_data, input_data, input_data)
    )
