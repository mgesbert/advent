def parse_line(line):
    for handful in line.split(": ")[1].split("; "):
        for data in handful.split(", "):
            count_str, color = data.split(" ")
            count = int(count_str)
            yield count, color


def part_1(input_data):
    return sum(
        int(line.split(":")[0].split(" ")[1])
        for line in input_data
        if all(
            {"red": 12, "green": 13, "blue": 14}[color] >= count
            for count, color in parse_line(line)
        )
    )


def set_power(line):
    counts = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    for count, color in parse_line(line):
        counts[color] = max(counts[color], count)
    return counts["red"] * counts["green"] * counts["blue"]


def part_2(input_data):
    return sum(set_power(line) for line in input_data)
