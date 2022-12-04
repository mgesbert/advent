from collections import defaultdict
from functools import lru_cache


def part_1(input_data):
    polymer = next(input_data)
    next(input_data)
    rules: dict[str, dict[str, str]] = defaultdict(dict)
    for line in input_data:
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
    return max(polymer.count(c) for c in characters) - min(
        polymer.count(c) for c in characters
    )


def part_2(input_data):
    def count_chars(polymer: str):
        return {c: polymer.count(c) for c in set(polymer)}

    polymer = next(input_data)
    next(input_data)
    rules: dict[str, dict[str, str]] = defaultdict(lambda: dict())
    for line in input_data:
        left = line[0]
        right = line[1]
        insert = line[6]
        rules[left][right] = insert

    rules = dict(rules)

    @lru_cache(maxsize=1000)
    def dfs(polymer: str, step: int):
        if step == 40:
            return count_chars(polymer)
        counts: dict[str, int] = defaultdict(int)
        for left, right in zip(polymer[:-1], polymer[1:]):
            sub_counts = dfs(left + rules[left][right] + right, step + 1)
            for k, v in sub_counts.items():
                counts[k] += v
            counts[right] -= 1
        counts[polymer[-1]] += 1
        return counts

    counts = dfs(polymer, 0)
    return max(counts.values()) - min(counts.values())
