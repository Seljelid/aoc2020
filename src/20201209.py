import itertools
import numpy as np


def encoding_error():
    with open("data/20201209.txt") as f:
        lines = f.readlines()
        input = [int(line.strip()) for line in lines]

    for idx, _ in list(enumerate(input))[0:-25]:
        preamble = input[idx : idx + 25]
        number = input[idx + 25]
        valid = _sum_in_permutations(preamble, number)
        if not valid:
            print(f"{number} is the first invalid number")
            break

    # Part 2
    weakness = _find_weakness(input, number)
    print(f"The weakness is {weakness}")


def _find_weakness(input: list, number: int):
    found = False
    start_idx = 0
    while not found:
        found = (
            number in np.cumsum(input[start_idx:])[1:]
        )  # From 1st position if the number itself present
        if found:
            accumulates = np.cumsum(input[start_idx:])
            found_at = np.argwhere(accumulates == number)[0][0]
            accumulates = accumulates[0:found_at]
            accumulates[1:] -= accumulates[:-1].copy()
            return accumulates.min() + accumulates.max()
        start_idx += 1


def _sum_in_permutations(preamble: list, number: int) -> bool:
    perms = list(itertools.permutations(preamble, 2))
    sums = [sum(perm) for perm in perms]
    return number in sums


if __name__ == "__main__":
    encoding_error()