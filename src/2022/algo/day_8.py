def part_1(input_data):
    tree_rows = list(input_data)
    h = len(tree_rows)
    w = len(tree_rows[0])
    visible_trees = {
        (i, j)
        for j, row in enumerate(tree_rows)
        for i, tree_height in enumerate(row)
        if all(tree_rows[j][x] < tree_height for x in range(i - 1, -1, -1))
        or all(tree_rows[j][x] < tree_height for x in range(i + 1, w))
        or all(tree_rows[y][i] < tree_height for y in range(j - 1, -1, -1))
        or all(tree_rows[y][i] < tree_height for y in range(j + 1, h))
    }

    return len(visible_trees)


def part_2(input_data):
    tree_rows = list(input_data)
    h = len(tree_rows)
    w = len(tree_rows[0])

    best_score = 0

    for j, row in enumerate(tree_rows):
        for i, tree_height in enumerate(row):
            score_left = 0
            for x in range(i - 1, -1, -1):
                score_left += 1
                if tree_rows[j][x] >= tree_height:
                    break
            score_right = 0
            for x in range(i + 1, w):
                score_right += 1
                if tree_rows[j][x] >= tree_height:
                    break
            score_top = 0
            for y in range(j - 1, -1, -1):
                score_top += 1
                if tree_rows[y][i] >= tree_height:
                    break
            score_bottom = 0
            for y in range(j + 1, h):
                score_bottom += 1
                if tree_rows[y][i] >= tree_height:
                    break
            score = score_left * score_right * score_top * score_bottom
            if score > best_score:
                best_score = score

    return best_score
