import math


def margin(time, distance):
    # t² - time*t + distance > 0
    # ∆ = time² - 4*distance
    delta = time**2 - 4 * distance
    x1 = (time - math.sqrt(delta)) / 2
    x2 = (time + math.sqrt(delta)) / 2
    max_hold_time = math.floor(x2) - (
        math.floor(x2) == x2
    )  # the second term is for the strict inequality
    min_hold_time = math.ceil(x1) + (
        math.ceil(x1) == x1
    )  # the second term is for the strict inequality
    return max_hold_time - min_hold_time + 1


def part_1(input_data):
    times = [int(x) for x in next(input_data).split()[1:]]
    distances = [int(x) for x in next(input_data).split()[1:]]
    return math.prod(margin(time, distance) for time, distance in zip(times, distances))


def part_2(input_data):
    time = int("".join(next(input_data).split()[1:]))
    distance = int("".join(next(input_data).split()[1:]))
    return margin(time, distance)
