def adapter_array():
    with open("data/20201210.txt") as f:
        lines = f.readlines()
        adapters = [int(line.strip()) for line in lines]

    device_rating = max(adapters) + 3
    adapters.append(device_rating)
    adapters.append(0)  # The outlet
    adapters = sorted(adapters)
    differances = [b - a for a, b in zip(adapters[:-1], adapters[1:])]
    print(f"The number is {differances.count(1) * differances.count(3)}")


if __name__ == "__main__":
    adapter_array()