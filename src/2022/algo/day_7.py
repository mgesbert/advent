def dfs_with_side_effect(fs, sizes):
    i = len(sizes)
    sizes.append(0)
    for node in fs.values():
        if isinstance(node, int):
            sizes[i] += node
            continue
        sizes[i] += dfs_with_side_effect(node, sizes)
    return sizes[i]


def build_fs(input_data):
    fs = {}
    dir_stack = []
    next(input_data)
    current_dir = fs
    for line in input_data:
        if line == "$ cd ..":
            current_dir = dir_stack.pop()
            continue
        if line.startswith("$ cd"):
            dir_stack.append(current_dir)
            current_dir = current_dir[line[5:]]
            continue
        if line == "$ ls":
            continue
        if line.startswith("dir"):
            current_dir[line[4:]] = {}
            continue
        size, file = line.split()
        current_dir[file] = int(size)

    return fs


def get_dir_sizes(fs):
    dir_sizes = []
    dfs_with_side_effect(fs, dir_sizes)

    return dir_sizes


def part_1(input_data):
    fs = build_fs(input_data)
    dir_sizes = get_dir_sizes(fs)
    return sum(size for size in dir_sizes if size <= 100000)


def part_2(input_data):
    fs = build_fs(input_data)
    dir_sizes = get_dir_sizes(fs)
    return next(size for size in sorted(dir_sizes) if size >= dir_sizes[0] - 40000000)
