import numpy as np


def find_trees():
    instructions = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    n_trees = []
    for instruction in instructions:
        trees = traverse_map(instruction[0], instruction[1])
        n_trees.append(trees)
    print(np.prod(n_trees))


def traverse_map(right=3, down=1):
    data = np.loadtxt("data/20201203.txt", dtype="str", comments=None)
    tree_at = [
        [
            index
            for index, char in enumerate(_shift_string(s, int((right * idx) / down)))
            if char == "#"
        ]
        for idx, s in enumerate(data)
    ]
    tree_pos_flat = [
        tree_pos
        for idx, row in enumerate(tree_at)
        for tree_pos in row
        if idx % down == 0
    ]
    return tree_pos_flat.count(0)


def _shift_string(string, places):
    first_part = string[0 : (places % len(string))]
    second_part = string[(places % len(string)) :]
    shifted_string = second_part + first_part
    return shifted_string


if __name__ == "__main__":
    find_trees()