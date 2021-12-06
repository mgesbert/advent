from advent_2021.helpers import get_input


if __name__ == "__main__":
    positions = list(map(int, next(get_input()).split(",")))
    print(
        min(
            sum(
                abs(position - target) * (abs(position - target) + 1) // 2
                for position in positions
            )
            for target in range(min(positions), max(positions))
        )
    )
