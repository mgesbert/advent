import re

from cachetools import LRUCache, cached
from cachetools.keys import hashkey
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import shortest_path


def parse(input_data):
    edges = []
    rates = {}
    for line in input_data:
        data = re.match(
            r"Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? (.*)", line
        )
        if not data:
            raise Exception(line)
        valve, rate_str, dests = data.groups()
        rates[valve] = int(rate_str)
        for node in dests.split(", "):
            edges.append((valve, node))

    nodes = sorted(rates.keys())

    graph = [[0] * len(rates) for _ in range(len(rates))]

    for a, b in edges:
        i = nodes.index(a)
        j = nodes.index(b)

        graph[i][j] = 1
        graph[j][i] = 1

    graph = csr_matrix(graph)
    dist_matrix = shortest_path(csgraph=graph, directed=False)

    compact_nodes = [k for k, v in rates.items() if v > 0 or k == "AA"]
    compact_graph = {n: {} for n in compact_nodes}

    for a in compact_nodes:
        for b in compact_nodes:
            if a == b:
                continue
            i = nodes.index(a)
            j = nodes.index(b)

            compact_graph[a][b] = int(dist_matrix[i][j])
            compact_graph[b][a] = int(dist_matrix[j][i])

    compact_rates = {k: v for k, v in rates.items() if k in compact_nodes}

    return compact_nodes, compact_graph, compact_rates


HIGHEST_FLOW_CACHE = {}


def get_flow(rates, open_valves):
    return sum(rates[v] for v in open_valves)


@cached(
    cache=HIGHEST_FLOW_CACHE,
    key=lambda graph, nodes, rates, current, open_valves=None, turns_left=30: hashkey(
        current, str(sorted(open_valves or [])), turns_left
    ),
)
def highest_flow(graph, nodes, rates, current, open_valves=None, turns_left=30):
    if open_valves is None:
        open_valves = set()

    # do nothing
    best_remaining_flow = turns_left * get_flow(rates, open_valves)
    instructions = [
        f"position {current}, turn {31 - turns_left}, flow {get_flow(rates, open_valves)}, do nothing, total {best_remaining_flow}"
    ]

    # move to other nodes
    for node in nodes:
        if node == current:
            continue

        if node in open_valves:
            continue

        if rates[node] == 0:
            continue

        if graph[current][node] > turns_left:
            continue

        flow, inst = highest_flow(
            graph,
            nodes,
            rates,
            node,
            open_valves,
            turns_left - graph[current][node],
        )
        flow += graph[current][node] * get_flow(rates, open_valves)
        if flow > best_remaining_flow:
            best_remaining_flow = flow
            instructions = [
                f"position {current}, turn {31 - turns_left}, flow {get_flow(rates, open_valves)}, move to {node} in {graph[current][node]} turns, total {best_remaining_flow}"
            ] + inst

    # open current valve
    if current not in open_valves and turns_left > 0:
        flow, inst = highest_flow(
            graph, nodes, rates, current, open_valves | {current}, turns_left - 1
        )
        flow += get_flow(rates, open_valves)

        if flow > best_remaining_flow:
            best_remaining_flow = flow
            instructions = [
                f"position {current}, turn {31 - turns_left}, flow {get_flow(rates, open_valves)}, opened valve, total {best_remaining_flow}"
            ] + inst

    return best_remaining_flow, instructions


HIGHEST_FLOW_DOUBLE_CACHE = LRUCache(maxsize=1000000)


def possible_next_positions(current_node, graph, nodes, open_valves, rates, turns_left):
    pass


@cached(
    cache=HIGHEST_FLOW_DOUBLE_CACHE,
    key=lambda graph, nodes, rates, current, open_valves=None, turns_left=30: hashkey(
        str(sorted(list(current))), str(sorted(open_valves or [])), turns_left
    ),
)
# current:
#   (("BB", 1), ("CC", 0)) -> init (("AA", 0), ("AA", 0))
def highest_flow_double(graph, nodes, rates, current, open_valves=None, turns_left=26):
    if turns_left == 0:
        return 0, []
    if open_valves is None:
        open_valves = set()

    (target_me, turns_me), (target_el, turns_el) = current

    # do nothing
    best_remaining_flow = turns_left * get_flow(rates, open_valves)
    instructions = [
        f"positions {current}, turn {27 - turns_left}, flow {get_flow(rates, open_valves)}, do nothing, total {best_remaining_flow}"
    ]

    my_valid_targets = (
        [
            (n, graph[target_me][n])
            for n in nodes
            if n != target_me
            and n != target_el
            and n not in open_valves
            and rates[n] > 0
            and graph[target_me][n] < turns_left
        ]
        + [(target_me, turns_left)]
        if turns_me == -1
        else [(target_me, turns_me)]
    )

    i = 0
    for my_target, my_turns in my_valid_targets:
        i += 1
        if turns_left == 26:
            print(i, len(my_valid_targets))
        el_valid_targets = (
            [
                (n, graph[target_el][n])
                for n in nodes
                if n != my_target
                and n != target_el
                and n not in open_valves
                and rates[n] > 0
                and graph[target_el][n] < turns_left
            ]
            + [(target_el, turns_left)]
            if turns_el == -1
            else [(target_el, turns_el)]
        )

        j = 0
        for el_target, el_turns in el_valid_targets:
            j += 1
            if turns_left == 26:
                print(j, len(my_valid_targets))
            if my_turns == 0 and el_turns == 0:
                # open both valves
                flow, inst = highest_flow_double(
                    graph,
                    nodes,
                    rates,
                    ((my_target, -1), (el_target, -1)),
                    open_valves | {my_target} | {el_target},
                    turns_left - 1,
                )
                flow += get_flow(rates, open_valves)

                if flow > best_remaining_flow:
                    best_remaining_flow = flow
                    instructions = [
                        f"positions {current}, turn {27 - turns_left}, flow {get_flow(rates, open_valves)}, opened {my_target} and {el_target}, total {best_remaining_flow}"
                    ] + inst
                continue

            if my_turns == 0:
                # open my valve
                flow, inst = highest_flow_double(
                    graph,
                    nodes,
                    rates,
                    ((my_target, -1), (el_target, el_turns - 1)),
                    open_valves | {my_target},
                    turns_left - 1,
                )
                flow += get_flow(rates, open_valves)

                if flow > best_remaining_flow:
                    best_remaining_flow = flow
                    instructions = [
                        f"positions {current}, turn {27 - turns_left}, flow {get_flow(rates, open_valves)}, opened {my_target}, el moves to {el_target} in {el_turns}, total {best_remaining_flow}"
                    ] + inst
                continue

            if el_turns == 0:
                # open my valve
                flow, inst = highest_flow_double(
                    graph,
                    nodes,
                    rates,
                    ((my_target, my_turns - 1), (el_target, -1)),
                    open_valves | {el_target},
                    turns_left - 1,
                )
                flow += get_flow(rates, open_valves)

                if flow > best_remaining_flow:
                    best_remaining_flow = flow
                    instructions = [
                        f"positions {current}, turn {27 - turns_left}, flow {get_flow(rates, open_valves)}, I move to {my_target} in {my_turns} turns, opened {el_target}, total {best_remaining_flow}"
                    ] + inst
                continue

            # move to other nodes
            turns_till_next_tick = min(my_turns, el_turns)
            flow, inst = highest_flow_double(
                graph,
                nodes,
                rates,
                (
                    (my_target, my_turns - turns_till_next_tick),
                    (el_target, el_turns - turns_till_next_tick),
                ),
                open_valves,
                turns_left - turns_till_next_tick,
            )
            flow += turns_till_next_tick * get_flow(rates, open_valves)
            if flow > best_remaining_flow:
                best_remaining_flow = flow
                instructions = [
                    f"positions {current}, turn {27 - turns_left}, flow {get_flow(rates, open_valves)}, I move to {my_target} in {my_turns} turns, el moves to {el_target} in {el_turns}, total {best_remaining_flow}"
                ] + inst

    return best_remaining_flow, instructions


def part_1(input_data):
    for k in list(HIGHEST_FLOW_CACHE.keys()):
        del HIGHEST_FLOW_CACHE[k]

    nodes, graph, rates = parse(input_data)

    flow, instructions = highest_flow(graph, nodes, rates, "AA")
    print("\n".join(instructions))
    return flow


def part_2(input_data):
    nodes, graph, rates = parse(input_data)
    flow, instructions = highest_flow_double(
        graph, nodes, rates, (("AA", -1), ("AA", -1))
    )
    print("\n".join(instructions))
    return flow
