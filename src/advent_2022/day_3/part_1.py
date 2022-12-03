from advent_2022.helpers import get_input


if __name__ == "__main__":
    print(
        sum(
            " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".index(
                next(c for c in line[: len(line) // 2] if c in line[len(line) // 2 :])
            )
            for line in get_input()
        )
    )
