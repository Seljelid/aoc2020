import re
import pandas as pd
import numpy as np


def ticket_translation():
    with open("data/20201216.txt") as f:
        lines = f.readlines()

    limitations = {}
    nearby_tickets = []
    mt = False
    nt = False
    for line in lines:
        if "-" in line:
            l = line.split(":")[0]
            bounds = re.findall(r"[0-9]+", line)
            bounds = [int(bound) for bound in bounds]
            limitations[l] = set(range(bounds[0], bounds[1] + 1)).union(
                set(range(bounds[2], bounds[3] + 1))
            )
        elif "your" in line:
            mt = True
        elif mt:
            my_ticket = line.strip().split(",")
            my_ticket = [int(entry) for entry in my_ticket]
            mt = False
        elif "nearby" in line:
            nt = True
        elif nt:
            ticket = line.strip().split(",")
            ticket = [int(entry) for entry in ticket]
            nearby_tickets.append(ticket)

    rough_limitations = set()
    for limitation in limitations.values():
        rough_limitations = rough_limitations.union(limitation)

    valid_tickets = []
    invalid_count = 0
    for ticket in nearby_tickets:
        t = set(ticket)
        invalid = t.difference(rough_limitations)
        invalid_count += sum(invalid)
        if not invalid:
            valid_tickets.append(ticket)

    print(f"Scanning error rate: {invalid_count}")

    # Part 2
    possible_limitations = {i: [] for i, _ in enumerate(limitations)}
    df = pd.DataFrame(valid_tickets)
    for limitation, bounds in limitations.items():
        could_be = df.isin(bounds).sum() == df.shape[0]
        could_be = could_be[could_be == True]
        for i in could_be.index:
            possible_limitations[i].append(limitation)
    possible_limitations = {k: set(v) for k, v in possible_limitations.items()}

    departure_values = []
    order = sorted(possible_limitations, key=lambda k: len(possible_limitations[k]))
    for i in order:
        secured = possible_limitations[i].pop()
        if secured.startswith("departure"):
            departure_values.append(my_ticket[i])
        for v in possible_limitations.values():
            v.discard(secured)

    print(f"The departure product is {np.prod(departure_values)}")


if __name__ == "__main__":
    ticket_translation()
