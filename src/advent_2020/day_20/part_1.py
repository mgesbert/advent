import sys
from dataclasses import dataclass

from advent_2020.helpers import get_input


SIDES = {
    "right": "left",
    "left": "right",
    "top": "bottom",
    "bottom": "top",
}


@dataclass
class Tile:
    id: int
    top: str
    left: str
    right: str
    bottom: str

    def __init__(self, id_: int, top: str, left: str, right: str, bottom: str):
        self.id = id_
        self.top = top
        self.left = left
        self.right = right
        self.bottom = bottom

    @classmethod
    def from_lines(cls, id_: int, lines: list[list[str]]):
        return cls(
            id_,
            "".join(lines[0]),
            "".join([line[0] for line in lines]),
            "".join([line[-1] for line in lines]),
            "".join(lines[-1]),
        )

    def rotate(self):
        return Tile(self.id, self.right, self.top[::-1], self.bottom[::-1], self.left)

    def flip(self):
        return Tile(self.id, self.top, self.right, self.left, self.bottom)

    def __getitem__(self, key: str):
        if key == "top":
            return self.top
        if key == "left":
            return self.left
        if key == "right":
            return self.right
        if key == "bottom":
            return self.bottom
        raise ValueError


Puzzle = dict[tuple[int, int], Tile]


def is_puzzle_valid(tiles: list[Tile], puzzle: Puzzle):
    side_length = len(tiles)
    return (
        max([x for x, _ in puzzle]) - min([x for x, _ in puzzle]) < side_length
        and max([y for _, y in puzzle]) - min([y for _, y in puzzle]) < side_length
    )


def nothing(t: Tile):
    return t


def backtracking(
    tiles: list[Tile],
    puzzle: Puzzle | None = None,
    used: set[int] | None = None,
) -> Puzzle | None:
    if used is None:
        used = set()

    if puzzle is None:
        puzzle = {(0, 0): tiles[0]}
        used |= {tiles[0].id}
        return backtracking(tiles, puzzle, used)

    if not is_puzzle_valid(tiles, puzzle):
        return None

    if len(tiles) == len(puzzle):
        return puzzle

    for (x0, y0), t0 in puzzle.items():
        for x1, y1, s0 in [
            (x0 - 1, y0, "right"),
            (x0 + 1, y0, "left"),
            (x0, y0 - 1, "top"),
            (x0, y0 + 1, "bottom"),
        ]:
            s1 = SIDES[s0]
            if (x1, y1) in puzzle:
                continue
            for t1 in tiles:
                if t1.id in used:
                    continue
                for action in [
                    nothing,
                    Tile.rotate,
                    Tile.rotate,
                    Tile.rotate,
                    Tile.flip,
                    Tile.rotate,
                    Tile.rotate,
                    Tile.rotate,
                ]:
                    t1 = action(t1)
                    if t1[s1] != t0[s0]:
                        continue
                    next_puzzle = dict(puzzle)
                    next_puzzle[(x1, y1)] = t1
                    result = backtracking(tiles, next_puzzle, used | {t1.id})
                    if result is not None:
                        return result

    return None


if __name__ == "__main__":
    tiles: list[Tile] = []
    lines: list[list[str]] = []
    tile_id: int = 0
    for line in get_input():
        if line.startswith("Tile"):
            lines = []
            tile_id = int(line[5:9])
            continue
        if line == "":
            tiles.append(Tile.from_lines(tile_id, lines))
            continue
        lines.append(list(line))
    tiles.append(Tile.from_lines(tile_id, lines))

    image = backtracking(tiles)
    if image is None:
        sys.exit(1)
    min_x = min([x for x, _ in image.keys()])
    max_x = max([x for x, _ in image.keys()])
    min_y = min([y for _, y in image.keys()])
    max_y = max([y for _, y in image.keys()])

    print(
        image[(min_x, min_y)].id
        * image[(max_x, min_y)].id
        * image[(min_x, max_y)].id
        * image[(max_x, max_y)].id
    )
