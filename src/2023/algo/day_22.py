from collections import defaultdict


def parse_input(input_data):
    bricks = list()
    for row in input_data:
        (x1, y1, z1), (x2, y2, z2) = [
            tuple(map(int, x.split(","))) for x in row.split("~")
        ]
        bricks.append(
            tuple(
                (x, y, z)
                for x in range(x1, x2 + 1)
                for y in range(y1, y2 + 1)
                for z in range(z1, z2 + 1)
            )
        )
    return bricks


def fall(bricks):
    result = set()
    for brick in bricks:
        if not any(
            z < 2 or (x, y, z - 1) in b
            for b in bricks
            for (x, y, z) in brick
            if (b != brick)
        ):
            result.add(tuple((x, y, z - 1) for (x, y, z) in brick))
        else:
            result.add(brick)
    return result


def part_1(input_data):
    bricks = parse_input(input_data)
    while bricks != (bricks := fall(bricks)):
        pass

    supported_by = defaultdict(set)

    for i, brick in enumerate(bricks):
        print(f"{i}/{len(bricks)}")
        for j, b in enumerate(bricks):
            if i == j:
                continue
            for x, y, z in brick:
                if (x, y, z + 1) in b:
                    supported_by[j].add(i)

    return sum(
        all(len(supports) > 1 for supports in supported_by.values() if i in supports)
        for i in range(len(bricks))
    )


def nb_falls(supported_by, supports, brick_i):
    desintegrated = {brick_i}
    while True:
        next_desintegrated = desintegrated | {
            j
            for i in desintegrated
            for j in supports[i]
            if all(x in desintegrated for x in supported_by[j])
        }
        if next_desintegrated == desintegrated:
            break
        desintegrated = next_desintegrated
    return len(desintegrated) - 1


def part_2(input_data):
    bricks = parse_input(input_data)
    while bricks != (bricks := fall(bricks)):
        pass

    supported_by = defaultdict(set)
    supports = defaultdict(set)

    for i, brick in enumerate(bricks):
        for j, b in enumerate(bricks):
            if i == j:
                continue
            for x, y, z in brick:
                if (x, y, z + 1) in b:
                    supported_by[j].add(i)
                    supports[i].add(j)

    return sum(
        nb_falls(supported_by, supports, brick_i) for brick_i in range(len(bricks))
    )
