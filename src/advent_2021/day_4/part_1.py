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

        for board in boards:
            for line in board:
                if all(i == -1 for i in line):
                    bingo(board, n)
                    sys.exit(0)
            for c in range(5):
                if all(line[c] == -1 for line in board):
                    bingo(board, n)
                    sys.exit(0)
