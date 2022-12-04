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
    rules: dict[str, Callable[[int], bool]] = {}

    while (line := next(input_getter)) != "":
        search_result = re.search(r"(.*): (\d+)-(\d+) or (\d+)-(\d+)", line)
        if search_result is None:
            sys.exit(1)
        groups = search_result.groups()
        a, b, c, d = (int(x) for x in groups[1:])

        rules[groups[0]] = get_rule(a, b, c, d)

    next(input_getter)
    my_ticket = [int(x) for x in next(input_getter).split(",")]
    next(input_getter)
    next(input_getter)

    other_tickets: list[list[int]] = []
    for line in input_getter:
        other_tickets.append([int(x) for x in line.split(",")])

    fields = [list(rules.keys()) for _ in range(len(my_ticket))]

    for ticket in [my_ticket] + other_tickets:
        for i, value in enumerate(ticket):
            if not any(rule(value) for rule in rules.values()):
                break
        else:
            for i, value in enumerate(ticket):
                for field in [*fields[i]]:
                    if not rules[field](value):
                        fields[i].remove(field)

    while any(len(group) > 1 for group in fields):
        attributed_fields = {group[0] for group in fields if len(group) == 1}
        for group in fields:
            if len(group) == 1:
                continue
            for field in attributed_fields:
                if field in group:
                    group.remove(field)

    fields = [group[0] for group in fields]

    result = 1

    for value, field in zip(my_ticket, fields):
        if field.startswith("departure"):
            result *= value

    print(result)
