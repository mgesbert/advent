HALLWAY_REST_POS = [0, 1, 3, 5, 7, 9, 10]
POD_POS = {"A": 2, "B": 4, "C": 6, "D": 8}
COST = {"A": 1, "B": 10, "C": 100, "D": 1000}
TARGET = {
    "A": ["A", "A", "A", "A"],
    "B": ["B", "B", "B", "B"],
    "C": ["C", "C", "C", "C"],
    "D": ["D", "D", "D", "D"],
}


def possible_moves(hallway: list[str], pods: dict[str, list[str]]):
    for pos, amphipod in enumerate(hallway):
        if amphipod == ".":
            continue
        if all(
            c == "."
            for c in hallway[
                min(pos + 1, POD_POS[amphipod]) : max(pos - 1, POD_POS[amphipod]) + 1
            ]
        ) and (all(a == amphipod for a in pods[amphipod])):
            yield (
                hallway[:pos] + ["."] + hallway[pos + 1 :],
                {**pods, amphipod: [amphipod] + pods[amphipod]},
                (abs(POD_POS[amphipod] - pos) + 4 - len(pods[amphipod]))
                * COST[amphipod],
            )
            return
    for pod_name, pod in pods.items():
        if all(c == pod_name for c in pod):
            continue
        amphipod = pod[0]
        for rest_pos in HALLWAY_REST_POS:
            if any(
                c != "."
                for c in hallway[
                    min(rest_pos, POD_POS[pod_name]) : max(rest_pos, POD_POS[pod_name])
                    + 1
                ]
            ):
                continue
            yield (
                hallway[:rest_pos] + [amphipod] + hallway[rest_pos + 1 :],
                {**pods, pod_name: pod[1:]},
                (abs(POD_POS[pod_name] - rest_pos) + 5 - len(pod)) * COST[amphipod],
            )


if __name__ == "__main__":
    hallway = ["."] * 11
    pods = {
        "A": ["C", "D", "D", "B"],
        "B": ["D", "C", "B", "A"],
        "C": ["A", "B", "A", "D"],
        "D": ["B", "A", "C", "C"],
    }
    stack: list[tuple[list[str], dict[str, list[str]], int]] = [(hallway, pods, 0)]
    full_stack = {f"{hallway}{pods['A'],pods['B'],pods['C'],pods['D']}0"}
    best = float("inf")
    while stack:
        (hallway, pods, cost) = stack.pop()
        if pods == TARGET:
            best = min(best, cost)
            continue
        for h, p, c in possible_moves(hallway, pods):
            if f"{h}{p['A']}{p['B']}{p['C']}{p['D']}{cost + c}" in full_stack:
                continue
            stack.append((h, p, cost + c))
            full_stack.add(f"{h}{p['A']}{p['B']}{p['C']}{p['D']}{cost + c}")
    print(best)
