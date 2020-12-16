import re
import itertools


def docking_data():
    with open("data/20201214.txt") as f:
        lines = f.readlines()

    memory = {}
    for line in lines:
        if line.startswith("mask"):
            mask = line.split("=")[1].strip()
        elif line.startswith("mem"):
            mem_place = int(re.search(r"\d+", line).group())
            value = int(re.search(r"\d+", line.split("=")[1]).group())
            value = bin(value)[2:].zfill(36)
            val = "".join(
                [
                    shifted_bit if shifted_bit in ["0", "1"] else bit
                    for shifted_bit, bit in zip(list(mask), list(value))
                ]
            )
            memory[mem_place] = val
        else:
            raise Exception("Invalid input")

    agg = sum([int(val, 2) for val in memory.values()])
    print(f"The sum is {agg} in part 1")

    # Part 2
    memory = {}
    for line in lines:
        if line.startswith("mask"):
            mask = line.split("=")[1].strip()
        elif line.startswith("mem"):
            mem_place = int(re.search(r"\d+", line).group())
            mem_place = bin(mem_place)[2:].zfill(36)
            value = int(re.search(r"\d+", line.split("=")[1]).group())
            addresses = _get_addresses(mask, mem_place)
            for address in addresses:
                memory[address] = value
        else:
            raise Exception("Invalid input")

    agg = sum(memory.values())
    print(f"The sum is {agg} in part 2")


def _get_addresses(mask: str, mem_place: str) -> list:
    mem_place = "".join(
        [
            shifted_bit if shifted_bit in ["1", "X"] else bit
            for shifted_bit, bit in zip(list(mask), list(mem_place))
        ]
    )
    xs = [match.start() for match in re.finditer("X", mem_place)]
    n_x = len(xs)
    permutations = [
        "".join(sequence) for sequence in itertools.product("01", repeat=n_x)
    ]
    addresses = []
    for perm in permutations:
        address = list(mem_place)
        for i, bit in enumerate(perm):
            address[xs[i]] = bit
        addresses.append(int("".join(address), 2))

    return addresses


if __name__ == "__main__":
    docking_data()