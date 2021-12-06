from advent_2021.helpers import get_input


if __name__ == "__main__":
    positions = list(map(int, next(get_input()).split(",")))
    print(
        min(
            sum(abs(position - target) for position in positions)
            for target in range(min(positions), max(positions))
        )
    )
