import pandas as pd
import numpy as np


def shuttle_search():

    with open("data/20201213.txt") as f:
        earliest_departure = int(f.readline().strip())
        fleet = f.readline().strip().replace("x,", "").split(",")

    fleet = [int(bus) for bus in fleet]
    multipliers = [(earliest_departure // bus) + 1 for bus in fleet]
    departures = list(np.multiply(fleet, multipliers))
    my_departure = min(departures)
    bus_id = fleet[departures.index(my_departure)]
    wait = my_departure - earliest_departure
    print(f"Magic number is: {bus_id*wait}")

    # Part 2
    with open("data/20201213.txt") as f:
        _ = f.readline()
        fleet = f.readline().strip().split(",")

    fleet = (
        pd.DataFrame(fleet)
        .reset_index()
        .rename(columns={"index": "offset", 0: "bus_id"})
    )
    fleet = fleet[fleet.bus_id != "x"]
    fleet = fleet.astype("int32")
    fleet["offset_diff"] = fleet.bus_id - fleet.offset

    agg = 0
    prod = int(np.prod(fleet.bus_id))
    for b_id, od in zip(fleet.bus_id, fleet.offset_diff):
        p = prod // b_id
        agg += od * pow(p, -1, b_id) * p
    timestamp = agg % prod

    print(f"The timestamp is {timestamp}")


if __name__ == "__main__":
    shuttle_search()
