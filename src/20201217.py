def conway_cubes():
    with open("data/20201217.txt") as f:
        lines = f.readlines()

    initial_state = []
    for line in lines:
        initial_state.append(list(line.strip()))

    active_state = []
    for x, row in enumerate(initial_state):
        for y, cell in enumerate(row):
            if cell == "#":
                active_state.append((x, y, 0))  # z = 0 in initial state

    for _ in range(6):
        active_state = _cycle_3d(active_state)

    print(f"There are {len(active_state)} active cubes")

    # Part 2
    active_state = []
    for x, row in enumerate(initial_state):
        for y, cell in enumerate(row):
            if cell == "#":
                active_state.append((x, y, 0, 0))  # z = w = 0 in initial state

    for _ in range(6):
        active_state = _cycle_4d(active_state)

    print(f"There are {len(active_state)} active cubes")


def _cycle_3d(current_active_state):
    new_active_state = []
    unique_active = set(current_active_state)
    neighbors = set(
        [
            (x + dx, y + dy, z + dz)
            for x, y, z in current_active_state
            for dx in range(-1, 2)
            for dy in range(-1, 2)
            for dz in range(-1, 2)
        ]
    )
    for new_x, new_y, new_z in neighbors:
        agg = sum(
            (new_x + dx, new_y + dy, new_z + dz) in unique_active
            for dx in range(-1, 2)
            for dy in range(-1, 2)
            for dz in range(-1, 2)
        )
        agg -= (new_x, new_y, new_z) in unique_active
        if agg == 3 or (agg == 2 and (new_x, new_y, new_z) in unique_active):
            new_active_state.append((new_x, new_y, new_z))
    return new_active_state


def _cycle_4d(current_active_state):
    new_active_state = []
    unique_active = set(current_active_state)
    neighbors = set(
        [
            (x + dx, y + dy, z + dz, w + dw)
            for x, y, z, w in current_active_state
            for dx in range(-1, 2)
            for dy in range(-1, 2)
            for dz in range(-1, 2)
            for dw in range(-1, 2)
        ]
    )
    for new_x, new_y, new_z, new_w in neighbors:
        agg = sum(
            (new_x + dx, new_y + dy, new_z + dz, new_w + dw) in unique_active
            for dx in range(-1, 2)
            for dy in range(-1, 2)
            for dz in range(-1, 2)
            for dw in range(-1, 2)
        )
        agg -= (new_x, new_y, new_z, new_w) in unique_active
        if agg == 3 or (agg == 2 and (new_x, new_y, new_z, new_w) in unique_active):
            new_active_state.append((new_x, new_y, new_z, new_w))
    return new_active_state


if __name__ == "__main__":
    conway_cubes()