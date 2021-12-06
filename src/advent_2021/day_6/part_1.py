from advent_2021.helpers import get_input


if __name__ == "__main__":
    fishes = list(map(int, next(get_input()).split(",")))
    for _ in range(80):
        fishes = [g for f in fishes for g in ([f - 1] if f > 0 else [6, 8])]
    print(len(fishes))
