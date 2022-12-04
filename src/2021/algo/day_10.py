def part_1(input_data):
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

    error_count = 0
    for line in input_data:
        stack: list[str] = []
        for c in line:
            if c in PAIRS:
                stack.append(c)
            elif stack and c == PAIRS[stack[-1]]:
                stack.pop()
            else:
                error_count += VALUES[c]
                break

    return error_count


def part_2(input_data):
    PAIRS = {
        "(": ")",
        "[": "]",
        "{": "}",
        "<": ">",
    }

    VALUES = {
        "(": 1,
        "[": 2,
        "{": 3,
        "<": 4,
    }

    scores: list[int] = []
    for line in input_data:
        stack: list[str] = []
        for c in line:
            if c in PAIRS:
                stack.append(c)
            elif stack and c == PAIRS[stack[-1]]:
                stack.pop()
            else:
                break
        else:
            score = 0
            for c in stack[::-1]:
                score *= 5
                score += VALUES[c]
            scores.append(score)

    return sorted(scores)[len(scores) // 2]
