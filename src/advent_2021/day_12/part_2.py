from collections import defaultdict

from advent_2021.helpers import get_input


def dfs(
    caves: dict[str, list[str]],
    current: str,
    visited: set[str] | None = None,
    visited_twice: bool = False,
) -> int:
    nb_paths = 0
    if visited is None:
        visited = set()

    if current == "end":
        return 1
    if current == "start" and "start" in visited:
        return 0

    for cave in caves[current]:
        if cave in visited:
            if visited_twice:
                continue
        nb_paths += dfs(
            caves,
            cave,
            visited | {current} if current.islower() else visited,
            visited_twice or cave in visited,
        )

    return nb_paths


if __name__ == "__main__":
    caves: dict[str, list[str]] = defaultdict(list)
    for line in get_input():
        caves[line.split("-")[0]].append(line.split("-")[1])
        caves[line.split("-")[1]].append(line.split("-")[0])
    print(dfs(caves, "start"))
