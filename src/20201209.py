import itertools


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


def _sum_in_permutations(preamble: list, number: int) -> bool:
    perms = list(itertools.permutations(preamble, 2))
    sums = [sum(perm) for perm in perms]
    return number in sums


if __name__ == "__main__":
    encoding_error()