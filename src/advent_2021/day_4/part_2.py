import sys

from advent_2021.helpers import get_input


def bingo(board: list[list[int]], n: int):
    print(sum(sum(i for i in line if i != -1) for line in board) * n)


if __name__ == "__main__":
    data = list(get_input())
    numbers = map(int, data[0].split(","))
    boards: list[list[list[int]]] = []
    for i in range(len(data) // 6):
        board: list[list[int]] = []
        for j in range(6 * i + 2, 6 * i + 7):
            board.append([int(x) for x in data[j].split()])
        boards.append(board)

    for n in numbers:
        for board in boards:
            for line in board:
                for i, x in enumerate(line):
                    if x == n:
                        line[i] = -1

        boards_to_delete: set[int] = set()
        for b, board in enumerate(boards):
            if any(all(i == -1 for i in line) for line in board) or any(
                all(line[c] == -1 for line in board) for c in range(5)
            ):
                if len(boards) == 1:
                    bingo(boards[0], n)
                    sys.exit(0)
                boards_to_delete.add(b)

        boards = [board for b, board in enumerate(boards) if b not in boards_to_delete]
