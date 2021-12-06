import functools

from advent_2020.helpers import get_input


def reducer(acc: list[str], l: str):
    if l == "":
        return acc + [l]
    if acc[-1] == "":
        return acc[:-1] + [l]
    return acc[:-1] + [acc[-1] + " " + l]


if __name__ == "__main__":
    data = functools.reduce(reducer, list(get_input()), [""])
    print(
        sum(
            all(
                w in passport
                for w in [
                    "byr:",
                    "iyr:",
                    "eyr:",
                    "hgt:",
                    "hcl:",
                    "ecl:",
                    "pid:",
                ]
            )
            for passport in data
        )
    )
