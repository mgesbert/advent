from advent_2020.helpers import get_input


if __name__ == "__main__":
    state: dict[int, dict[int, dict[int, str]]] = {0: {}}

    for y, line in enumerate(get_input()):
        state[0][y] = {}
        for x, c in enumerate(line):
            state[0][y][x] = c

    for _ in range(6):
        new_state: dict[int, dict[int, dict[int, str]]] = {}
        for z in range(min(state.keys()) - 1, max(state.keys()) + 2):
            level = state.get(z) or {}
            for y in range(min(state[0].keys()) - 1, max(state[0].keys()) + 2):
                row = level.get(y) or {}
                for x in range(
                    min(state[0][0].keys()) - 1, max(state[0][0].keys()) + 2
                ):
                    value = row.get(x, ".")
                    nb_active_neighbors = sum(
                        state.get(zz, {}).get(yy, {}).get(xx, ".") == "#"
                        for zz in range(z - 1, z + 2)
                        for yy in range(y - 1, y + 2)
                        for xx in range(x - 1, x + 2)
                        if zz != z or yy != y or xx != x
                    )
                    if z not in new_state:
                        new_state[z] = {}
                    if y not in new_state[z]:
                        new_state[z][y] = {}
                    new_state[z][y][x] = (
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
            for level in state.values()
            for row in level.values()
            for value in row.values()
        )
    )
