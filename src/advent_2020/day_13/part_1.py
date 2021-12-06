import math

from advent_2020.helpers import get_input


if __name__ == "__main__":
    input_getter = get_input()
    ts = int(next(input_getter))
    buses = [int(x) for x in next(input_getter).split(",") if x.isdigit()]
    bus = min(buses, key=lambda bus: bus - ts % bus)
    print(bus * (int(math.ceil(ts / bus)) * bus - ts))
