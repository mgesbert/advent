from advent_2020.helpers import get_input


nb_ar_cache: dict[tuple[int, int], int] = {}


def nb_ar(adapters: list[int], current: int) -> int:
    if (current, len(adapters)) in nb_ar_cache:
        return nb_ar_cache[(current, len(adapters))]

    if len(adapters) <= 1:
        nb_ar_cache[(current, 1)] = 1
        return 1

    result = nb_ar(adapters[1:], adapters[0])
    if len(adapters) > 1 and adapters[1] - current < 4:
        result += nb_ar(adapters[2:], adapters[0])
    if len(adapters) > 2 and adapters[2] - current < 4:
        result += nb_ar(adapters[3:], adapters[0])
    if len(adapters) > 3 and adapters[3] - current < 4:
        result += nb_ar(adapters[4:], adapters[0])
    nb_ar_cache[(current, len(adapters))] = result
    return result


if __name__ == "__main__":
    adapters = sorted(map(int, get_input()))
    print(nb_ar(adapters, 0))
