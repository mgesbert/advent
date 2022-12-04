from collections import defaultdict

from advent_2020.helpers import get_input


if __name__ == "__main__":
    init = [int(x) for x in next(get_input()).split(",")]
    state: dict[int, list[int]] = defaultdict(lambda: [])
    last: int = 0

    for i, n in enumerate(init):
        state[n] = [i]
        last = n

    for turn in range(len(init), 2020):
        hist = state[last]
        last = 0 if len(hist) == 1 else hist[-1] - hist[-2]
        state[last] += [turn]

    print(last)
