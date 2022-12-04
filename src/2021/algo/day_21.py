from functools import lru_cache


def part_1(input_data):
    def get_die():
        n = 0
        while True:
            yield n % 100 + 1
            n += 1

    players = [
        int(next(input_data).split(": ")[1]),
        int(next(input_data).split(": ")[1]),
    ]
    scores = [0, 0]
    die = get_die()
    nb_rolls = 0

    while True:
        for i in range(2):
            players[i] = (players[i] + next(die) + next(die) + next(die) - 1) % 10 + 1
            scores[i] += players[i]
            nb_rolls += 3
            if scores[i] > 999:
                return scores[1 - i] * nb_rolls


def part_2(input_data):
    @lru_cache(maxsize=None)
    def nb_wins(
        p1: int, p2: int, s1: int, s2: int, is_p1: bool = False
    ) -> tuple[int, int]:
        if s1 > 20:
            return 1, 0
        if s2 > 20:
            return 0, 1
        total_1 = total_2 = 0
        if is_p1:
            for i in range(1, 4):
                for j in range(1, 4):
                    for k in range(1, 4):
                        p2_next = (p2 + i + j + k - 1) % 10 + 1
                        w1, w2 = nb_wins(p1, p2_next, s1, s2 + p2_next, False)
                        total_1 += w1
                        total_2 += w2
        else:
            for i in range(1, 4):
                for j in range(1, 4):
                    for k in range(1, 4):
                        p1_next = (p1 + i + j + k - 1) % 10 + 1
                        w1, w2 = nb_wins(p1_next, p2, s1 + p1_next, s2, True)
                        total_1 += w1
                        total_2 += w2

        return total_1, total_2

    players = [
        int(next(input_data).split(": ")[1]),
        int(next(input_data).split(": ")[1]),
    ]
    return max(nb_wins(*players, 0, 0))
