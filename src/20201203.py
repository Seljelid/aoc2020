import numpy as np


def find_trees():
    data = np.loadtxt("data/20201203.txt", dtype="str", comments=None)
    tree_at = [
        [index for index, char in enumerate(_shift_string(s, 3 * idx)) if char == "#"]
        for idx, s in enumerate(data)
    ]
    tree_pos_flat = [tree_pos for row in tree_at for tree_pos in row]
    print(tree_pos_flat.count(0))


def _shift_string(string, places):
    first_part = string[0 : (places % len(string))]
    second_part = string[(places % len(string)) :]
    shifted_string = second_part + first_part
    return shifted_string


if __name__ == "__main__":
    find_trees()