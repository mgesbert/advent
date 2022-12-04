from advent_2020.helpers import get_input


if __name__ == "__main__":
    data = list(get_input())
    result = 1
    for x, y in [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]:
        tree_count = 0
        for j in range(0, len(data), y):
            tree_count += data[j][(x * j // y) % len(data[0])] == "#"
        result *= tree_count
        print(tree_count)
    print(result)
