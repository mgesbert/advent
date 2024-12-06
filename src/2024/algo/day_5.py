def parse_input(input_data):
    rules = []
    updates = []
    for line in input_data:
        if "|" in line:
            rules.append([int(x) for x in line.split("|")])
        elif "," in line:
            updates.append([int(x) for x in line.split(",")])
    return rules, updates


def is_valid(update, rule):
    a, b = rule
    return a not in update or b not in update or update.index(a) < update.index(b)


def reorder(update, rules):
    while True:
        for a, b in rules:
            if a not in update or b not in update:
                continue
            i_a, i_b = update.index(a), update.index(b)
            if i_a < i_b:
                continue
            update[i_a], update[i_b] = update[i_b], update[i_a]
            break
        else:
            return update


def part_1(input_data):
    rules, updates = parse_input(input_data)

    return sum(
        update[(len(update) - 1) // 2]
        for update in updates
        if all(is_valid(update, rule) for rule in rules)
    )


def part_2(input_data):
    rules, updates = parse_input(input_data)

    return sum(
        reorder(update, rules)[(len(update) - 1) // 2]
        for update in updates
        if any(not is_valid(update, rule) for rule in rules)
    )
