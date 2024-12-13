import math
from functools import cache


@cache
def compute_next_stones(stone):
    if stone == 0:
        return [1]
    nb_digits = int(math.log10(stone)) + 1
    if nb_digits % 2 == 0:
        return [stone // 10 ** (nb_digits // 2), stone % 10 ** (nb_digits // 2)]
    return [stone * 2024]


@cache
def iter_stone(stone, n):
    if n == 0:
        return 1

    next_stones = compute_next_stones(stone)
    return sum(iter_stone(s, n - 1) for s in next_stones)


def part_1(input_data):
    stones = [int(stone) for stone in next(input_data).split()]
    for _ in range(25):
        stones = [s for stone in stones for s in compute_next_stones(stone)]
    return len(stones)


def part_2(input_data):
    stones = [int(stone) for stone in next(input_data).split()]
    return sum(iter_stone(stone, 75) for stone in stones)
