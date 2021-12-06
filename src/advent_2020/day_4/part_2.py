import functools
import re
from collections.abc import Callable

from advent_2020.helpers import get_input


def reducer(acc: list[str], l: str):
    if l == "":
        return acc + [l]
    if acc[-1] == "":
        return acc[:-1] + [l]
    return acc[:-1] + [acc[-1] + " " + l]


def build_validator(
    regex: str, predicate: Callable[[tuple[str, ...]], bool]
) -> Callable[[str], bool]:
    def validator(s: str):
        match = re.search(regex, s)
        return match is not None and predicate(match.groups())

    return validator


if __name__ == "__main__":
    data = functools.reduce(reducer, list(get_input()), [""])
    print(
        sum(
            all(
                validator(passport)
                for validator in [
                    build_validator(
                        r"byr:(\d{4})(\D|$)",
                        lambda g: g[0].isdigit() and 1920 <= int(g[0]) <= 2002,
                    ),
                    build_validator(
                        r"iyr:(\d{4})(\D|$)",
                        lambda g: g[0].isdigit() and 2010 <= int(g[0]) <= 2020,
                    ),
                    build_validator(
                        r"eyr:(\d{4})(\D|$)",
                        lambda g: g[0].isdigit() and 2020 <= int(g[0]) <= 2030,
                    ),
                    build_validator(
                        r"hgt:(\d+)(cm|in)( |$)",
                        lambda g: g[0].isdigit() and (150 <= int(g[0]) <= 193)
                        if g[1] == "cm"
                        else (59 <= int(g[0]) <= 76),
                    ),
                    build_validator(r"hcl:#([0-9a-f]{6})( |$)", lambda _: True),
                    build_validator(
                        r"ecl:(amb|blu|brn|gry|grn|hzl|oth)( |$)", lambda _: True
                    ),
                    build_validator(r"pid:(\d{9})( |$)", lambda g: g[0].isdigit()),
                ]
            )
            for passport in data
        )
    )
