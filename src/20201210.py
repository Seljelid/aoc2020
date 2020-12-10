import numpy as np


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

    # Part 2
    graph = np.empty([len(adapters), len(adapters)])
    for x, first in enumerate(adapters):
        for y, second in enumerate(adapters):
            if second - first in range(1, 4):
                graph[x][y] = True
            else:
                graph[x][y] = False

    start = 0
    goal = len(adapters) - 1
    count = _count_arrangements(graph=graph, start=start, goal=goal)
    print(f"Number of arrangements: {count}")


def _count_arrangements(graph, start, goal):
    count = np.zeros([goal, goal, goal], dtype=int)
    for z in range(0, goal):
        for x in range(goal):
            for y in range(goal):
                count[x][y][z] = 0

            if z == 0 and x == y:
                count[x][y][z] = 1
            if z == 1 and graph[x][y]:
                count[x][y][z] = 1

            if z > 1:
                for idx in range(goal):
                    if graph[x][idx]:
                        count[x][y][z] += count[idx][y][z - 1]
    return sum(count[start][goal - 1])


if __name__ == "__main__":
    adapter_array()