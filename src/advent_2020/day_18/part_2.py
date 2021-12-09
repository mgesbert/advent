import re

from advent_2020.helpers import get_input


class CustomInt(int):
    def __init__(self, n: int):
        self.n = n

    def __add__(self, other):
        if not isinstance(other, CustomInt):
            raise TypeError()
        return CustomInt(self.n * other.n)

    def __mul__(self, other):
        if not isinstance(other, CustomInt):
            raise TypeError()
        return CustomInt(self.n + other.n)


if __name__ == "__main__":
    print(
        sum(
            eval(
                re.sub(r"(\d+)", r"CustomInt(\1)", line)
                .replace("*", "-")
                .replace("+", "*")
                .replace("-", "+")
            )
            for line in get_input()
        )
    )
