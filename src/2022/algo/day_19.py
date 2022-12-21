import re
from collections import deque


def parse(input_data):
    regex = r"Blueprint \d+: Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian."
    blueprints = []
    for line in input_data:
        data = re.match(regex, line)
        if not data:
            raise Exception(line)
        blueprints.append(
            {
                "ore_robot": {"ore": int(data.groups()[0])},
                "clay_robot": {"ore": int(data.groups()[1])},
                "obsidian_robot": {
                    "ore": int(data.groups()[2]),
                    "clay": int(data.groups()[3]),
                },
                "geode_robot": {
                    "ore": int(data.groups()[4]),
                    "obsidian": int(data.groups()[5]),
                },
            }
        )
    return blueprints


State = tuple[int, int, int, int, int, int, int, int, int]


def compute_next_state(
    blueprint,
    action,
    minute,
    ore,
    clay,
    obsidian,
    geodes,
    ore_robots,
    clay_robots,
    obsidian_robots,
    geode_robots,
):
    if action == "NOOP":
        return (
            minute + 1,
            ore + ore_robots,
            clay + clay_robots,
            obsidian + obsidian_robots,
            geodes + geode_robots,
            ore_robots,
            clay_robots,
            obsidian_robots,
            geode_robots,
        )
    if action == "ORE":
        return (
            minute + 1,
            ore + ore_robots - blueprint["ore_robot"]["ore"],
            clay + clay_robots,
            obsidian + obsidian_robots,
            geodes + geode_robots,
            ore_robots + 1,
            clay_robots,
            obsidian_robots,
            geode_robots,
        )
    if action == "CLAY":
        return (
            minute + 1,
            ore + ore_robots - blueprint["clay_robot"]["ore"],
            clay + clay_robots,
            obsidian + obsidian_robots,
            geodes + geode_robots,
            ore_robots,
            clay_robots + 1,
            obsidian_robots,
            geode_robots,
        )
    if action == "OBSIDIAN":
        return (
            minute + 1,
            ore + ore_robots - blueprint["obsidian_robot"]["ore"],
            clay + clay_robots - blueprint["obsidian_robot"]["clay"],
            obsidian + obsidian_robots,
            geodes + geode_robots,
            ore_robots,
            clay_robots,
            obsidian_robots + 1,
            geode_robots,
        )
    if action == "GEODE":
        return (
            minute + 1,
            ore + ore_robots - blueprint["geode_robot"]["ore"],
            clay + clay_robots,
            obsidian + obsidian_robots - blueprint["geode_robot"]["obsidian"],
            geodes + geode_robots,
            ore_robots,
            clay_robots,
            obsidian_robots,
            geode_robots + 1,
        )
    raise ValueError(f"Unknown action: {action}")


CACHE = set()


def append(stack, state):
    truncated_state = tuple(state[1:])
    if truncated_state in CACHE:
        return
    CACHE.add(truncated_state)
    stack.append(state)


def get_max_geodes(nb_steps, blueprint):
    stack: deque[State] = deque([(0, 0, 0, 0, 0, 1, 0, 0, 0)])
    result = 0
    max_ore = max(
        blueprint["ore_robot"]["ore"],
        blueprint["clay_robot"]["ore"],
        blueprint["obsidian_robot"]["ore"],
        blueprint["geode_robot"]["ore"],
    )
    max_clay = blueprint["obsidian_robot"]["clay"]
    max_obsidian = blueprint["geode_robot"]["obsidian"]

    while stack:
        appended = False
        state = stack.popleft()

        (
            minute,
            ore,
            clay,
            obsidian,
            geodes,
            ore_robots,
            clay_robots,
            obsidian_robots,
            geode_robots,
        ) = state

        if minute == nb_steps - 1:
            result = max(result, geodes + geode_robots)
            continue

        if (
            ore >= blueprint["geode_robot"]["ore"]
            and obsidian >= blueprint["geode_robot"]["obsidian"]
        ):
            append(stack, compute_next_state(blueprint, "GEODE", *state))
            appended = True

        if (
            ore >= blueprint["obsidian_robot"]["ore"]
            and clay >= blueprint["obsidian_robot"]["clay"]
            and obsidian_robots < blueprint["geode_robot"]["obsidian"]
            and minute < nb_steps - 2
        ):
            append(stack, compute_next_state(blueprint, "OBSIDIAN", *state))
            appended = True

        if (
            blueprint["clay_robot"]["ore"] + ore_robots
            > ore
            >= blueprint["clay_robot"]["ore"]
            and clay_robots < blueprint["obsidian_robot"]["clay"]
            and minute < nb_steps - 3
        ):
            append(stack, compute_next_state(blueprint, "CLAY", *state))
            appended = True

        if (
            blueprint["ore_robot"]["ore"] + ore_robots
            > ore
            >= blueprint["ore_robot"]["ore"]
            and ore_robots < max_ore
            and minute < nb_steps - 2
        ):
            append(stack, compute_next_state(blueprint, "ORE", *state))
            appended = True

        if (
            (
                clay_robots == 0
                and obsidian_robots == 0
                and ore
                < max(blueprint["ore_robot"]["ore"], blueprint["clay_robot"]["ore"])
            )
            or (
                obsidian_robots == 0
                and ore
                < max(
                    blueprint["ore_robot"]["ore"],
                    blueprint["clay_robot"]["ore"],
                    blueprint["obsidian_robot"]["ore"],
                )
            )
            or (ore < max_ore)
            or (clay < max_clay and clay_robots > 0)
            or (obsidian < max_obsidian and obsidian_robots > 0)
            or not appended
        ):
            append(stack, compute_next_state(blueprint, "NOOP", *state))

    return result


def part_1(input_data):
    blueprints = parse(input_data)
    score = 0
    for i, blueprint in enumerate(blueprints, start=1):
        global CACHE
        CACHE = set()
        score += i * get_max_geodes(24, blueprint)

    return score


def part_2(input_data):
    blueprints = parse(list(input_data)[:3])
    score = 1
    for blueprint in blueprints:
        global CACHE
        CACHE = set()
        score *= get_max_geodes(32, blueprint)

    return score
