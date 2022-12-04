from collections import defaultdict

from advent_2020.helpers import get_input


def parse_rule(rule: str):
    container, contained = (
        rule.replace(" bags", "")
        .replace(" bag", "")
        .replace(".", "")
        .split(" contain ")
    )
    contains: dict[str, list[tuple[int, str]]] = {container: []}
    for content in contained.split(", "):
        if content.startswith("no "):
            continue
        n, *tail = content.split(" ")
        contains[container].append((int(n), " ".join(tail)))
    return contains


def dfs(tree: dict[str, list[tuple[int, str]]], root: str):
    result = 0
    for n, bag in tree[root]:
        result += n * (dfs(tree, bag) + 1)
    return result


if __name__ == "__main__":
    contains: dict[str, list[tuple[int, str]]] = defaultdict(list)
    for rule in get_input():
        contains = dict(**contains, **parse_rule(rule))

    print(dfs(contains, "shiny gold"))
