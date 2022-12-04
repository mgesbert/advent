def part_1(input_data):
    return sum(
        ord(me) - ord("W") + ((ord(me) - ord(opp) - 1) % 3) * 3
        for [opp, me] in [line.split() for line in input_data]
    )


def part_2(input_data):
    return sum(
        (ord(opp) + ord(me) - 1) % 3 + 1 + (ord(me) - ord("X")) * 3
        for [opp, me] in [line.split() for line in input_data]
    )
