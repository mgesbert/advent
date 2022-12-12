def dijkstra(map_, start_nodes):
    end = next(
        i + 1j * j
        for j, row in enumerate(map_)
        for i, value in enumerate(row)
        if value == "E"
    )
    visited = {end}
    queue: list[tuple[complex, int]] = [(end, 0)]
    while queue:
        (current, path_len), *queue = queue
        x, y = int(round(current.real)), int(round(current.imag))
        if map_[y][x] in start_nodes:
            return path_len
        for offset in [1, -1, 1j, -1j]:
            pos = current + offset
            next_x, next_y = int(round(pos.real)), int(round(pos.imag))
            if not (0 <= next_x < len(map_[0]) and 0 <= next_y < len(map_)):
                continue
            if pos in visited:
                continue
            elevation = ord("z" if map_[y][x] == "E" else map_[y][x])
            next_elevation = ord(
                "a" if map_[next_y][next_x] == "S" else map_[next_y][next_x]
            )
            if elevation - next_elevation > 1:
                continue
            visited |= {pos}
            queue.append((pos, path_len + 1))


def part_1(input_data):
    map_ = list(input_data)
    return dijkstra(map_, "S")


def part_2(input_data):
    map_ = list(input_data)
    return dijkstra(map_, "a")
