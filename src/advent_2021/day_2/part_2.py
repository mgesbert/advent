from advent_2021.helpers import get_input


if __name__ == "__main__":
    h, v, a = 0, 0, 0
    for l in get_input():
        d, x = l.split()
        x = int(x)
        a += {"down": 1, "up": -1, "forward": 0}[d] * x
        h += {"down": 0, "up": 0, "forward": 1}[d] * x
        v += {"down": 0, "up": 0, "forward": 1}[d] * a * x
    print(h * v)
