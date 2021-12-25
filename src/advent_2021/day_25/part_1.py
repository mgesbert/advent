from advent_2021.helpers import get_input


if __name__ == "__main__":
    floor_map = list(get_input())
    previous_floor_map = []
    n = 0
    while previous_floor_map != floor_map:
        n += 1
        previous_floor_map = floor_map
        floor_map = [
            "".join(
                "."
                if c0 != ">" and c1 == "." or c1 == ">" and c2 == "."
                else ">"
                if c0 == ">" and c1 == "." or c1 == ">" and c2 != "."
                else c1
                for c0, c1, c2 in zip(line[-1] + line[:-1], line, line[1:] + line[0])
            )
            for line in floor_map
        ]
        floor_map = [
            "".join(
                "."
                if l0[i] != "v" and l1[i] == "." or l1[i] == "v" and l2[i] == "."
                else "v"
                if l0[i] == "v" and l1[i] == "." or l1[i] == "v" and l2[i] != "."
                else l1[i]
                for i in range(len(l1))
            )
            for l0, l1, l2 in zip(
                [floor_map[-1]] + floor_map[:-1],
                floor_map,
                floor_map[1:] + [floor_map[0]],
            )
        ]
    print(n)
