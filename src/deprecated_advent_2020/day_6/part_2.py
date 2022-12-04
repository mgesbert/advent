import itertools

from advent_2020.helpers import get_input


if __name__ == "__main__":
    result = 0
    group: list[str] = []
    for l in itertools.chain(get_input(), iter([""])):
        if l != "":
            group.append(l)
            continue
        questions = {c for c in group[0]}
        for w in group:
            questions &= {c for c in w}
        result += len(questions)
        group = []
    print(result)
