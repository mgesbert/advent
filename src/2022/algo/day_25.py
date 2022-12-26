SNAFU = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}


def snafu_to_int(snafu):
    return sum(SNAFU[c] * 5**i for i, c in enumerate(snafu[::-1]))


def int_to_base_5(n):
    x = n % 5
    if x == n:
        return str(x)
    return int_to_base_5(n // 5) + str(x)


def int_to_snafu(n):
    snafu = ""
    hold = 0
    for c in int_to_base_5(n)[::-1]:
        x = int(c) + hold
        snafu = "012=-0"[x] + snafu
        hold = int(x > 2)
    if hold:
        snafu = str(hold) + snafu
    return snafu


def part_1(input_data):
    return int_to_snafu(sum(map(snafu_to_int, input_data)))


def part_2(input_data):
    list(input_data)
