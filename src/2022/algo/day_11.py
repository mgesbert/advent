from math import prod


def parse(input_data):
    monkeys = []
    for line in input_data:
        if not line:
            continue
        if line.startswith("Monkey"):
            monkeys.append(
                {
                    "items": eval(f"[{next(input_data)[len('  Starting items: '):]}]"),
                    "operation": eval(
                        f"lambda old: {next(input_data)[len('  Operation: new = '):]}"
                    ),
                    "test": int(eval(next(input_data).split()[-1])),
                    "if_true": int(eval(next(input_data).split()[-1])),
                    "if_false": int(eval(next(input_data).split()[-1])),
                }
            )

    return monkeys


def play(monkeys, rounds, transform_item):
    total_inspected = [0] * len(monkeys)

    for _ in range(rounds):
        for i, monkey in enumerate(monkeys):
            total_inspected[i] += len(monkey["items"])
            for item in monkey["items"]:
                worry_level = transform_item(monkey["operation"](item))
                monkeys[
                    monkey[
                        "if_true" if worry_level % monkey["test"] == 0 else "if_false"
                    ]
                ]["items"].append(worry_level)
            monkey["items"] = []

    return sorted(total_inspected)[-1] * sorted(total_inspected)[-2]


def part_1(input_data):
    monkeys = parse(input_data)

    return play(monkeys, 20, lambda x: x // 3)


def part_2(input_data):
    monkeys = parse(input_data)
    modulus = prod(monkey["test"] for monkey in monkeys)

    return play(monkeys, 10000, lambda x: x % modulus)
