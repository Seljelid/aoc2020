import pandas as pd


def rain_risk():
    df = pd.read_csv("data/20201212.txt", header=None, names=["raw"])
    df["action"] = df.apply(lambda x: x["raw"][0], axis=1)
    df["value"] = df.apply(lambda x: int(x["raw"][1:]), axis=1)

    pos = {"N": 0, "S": 0, "E": 0, "W": 0}
    deg_to_dir = {0: "E", 90: "S", 180: "W", 270: "N"}
    deg = 0
    for _, row in df.iterrows():
        direction = deg_to_dir[deg]
        if row.action == "F":
            pos[direction] += row.value
        elif row.action in pos.keys():
            pos[row.action] += row.value
        else:
            deg = _change_direction(deg, row.action, row.value)

    east_west = abs(pos["E"] - pos["W"])
    south_north = abs(pos["N"] - pos["S"])
    manhattan = east_west + south_north
    print(f"The Manhattan distance is: {manhattan}")

    # Part 2
    waypoint = {"x": 10, "y": 1}
    pos = {"x": 0, "y": 0}
    moves = {
        "N": {"x": 0, "y": 1},
        "S": {"x": 0, "y": -1},
        "E": {"x": 1, "y": 0},
        "W": {"x": -1, "y": 0},
    }

    for _, row in df.iterrows():
        if row.action == "F":
            pos["x"] += waypoint["x"] * row.value
            pos["y"] += waypoint["y"] * row.value
        elif row.action in moves:
            move = moves[row.action]
            waypoint["x"] += move["x"] * row.value
            waypoint["y"] += move["y"] * row.value
        else:
            waypoint = _rotate_waypoint(waypoint, row.action, row.value)

    manhattan = abs(pos["x"]) + abs(pos["y"])
    print(f"The Manhattan distance is: {manhattan}")


def _change_direction(cur_deg, turn, deg):
    if turn == "L":
        new_deg = (cur_deg - deg) % 360
    else:
        new_deg = (cur_deg + deg) % 360
    return new_deg


def _rotate_waypoint(waypoint, turn, deg):
    quadrant = deg // 90
    quadrant %= 4
    if turn == "L":
        quadrant = 4 - quadrant
    for _ in range(quadrant):
        waypoint = {"x": waypoint["y"], "y": -waypoint["x"]}
    return waypoint


if __name__ == "__main__":
    rain_risk()