from advent_2021.helpers import get_input


def find_rating(diag: list[str], keep_least_common: bool):
    pos = 0
    while len(diag) > 1:
        col = "".join(line[pos] for line in diag)
        bit_value = "01"[(col.count("1") >= col.count("0")) - keep_least_common]
        diag = [l for l in diag if l[pos] == bit_value]
        pos += 1
    return int(diag[0], 2)


if __name__ == "__main__":
    oxygen = list(get_input())
    co2 = list(get_input())

    print(find_rating(oxygen, False) * find_rating(co2, True))
