def bfs(area, start):
    plant = area[start]
    queue = [start]
    visited = set()
    while queue:
        z = queue.pop(0)
        if z in visited:
            continue
        visited.add(z)
        for dz in [1, -1, 1j, -1j]:
            nz = z + dz
            if nz not in visited and area.get(nz) == plant:
                queue.append(nz)
    return visited


def part_1(input_data):
    area = {
        x + y * 1j: c for y, line in enumerate(input_data) for x, c in enumerate(line)
    }
    visited = set()
    total_price = 0
    for z in area:
        if z in visited:
            continue
        field = bfs(area, z)
        visited.update(field)
        total_price += len(field) * (
            sum(z + dz not in field for z in field for dz in [1, -1, 1j, -1j])
        )

    return total_price


def compute_price(field):
    def is_left_border(z):
        return z - 1 not in field and z in field

    def is_right_border(z):
        return z + 1 not in field and z in field

    def is_top_border(z):
        return z - 1j not in field and z in field

    def is_bottom_border(z):
        return z + 1j not in field and z in field

    min_x, max_x = int(min(z.real for z in field)), int(max(z.real for z in field))
    min_y, max_y = int(min(z.imag for z in field)), int(max(z.imag for z in field))
    nb_sides = 0
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            z = x + y * 1j
            if z not in field:
                continue
            nb_sides += is_right_border(z) and not is_right_border(z - 1j)
            nb_sides += is_left_border(z) and not is_left_border(z - 1j)
            nb_sides += is_top_border(z) and not is_top_border(z - 1)
            nb_sides += is_bottom_border(z) and not is_bottom_border(z - 1)
    return nb_sides * len(field)


def part_2(input_data):
    area = {
        x + y * 1j: c for y, line in enumerate(input_data) for x, c in enumerate(line)
    }
    visited = set()
    total_price = 0
    for z in area:
        if z in visited:
            continue
        field = bfs(area, z)
        visited.update(field)
        total_price += compute_price(field)

    return total_price
