import re

from advent_2020.helpers import get_input


if __name__ == "__main__":
    print(
        sum(
            len(set(g))
            for g in re.sub(r"([^\n])\n", r"\g<1>", "\n".join(get_input())).split()
        )
    )
