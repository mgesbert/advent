import re

from advent_2020.helpers import get_input


def is_leaf(rule: str):
    return all(not c.isdigit() for c in rule)


def interpolate(rules: dict[int, str], rule: str) -> str:
    if is_leaf(rule):
        return rule
    if "|" in rule:
        rule = f"({rule})"
    interpolated_rules = {
        i: interpolate(rules, rules[int(i)]) for i in re.findall(r"(\d+)", rule)
    }
    for rule_id, interpolated_rule in interpolated_rules.items():
        regex = r"\D" + rule_id + r"\D"
        while re.search(regex, rule) is not None:
            rule = re.sub(
                regex,
                f" {interpolated_rule} ",
                rule,
            )
    return rule


if __name__ == "__main__":
    rules: dict[int, str] = {}
    for line in get_input():
        if len(line) == 0:
            break
        i, rule = line.split(": ")
        rules[int(i)] = f" {rule} "

    rule = interpolate(rules, rules[0]).replace(" ", "").replace('"', "")
    print(sum(re.fullmatch(rule, line) is not None for line in get_input()))
