from advent_2022.helpers import get_input


if __name__ == "__main__":
    print(
        sum(
            (ord(opp) + ord(me) - 1) % 3 + 1 + (ord(me) - ord("X")) * 3
            for [opp, me] in [line.split() for line in get_input()]
        )
    )
