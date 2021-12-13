from advent_2021.helpers import get_input


def get_next_flash(octopuses: list[list[int]]):
    return next(
        (
            (i, j)
            for j, line in enumerate(octopuses)
            for i, o in enumerate(line)
            if o > 9
        ),
        (None, None),
    )


if __name__ == "__main__":
    octopuses = [[int(o) for o in line] for line in get_input()]
    n = 0
    while True:
        n += 1
        nb_flashes = 0
        for line in octopuses:
            for i in range(len(octopuses)):
                line[i] += 1

        flash_x, flash_y = get_next_flash(octopuses)
        while flash_x is not None and flash_y is not None:
            nb_flashes += 1
            octopuses[flash_y][flash_x] = -100000000
            for x in [flash_x - 1, flash_x, flash_x + 1]:
                for y in [flash_y - 1, flash_y, flash_y + 1]:
                    if flash_x == x and flash_y == y:
                        continue
                    if x < 0 or x >= len(octopuses[0]) or y < 0 or y >= len(octopuses):
                        continue
                    octopuses[y][x] += 1
            flash_x, flash_y = get_next_flash(octopuses)

        for j, line in enumerate(octopuses):
            for i, o in enumerate(line):
                line[i] = max(line[i], 0)

        if nb_flashes == len(octopuses) * len(octopuses[0]):
            print(n)
            break
