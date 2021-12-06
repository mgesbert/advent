from advent_2020.helpers import get_input


if __name__ == "__main__":
    state: dict[int, dict[int, dict[int, dict[int, str]]]] = {0: {0: {}}}

    for x, line in enumerate(get_input()):
        state[0][0][x] = {w: c for w, c in enumerate(line)}

    for _ in range(6):
        new_state: dict[int, dict[int, dict[int, dict[int, str]]]] = {}
        for z in range(min(state.keys()) - 1, max(state.keys()) + 2):
            cube = state.get(z, {})
            for y in range(min(state[0].keys()) - 1, max(state[0].keys()) + 2):
                level = cube.get(y, {})
                for x in range(
                    min(state[0][0].keys()) - 1, max(state[0][0].keys()) + 2
                ):
                    row = level.get(x, {})
                    for w in range(
                        min(state[0][0][0].keys()) - 1, max(state[0][0][0].keys()) + 2
                    ):
                        value = row.get(w, ".")
                        nb_active_neighbors = sum(
                            state.get(zz, {}).get(yy, {}).get(xx, {}).get(ww, ".")
                            == "#"
                            for zz in range(z - 1, z + 2)
                            for yy in range(y - 1, y + 2)
                            for xx in range(x - 1, x + 2)
                            for ww in range(w - 1, w + 2)
                            if zz != z or yy != y or xx != x or ww != w
                        )
                        if z not in new_state:
                            new_state[z] = {}
                        if y not in new_state[z]:
                            new_state[z][y] = {}
                        if x not in new_state[z][y]:
                            new_state[z][y][x] = {}
                        new_state[z][y][x][w] = (
                            "#"
                            if value == "#"
                            and 2 <= nb_active_neighbors <= 3
                            or value == "."
                            and nb_active_neighbors == 3
                            else "."
                        )
        state = new_state

    print(
        sum(
            value == "#"
            for cube in state.values()
            for level in cube.values()
            for row in level.values()
            for value in row.values()
        )
    )

    # for z, cube in sorted(state.items(), key=lambda c: c[0]):
    #     for y, level in sorted(cube.items(), key=lambda c: c[0]):
    #         print(f"z={z} y={y}")
    #         for x, row in sorted(level.items(), key=lambda c: c[0]):
    #             print("".join([c for _, c in sorted(row.items(), key=lambda c: c[0])]))
