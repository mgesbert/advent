from advent_2022.helpers import get_input


if __name__ == "__main__":
    print(
        sum(
            ord(me) - ord("W") + ((ord(me) - ord(opp) - 1) % 3) * 3
            for [opp, me] in [line.split() for line in get_input()]
        )
    )
