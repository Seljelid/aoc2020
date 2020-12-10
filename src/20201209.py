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
    # import timeit

    # t1 = timeit.Timer(lambda: _find_weakness(input, number))
    # print(t1.timeit(100) / 100)
    # t2 = timeit.Timer(lambda: _find_weakness_brutus(input, number))
    # print(t2.timeit(100) / 100)
    # weakness = _find_weakness(input, number)
    # print(f"The weakness is {weakness}")
    weakness = _find_weakness_brutus(input, number)
    print(f"The weakness is {weakness}")


def _find_weakness(input: list, number: int):
    for idx, _ in enumerate(input):
        found = number in itertools.accumulate(input[idx:])
        if found:
            accumulates = list(itertools.accumulate(input[idx:]))
            found_at = accumulates.index(number)
            accumulates = np.array(accumulates[0:found_at])
            accumulates[1:] -= accumulates[:-1].copy()
            return accumulates.min() + accumulates.max()


def _find_weakness_brutus(input: list, number: list):
    chunk_size = 2
    found = False
    while not found:
        overlap = chunk_size - 1
        chunks = [
            input[idx : idx + chunk_size]
            for idx in range(0, len(input), chunk_size - overlap)
        ]
        sums = [sum(chunk) for chunk in chunks]
        found = number in sums
        if found:
            at = sums.index(number)
            pieces = chunks[at]
            return min(pieces) + max(pieces)
        chunk_size += 1


def _sum_in_permutations(preamble: list, number: int) -> bool:
    perms = list(itertools.permutations(preamble, 2))
    sums = [sum(perm) for perm in perms]
    return number in sums


if __name__ == "__main__":
    encoding_error()