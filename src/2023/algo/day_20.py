import re
from collections import deque
import math


def get_flip_flop():
    state = False

    def flip_flop(_, signal):
        nonlocal state
        if signal:
            return None
        state = not state
        return state

    return flip_flop


def get_conjunction(modules):
    state = {module: False for module in modules}

    def conjunction(module, signal):
        nonlocal state
        state[module] = signal
        return not all(state.values())

    return conjunction


def parse_input(input_data):
    modules = {}
    broadcasts = []
    for line in input_data:
        if line.startswith("broadcaster"):
            broadcasts = line.split(" -> ")[1].split(", ")
        else:
            type_, module_name, targets = re.search(
                r"(%|&)(\w+) -> (.+)", line
            ).groups()
            targets = targets.split(", ")
            modules[module_name] = (type_, targets)

    for module_name, (type_, targets) in modules.items():
        if type_ == "%":
            modules[module_name] = get_flip_flop(), targets
        elif type_ == "&":
            modules[module_name] = (
                get_conjunction([k for k, v in modules.items() if module_name in v[1]]),
                targets,
            )

    return modules, broadcasts


def part_1(input_data):
    modules, broadcasts = parse_input(input_data)

    highs = lows = 0

    for _ in range(1000):
        queue = deque([("broadcaster", module, False) for module in broadcasts])
        lows += len(broadcasts) + 1
        while queue:
            source, module, signal = queue.popleft()
            func, targets = modules.get(module, (lambda *_: None, []))
            value = func(source, signal)
            if value is None:
                continue
            for target in targets:
                highs += value is True
                lows += value is False
                queue.append((module, target, value))

    return highs * lows


def part_2(input_data):
    modules, broadcasts = parse_input(input_data)

    highs = lows = 0

    high_to_th = {}
    for i in range(1, 10000):
        queue = deque([("broadcaster", module, False) for module in broadcasts])
        lows += len(broadcasts) + 1
        while queue:
            source, module, signal = queue.popleft()
            func, targets = modules.get(module, (lambda *_: None, []))
            value = func(source, signal)
            if value is None:
                continue
            for target in targets:
                if (
                    value is True
                    and target == "th"
                    and module not in high_to_th
                    and i > 0
                ):
                    high_to_th[module] = i
                highs += value is True
                lows += value is False
                queue.append((module, target, value))
    return math.lcm(*high_to_th.values())
