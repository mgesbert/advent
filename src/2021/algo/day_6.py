from collections import defaultdict


def part_1(input_data):
    fishes = list(map(int, next(input_data).split(",")))
    for _ in range(80):
        fishes = [g for f in fishes for g in ([f - 1] if f > 0 else [6, 8])]
    return len(fishes)


def part_2(input_data):
    fishes = list(map(int, next(input_data).split(",")))
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
    return sum(fishes_by_size.values())
