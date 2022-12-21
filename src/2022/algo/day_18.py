from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import shortest_path


def part_1(input_data):
    droplets = {eval(f"({line})") for line in input_data}
    return (
        sum((x + 1, y, z) not in droplets for x, y, z in droplets)
        + sum((x - 1, y, z) not in droplets for x, y, z in droplets)
        + sum((x, y + 1, z) not in droplets for x, y, z in droplets)
        + sum((x, y - 1, z) not in droplets for x, y, z in droplets)
        + sum((x, y, z + 1) not in droplets for x, y, z in droplets)
        + sum((x, y, z - 1) not in droplets for x, y, z in droplets)
    )


def get_index(x, y, z, width, height):
    return x + y * width + z * height * width


def part_2(input_data):
    droplets = {eval(f"({line})") for line in input_data}
    x0 = min(x for x, _, _ in droplets) - 1
    x1 = max(x for x, _, _ in droplets) + 1
    y0 = min(y for _, y, _ in droplets) - 1
    y1 = max(y for _, y, _ in droplets) + 1
    z0 = min(z for _, _, z in droplets) - 1
    z1 = max(z for _, _, z in droplets) + 1

    width = x1 - x0 + 1
    height = y1 - y0 + 1
    depth = z1 - z0 + 1
    nb_nodes = width * height * depth
    graph: list[list[int]] = [[0] * nb_nodes for _ in range(nb_nodes)]

    for x in range(x0, x1 + 1):
        for y in range(y0, y1 + 1):
            for z in range(z0, z1 + 1):
                if (x, y, z) in droplets:
                    continue
                if x > x0 and (x - 1, y, z) not in droplets:
                    graph[get_index(x, y, z, width, height)][
                        get_index(x - 1, y, z, width, height)
                    ] = 1
                if x < x1 and (x + 1, y, z) not in droplets:
                    graph[get_index(x, y, z, width, height)][
                        get_index(x + 1, y, z, width, height)
                    ] = 1
                if y > y0 and (x, y - 1, z) not in droplets:
                    graph[get_index(x, y, z, width, height)][
                        get_index(x, y - 1, z, width, height)
                    ] = 1
                if y < y1 and (x, y + 1, z) not in droplets:
                    graph[get_index(x, y, z, width, height)][
                        get_index(x, y + 1, z, width, height)
                    ] = 1
                if z > z0 and (x, y, z - 1) not in droplets:
                    graph[get_index(x, y, z, width, height)][
                        get_index(x, y, z - 1, width, height)
                    ] = 1
                if z < z1 and (x, y, z + 1) not in droplets:
                    graph[get_index(x, y, z, width, height)][
                        get_index(x, y, z + 1, width, height)
                    ] = 1

    graph = csr_matrix(graph)
    dist_matrix = shortest_path(csgraph=graph, directed=False, indices=0)

    return (
        sum(
            (x + 1, y, z) not in droplets
            and dist_matrix[get_index(x + 1, y, z, width, height)] != float("inf")
            for x, y, z in droplets
        )
        + sum(
            (x - 1, y, z) not in droplets
            and dist_matrix[get_index(x - 1, y, z, width, height)] != float("inf")
            for x, y, z in droplets
        )
        + sum(
            (x, y + 1, z) not in droplets
            and dist_matrix[get_index(x, y + 1, z, width, height)] != float("inf")
            for x, y, z in droplets
        )
        + sum(
            (x, y - 1, z) not in droplets
            and dist_matrix[get_index(x, y - 1, z, width, height)] != float("inf")
            for x, y, z in droplets
        )
        + sum(
            (x, y, z + 1) not in droplets
            and dist_matrix[get_index(x, y, z + 1, width, height)] != float("inf")
            for x, y, z in droplets
        )
        + sum(
            (x, y, z - 1) not in droplets
            and dist_matrix[get_index(x, y, z - 1, width, height)] != float("inf")
            for x, y, z in droplets
        )
    )
