def part_1(input_data):
    return sum(
        int(
            next(c for c in line if c.isdigit())
            + next(c for c in line[::-1] if c.isdigit())
        )
        for line in input_data
    )


def replace_digits(line):
    translations = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    res = ""
    for i, c in enumerate(line):
        word = next((k for k in translations.keys() if line[i:].startswith(k)), None)
        if word:
            res += translations[word]
        else:
            res += c

    return res


def part_2(input_data):
    return sum(
        int(
            next(c for c in replace_digits(line) if c.isdigit())
            + next(c for c in replace_digits(line)[::-1] if c.isdigit())
        )
        for line in input_data
    )
