from collections import defaultdict

from advent_2020.helpers import get_input


def parse_rule(rule: str):
    container, contained = (
        rule.replace(" bags", "")
        .replace(" bag", "")
        .replace(".", "")
        .split(" contain ")
    )
    contained_by: dict[str, list[str]] = {}
    for content in contained.split(", "):
        if content.startswith("no "):
            continue
        _, *tail = content.split(" ")
        contained_by[" ".join(tail)] = [container]
    return contained_by


def dfs(tree: dict[str, list[str]], root: str):
    result = set(tree[root])
    for b in tree[root]:
        result |= dfs(tree, b)
    return result


if __name__ == "__main__":
    contained_by: dict[str, list[str]] = defaultdict(list)
    for rule in get_input():
        for k, v in parse_rule(rule).items():
            contained_by[k] += v

    print(len(dfs(contained_by, "shiny gold")))
