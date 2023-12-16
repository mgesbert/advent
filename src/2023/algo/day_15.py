import re


def custom_hash(s):
    h = 0
    for c in s:
        h = ((h + ord(c)) * 17) % 256
    return h


def part_1(input_data):
    return sum(custom_hash(step) for step in next(input_data).split(","))


def part_2(input_data):
    boxes = [[] for _ in range(256)]
    for step in next(input_data).split(","):
        label = re.search(r"^[a-zA-Z]+", step).group(0)
        label_hash = custom_hash(label)
        op = re.search(r"-|=", step).group(0)
        if op == "-":
            boxes[label_hash] = [(l, f) for (l, f) in boxes[label_hash] if l != label]
            continue
        focal = int(re.search(r"\d+$", step).group(0))
        if all(l != label for l, _ in boxes[label_hash]):
            boxes[label_hash].append((label, focal))
        else:
            boxes[label_hash] = [
                (l, f) if l != label else (l, focal) for (l, f) in boxes[label_hash]
            ]

    return sum(
        i * j * focal
        for i, lenses in enumerate(boxes, start=1)
        for j, (_, focal) in enumerate(lenses, start=1)
    )
