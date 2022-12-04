def part_1(input_data):
    pos = {"h": 0, "v": 0}
    for l in input_data:
        d, v = l.split()
        pos[{"down": "v", "up": "v", "forward": "h"}[d]] += {
            "down": 1,
            "up": -1,
            "forward": 1,
        }[d] * int(v)
    return pos["h"] * pos["v"]


def part_2(input_data):
    h, v, a = 0, 0, 0
    for l in input_data:
        d, x = l.split()
        x = int(x)
        a += {"down": 1, "up": -1, "forward": 0}[d] * x
        h += {"down": 0, "up": 0, "forward": 1}[d] * x
        v += {"down": 0, "up": 0, "forward": 1}[d] * a * x
    return h * v
