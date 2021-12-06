from collections import defaultdict

from advent_2021.helpers import get_input


if __name__ == "__main__":
    fishes = list(map(int, next(get_input()).split(",")))
    fishes_by_size: dict[int, int] = defaultdict(int)
    for fish in fishes:
        fishes_by_size[fish] += 1
    for i in range(256):
        next_fishes_by_size: dict[int, int] = defaultdict(int)
        for size, count in fishes_by_size.items():
            if size == 0:
                next_fishes_by_size[6] += count
                next_fishes_by_size[8] += count
            else:
                next_fishes_by_size[size - 1] += count
        fishes_by_size = next_fishes_by_size
    print(sum(fishes_by_size.values()))
