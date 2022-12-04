import re

import regex  # type: ignore
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
    input_getter = get_input()
    rules: dict[int, str] = {}
    count = 0
    for line in input_getter:
        if len(line) == 0:
            break
        i, rule = line.split(": ")
        rules[int(i)] = f" {rule} "

    rule = interpolate(rules, rules[0]).replace(" ", "").replace('"', "")
    rule_31 = interpolate(rules, rules[31]).replace(" ", "").replace('"', "")
    rule_42 = interpolate(rules, rules[42]).replace(" ", "").replace('"', "")

    for line in input_getter:
        if re.fullmatch(rule, line) is not None:
            count += 1
            continue

        for i in range(len(line)):
            s1, s2 = line[:i], line[i:]

            if (
                re.fullmatch(rf"({rule_42})+", s1) is not None
                and regex.fullmatch(rf"({rule_42})(?:(?R))*+({rule_31})", s2)  # type: ignore
                is not None
            ):
                count += 1
                break

    print(count)
