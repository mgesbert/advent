from advent_2021.helpers import get_input


if __name__ == "__main__":
    pos = {"h": 0, "v": 0}
    for l in get_input():
        d, v = l.split()
        pos[{"down": "v", "up": "v", "forward": "h"}[d]] += {
            "down": 1,
            "up": -1,
            "forward": 1,
        }[d] * int(v)
    print(pos["h"] * pos["v"])
