OFFSETS = {
    "<": (-1, 0),
    ">": (1, 0),
    "v": (0, 1),
    "^": (0, -1),
}


def debug(blizzards, w, h):
    for y in range(h):
        if y == 0:
            print("# " + "#" * (w - 2))
            continue
        if y == h - 1:
            print("#" * (w - 2) + " #")
            continue
        for x in range(w):
            if x in [0, w - 1]:
                print("#", end="")
                continue
            b = [k for k, v in blizzards.items() if (x, y) in v]
            print("." if len(b) == 0 else b[0] if len(b) == 1 else len(b), end="")
        print()


def parse(input_data):
    blizzards = {
        "<": set(),
        ">": set(),
        "v": set(),
        "^": set(),
    }
    i = j = -1
    for j, row in enumerate(input_data):
        for i, x in enumerate(row):
            if x in ".#":
                continue
            blizzards[x].add((i, j))
    return i + 1, j + 1, blizzards


def move(blizzards, w, h):
    return {
        k: {
            (
                (x + OFFSETS[k][0] - 1) % (w - 2) + 1,
                (y + OFFSETS[k][1] - 1) % (h - 2) + 1,
            )
            for x, y in v
        }
        for k, v in blizzards.items()
    }


def solve(w, h, blizzards, objectives):
    turn = 0
    start = (1, 0)
    target = (w - 2, h - 1)
    positions = {start}
    objective, *objectives = objectives
    while True:
        turn += 1
        blizzards = move(blizzards, w, h)
        all_blizzards = {b for l in blizzards.values() for b in l}
        positions = {
            (x + offset[0], y + offset[1])
            for x, y in positions
            for offset in list(OFFSETS.values()) + [(0, 0)]
            if 0 < x + offset[0] < w - 1
            and 0 < y + offset[1] < h - 1
            and (x + offset[0], y + offset[1]) not in all_blizzards
            or (x + offset[0], y + offset[1]) in [start, target]
        }
        if objective in positions:
            if len(objectives) == 0:
                return turn
            positions = {objective}
            objective, *objectives = objectives


def part_1(input_data):
    w, h, blizzards = parse(input_data)
    target = (w - 2, h - 1)
    return solve(w, h, blizzards, [target])


def part_2(input_data):
    w, h, blizzards = parse(input_data)
    start = (1, 0)
    target = (w - 2, h - 1)
    return solve(w, h, blizzards, [target, start, target])
