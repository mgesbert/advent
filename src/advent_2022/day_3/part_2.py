from advent_2022.helpers import get_input


if __name__ == "__main__":
    print(
        sum(
            " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".index(
                next(c for c in l1 if c in l2 and c in l3)
            )
            for [l1, l2, l3] in zip(*[get_input()] * 3)
        )
    )
