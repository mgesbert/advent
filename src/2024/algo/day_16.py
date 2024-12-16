from collections import defaultdict


def parse_input(input_data):
    return {
        i + 1j * j: c for j, line in enumerate(input_data) for i, c in enumerate(line)
    }


def get_valid_moves(maze, pos):
    return [dzz for dzz in [1j, -1j, 1, -1] if maze.get(pos + dzz) != "#"]


def djikstra(maze):
    start = next(k for k, v in maze.items() if v == "S")
    end = next(k for k, v in maze.items() if v == "E")
    distances = defaultdict(lambda: float("inf"))
    distances[start] = 0
    queue = [(0, start, 1, [])]
    shortest_paths = []
    shortest_path_score = float("inf")

    while queue:
        (dist, pos, direction, path), *queue = queue
        if pos == end:
            if dist < shortest_path_score:
                shortest_path_score = dist
                shortest_paths = [path + [pos]]
            elif dist == shortest_path_score:
                shortest_paths.append(path + [pos])
            continue
        for dz in get_valid_moves(maze, pos):
            z = pos + dz
            zz = pos + 2 * dz
            new_dist = dist + (1 if direction == dz else 1001)
            # suboptimal for part 1, replace with
            # if new_dist < distances[z]:
            if (
                new_dist <= distances[z]
                or maze.get(zz) != "#"
                and new_dist + 1 <= distances[pos + 2 * dz]
            ):
                distances[z] = new_dist
                queue.append((new_dist, z, dz, path + [pos]))
    return shortest_path_score, shortest_paths


def part_1(input_data):
    maze = parse_input(input_data)
    score, _ = djikstra(maze)
    return score


def part_2(input_data):
    maze = parse_input(input_data)
    _, paths = djikstra(maze)
    return len({z for path in paths for z in path})
