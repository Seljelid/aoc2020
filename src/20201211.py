import copy

""" 
    . = floor
    L = empty seat
    # = occupied
    - If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
    - If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
    - Otherwise, the seat's state does not change.
"""


def seating_system():
    with open("data/20201211.txt") as f:
        lines = f.readlines()
        seats = [list(line.strip()) for line in lines]

    orig_seats = copy.deepcopy(seats)

    while True:
        new_seats = _run_simulation(seats)
        if seats == new_seats:
            break
        seats = copy.deepcopy(new_seats)

    seats_flat = [seat for row in seats for seat in row]
    print(f"There are {seats_flat.count('#')} occupied seats in part 1")

    # Part 2
    seats = orig_seats
    while True:
        new_seats = _run_simulation_2(seats)
        if seats == new_seats:
            break
        seats = copy.deepcopy(new_seats)

    seats_flat = [seat for row in seats for seat in row]
    print(f"There are {seats_flat.count('#')} occupied seats in part 2")


def _run_simulation(seats):
    new_seats = [["error" for _ in row] for row in seats]
    height = len(seats)
    width = len(seats[0])

    for i, row in enumerate(seats):
        for j, s_type in enumerate(row):
            neighbors = [
                seats[i + x_diff][j + y_diff]
                for x_diff in range(-1, 2)
                for y_diff in range(-1, 2)
                if 0 <= i + x_diff < height
                and 0 <= j + y_diff < width
                and (x_diff, y_diff) != (0, 0)
            ]
            if s_type == "error":
                raise Exception("Invalid seat type!")
            elif s_type == "L" and neighbors.count("#") == 0:
                new_seats[i][j] = "#"
            elif s_type == "#" and neighbors.count("#") > 3:
                new_seats[i][j] = "L"
            else:
                new_seats[i][j] = seats[i][j]
    return new_seats


def _run_simulation_2(seats):
    new_seats = [["error" for _ in row] for row in seats]
    height = len(seats)
    width = len(seats[0])

    for i, row in enumerate(seats):
        for j, s_type in enumerate(row):
            n_occupied = 0
            for x_diff in range(-1, 2):
                for y_diff in range(-1, 2):
                    if (x_diff, y_diff) == (0, 0):
                        continue
                    x = i + x_diff
                    y = j + y_diff
                    while 0 <= x < height and 0 <= y < width and seats[x][y] == ".":
                        x += x_diff
                        y += y_diff
                    if 0 <= x < height and 0 <= y < width and seats[x][y] == "#":
                        n_occupied += 1
            if s_type == "error":
                raise Exception("Invalid seat type!")
            if s_type == "L" and n_occupied == 0:
                new_seats[i][j] = "#"
            elif s_type == "#" and n_occupied > 4:
                new_seats[i][j] = "L"
            else:
                new_seats[i][j] = seats[i][j]
    return new_seats


if __name__ == "__main__":
    seating_system()