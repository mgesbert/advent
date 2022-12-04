import re
import sys
from collections.abc import Callable

from advent_2020.helpers import get_input


def get_rule(a: int, b: int, c: int, d: int):
    def rule(x: int):
        return a <= x <= b or c <= x <= d

    return rule


if __name__ == "__main__":
    input_getter = get_input()
    rules: list[Callable[[int], bool]] = []

    while (line := next(input_getter)) != "":
        search_result = re.search(r".*: (\d+)-(\d+) or (\d+)-(\d+)", line)
        if search_result is None:
            sys.exit(1)
        a, b, c, d = (int(x) for x in search_result.groups())

        rules.append(get_rule(a, b, c, d))

    next(input_getter)
    my_ticket = [int(x) for x in next(input_getter).split(",")]
    next(input_getter)
    next(input_getter)

    other_tickets: list[list[int]] = []
    for line in input_getter:
        other_tickets.append([int(x) for x in line.split(",")])

    print(
        sum(
            value
            for ticket in other_tickets
            for value in ticket
            if not any(rule(value) for rule in rules)
        )
    )
