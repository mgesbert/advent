from advent_2021.helpers import get_input


PAIRS = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

VALUES = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

if __name__ == "__main__":
    error_count = 0
    for line in get_input():
        stack: list[str] = []
        for c in line:
            if c in PAIRS:
                stack.append(c)
            elif stack and c == PAIRS[stack[-1]]:
                stack.pop()
            else:
                error_count += VALUES[c]
                break

    print(error_count)
