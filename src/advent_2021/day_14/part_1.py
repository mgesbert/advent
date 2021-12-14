from collections import defaultdict

from advent_2021.helpers import get_input


if __name__ == "__main__":
    input_getter = get_input()
    polymer = next(input_getter)
    next(input_getter)
    rules: dict[str, dict[str, str]] = defaultdict(dict)
    for line in input_getter:
        left = line[0]
        right = line[1]
        insert = line[6]
        rules[left][right] = insert

    rules = dict(rules)

    for _ in range(10):
        polymer = (
            "".join(
                left + rules[left][right]
                for left, right in zip(polymer[:-1], polymer[1:])
            )
            + polymer[-1]
        )

    characters = set(polymer)
    print(
        max(polymer.count(c) for c in characters)
        - min(polymer.count(c) for c in characters)
    )
