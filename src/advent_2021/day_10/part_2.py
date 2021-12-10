from advent_2021.helpers import get_input


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

if __name__ == "__main__":
    scores: list[int] = []
    for line in get_input():
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

    print(sorted(scores)[len(scores) // 2])
