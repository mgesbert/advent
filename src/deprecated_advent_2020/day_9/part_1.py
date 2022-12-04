import sys

from advent_2020.helpers import get_input


if __name__ == "__main__":
    queue: list[int] = []
    for i, line in enumerate(get_input()):
        n = int(line)
        if i < 25:
            queue.append(n)
            continue

        for j, x in enumerate(queue[:-1]):
            for y in queue[j + 1 :]:
                if x + y == n:
                    break
            else:
                continue
            break
        else:
            print(n)
            sys.exit(0)

        queue = queue[1:] + [n]
