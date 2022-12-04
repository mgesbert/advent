def part_1(input_data):
    def bingo(board: list[list[int]], n: int):
        return sum(sum(i for i in line if i != -1) for line in board) * n

    data = list(input_data)
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
                    return bingo(board, n)
            for c in range(5):
                if all(line[c] == -1 for line in board):
                    return bingo(board, n)


def part_2(input_data):
    def bingo(board: list[list[int]], n: int):
        return sum(sum(i for i in line if i != -1) for line in board) * n

    data = list(input_data)
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
                    return bingo(boards[0], n)
                boards_to_delete.add(b)

        boards = [board for b, board in enumerate(boards) if b not in boards_to_delete]
