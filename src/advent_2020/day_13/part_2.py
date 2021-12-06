import math

from advent_2020.helpers import get_input


def ppcm(a: int, b: int):
    return a * b // math.gcd(a, b)


if __name__ == "__main__":
    input_getter = get_input()
    ts = int(next(input_getter))
    equations = [
        (int(x), i) for i, x in enumerate(next(input_getter).split(",")) if x.isdigit()
    ]
    step = equations[0][0]
    result = ts
    while result % step != 0:
        result += 1
    for bus, minute in equations[1:]:
        while result % bus != bus - minute % bus:
            result += step
        step = ppcm(step, bus)
    print(result)
