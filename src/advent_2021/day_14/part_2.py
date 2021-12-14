from collections import defaultdict
from functools import lru_cache

from advent_2021.helpers import get_input


def count_chars(polymer: str):
    return {c: polymer.count(c) for c in set(polymer)}


if __name__ == "__main__":
    input_getter = get_input()
    polymer = next(input_getter)
    next(input_getter)
    rules: dict[str, dict[str, str]] = defaultdict(lambda: dict())
    for line in input_getter:
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
    print(max(counts.values()) - min(counts.values()))
