import re


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
    print(f"The sum is {agg}")


if __name__ == "__main__":
    docking_data()