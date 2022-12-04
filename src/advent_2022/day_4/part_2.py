from advent_2022.helpers import get_input


if __name__ == "__main__":
    print(
        sum(
            x1 <= y2 and y1 <= x2
            for x1, x2, y1, y2 in (
                map(int, line.replace(",", "-").split("-")) for line in get_input()
            )
        )
    )
