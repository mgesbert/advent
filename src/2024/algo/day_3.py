import re


def part_1(input_data):
    return sum(
        int(a) * int(b)
        for a, b in re.findall(r"mul\((\d+),(\d+)\)", "".join(input_data))
    )


def part_2(input_data):
    data = "".join(input_data)
    activate_indices = [x.start() for x in re.finditer(r"do\(\)", data)]
    deactivate_indices = [x.start() for x in re.finditer(r"don't\(\)", data)]
    matches = [
        m.groups()
        for m in re.finditer(r"mul\((\d+),(\d+)\)", data)
        if max((s for s in activate_indices if s < m.start()), default=0)
        > max((s for s in deactivate_indices if s < m.start()), default=-1)
    ]
    return sum(int(a) * int(b) for a, b in matches)
