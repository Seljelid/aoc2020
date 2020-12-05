import pandas as pd


def boarding_passes():
    file = open("data/20201205.txt")
    lines = file.readlines()
    rows = []
    columns = []
    for line in lines:
        rows.append(line[0:7])
        columns.append(line[7:-1])

    row_nums = []
    for row in rows:
        row_num = _get_row_num(row)
        row_nums.append(row_num)

    col_nums = []
    for col in columns:
        col_num = _get_col_num(col)
        col_nums.append(col_num)

    bdp = pd.DataFrame()
    bdp["row"] = row_nums
    bdp["col"] = col_nums
    bdp["seat_id"] = bdp.row * 8 + bdp.col
    print(f"Highest seat id is: {bdp.seat_id.max()}")

    # Part 2
    # Drop first and last row
    bdp = bdp.drop(bdp[bdp.row == bdp.row.max()].index)
    bdp = bdp.drop(bdp[bdp.row == bdp.row.min()].index)

    df = bdp.groupby("row").count()
    my_row_num = df[df.col != 8].index[0]
    taken_cols = bdp[bdp.row == my_row_num].col
    available_cols = list(range(0, 8))
    my_col_num = list(set(available_cols) - set(taken_cols))[0]
    my_seat_id = my_row_num * 8 + my_col_num
    print(f"My seat id is: {my_seat_id}")


def _get_row_num(code: str):
    row_range = list(range(0, 128))
    for char in code:
        if char == "F":
            row_range = row_range[: len(row_range) // 2]
        else:
            row_range = row_range[len(row_range) // 2 :]
    return row_range[0]


def _get_col_num(code: str):
    col_range = list(range(0, 8))
    for char in code:
        if char == "L":
            col_range = col_range[: len(col_range) // 2]
        else:
            col_range = col_range[len(col_range) // 2 :]
    return col_range[0]


if __name__ == "__main__":
    boarding_passes()