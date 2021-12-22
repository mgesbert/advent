from advent_2021.helpers import get_input


Cube = tuple[int, int, int, int, int, int]


def remove_intersection(c1: Cube, c2: Cube) -> list[Cube]:
    x0, x1, y0, y1, z0, z1 = c1
    i0, i1, j0, j1, k0, k1 = c2

    if x0 > i1 or x1 < i0 or y0 > j1 or y1 < j0 or z0 > k1 or z1 < k0:
        return [c1]

    result: list[Cube] = []
    if x0 < i0 <= x1:
        result.append((x0, i0 - 1, y0, y1, z0, z1))
    if x0 <= i1 < x1:
        result.append((i1 + 1, x1, y0, y1, z0, z1))

    if y0 < j0 <= y1:
        result.append((max(x0, i0), min(x1, i1), y0, j0 - 1, z0, z1))
    if y0 <= j1 < y1:
        result.append((max(x0, i0), min(x1, i1), j1 + 1, y1, z0, z1))

    if z0 < k0 <= z1:
        result.append((max(x0, i0), min(x1, i1), max(y0, j0), min(y1, j1), z0, k0 - 1))
    if z0 <= k1 < z1:
        result.append((max(x0, i0), min(x1, i1), max(y0, j0), min(y1, j1), k1 + 1, z1))

    return result


def volume(cube: Cube):
    x0, x1, y0, y1, z0, z1 = cube
    return (x1 - x0 + 1) * (y1 - y0 + 1) * (z1 - z0 + 1)


if __name__ == "__main__":
    cubes: list[tuple[str, Cube]] = []
    for line in get_input():
        command = line.split(" ")[0]
        boundaries = tuple(
            [
                int(s)
                for range_ in line.split(" ")[1].split(",")
                for s in range_[2:].split("..")
            ]
        )
        if boundaries[0] < -50 or boundaries[0] > 50:
            continue
        cubes.append((command, boundaries))  # type: ignore

    inactive_cubes: list[Cube] = []

    nb_cubes_on = 0
    for command, cube in cubes[::-1]:
        x0, x1, y0, y1, z0, z1 = cube
        active_cubes = [cube]
        for inactive_cube in inactive_cubes:
            active_cubes = [
                c
                for active_cube in active_cubes
                for c in remove_intersection(active_cube, inactive_cube)
            ]

        if command == "on":
            nb_cubes_on += sum(volume(c) for c in active_cubes)
        inactive_cubes += active_cubes
    print(nb_cubes_on)
