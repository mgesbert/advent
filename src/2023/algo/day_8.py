import re
import itertools
import math


def part_1(input_data):
    instructions = next(input_data)
    next(input_data)
    map_ = {
        k: (next_l, next_r)
        for k, next_l, next_r in (
            re.sub("[=(),]", "", line).split() for line in input_data
        )
    }

    pos = "AAA"
    for i, direction in enumerate(itertools.cycle(instructions), start=1):
        pos = map_[pos][0 if direction == "L" else 1]
        if pos == "ZZZ":
            return i


def part_2(input_data):
    instructions = next(input_data)
    next(input_data)
    map_ = {
        k: (next_l, next_r)
        for k, next_l, next_r in (
            re.sub("[=(),]", "", line).split() for line in input_data
        )
    }

    positions = [x for x in map_ if x.endswith("A")]
    cycle_lengths = []
    for pos in positions:
        for i, direction in enumerate(itertools.cycle(instructions), start=1):
            pos = map_[pos][0 if direction == "L" else 1]
            if pos.endswith("Z"):
                cycle_lengths.append(i)
                break
    return math.lcm(*cycle_lengths)
