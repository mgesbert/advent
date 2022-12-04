def part_1(input_data):
    lines = list(input_data)
    acc = [""] * len(lines[0])
    for line in lines:
        for i, c in enumerate(line):
            acc[i] += c
    return int(
        "".join("1" if c.count("1") > c.count("0") else "0" for c in acc), 2
    ) * int("".join("0" if c.count("1") > c.count("0") else "1" for c in acc), 2)


def part_2(input_data):
    def find_rating(diag: list[str], keep_least_common: bool):
        pos = 0
        while len(diag) > 1:
            col = "".join(line[pos] for line in diag)
            bit_value = "01"[(col.count("1") >= col.count("0")) - keep_least_common]
            diag = [l for l in diag if l[pos] == bit_value]
            pos += 1
        return int(diag[0], 2)

    oxygen = co2 = list(input_data)

    return find_rating(oxygen, False) * find_rating(co2, True)
