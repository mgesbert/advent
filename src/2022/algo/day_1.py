def part_1(input_data):
    return max(
        sum(int(calories) for calories in elve_carry.split("|"))
        for elve_carry in "|".join(input_data).split("||")
    )


def part_2(input_data):
    return sum(
        sorted(
            (
                sum(int(calories) for calories in elve_carry.split("|"))
                for elve_carry in "|".join(input_data).split("||")
            ),
            reverse=True,
        )[:3]
    )
