import pandas as pd


def game_stop():
    df = pd.read_csv(
        "data/20201208.txt", header=None, names=["operation", "arg"], sep=" "
    )
    df["order"] = pd.Series(dtype="int")

    def _run_program(df: pd.DataFrame()):
        last_visited = []
        stop = False
        idx = 0
        acc = 0
        terminated_correctly = False
        while not stop:
            if idx in last_visited:
                stop = True
                terminated_correctly = False
            elif idx == len(df):
                print("Program terminated!!")
                stop = True
                terminated_correctly = True
            else:
                if df.loc[idx].operation == "nop":
                    last_visited.append(idx)
                    idx += 1
                elif df.loc[idx].operation == "acc":
                    last_visited.append(idx)
                    acc += df.loc[idx].arg
                    idx += 1
                elif df.loc[idx].operation == "jmp":
                    last_visited.append(idx)
                    idx += df.loc[idx].arg
        return acc, terminated_correctly

    acc, _ = _run_program(df)
    print(f"The acc value is {acc}")

    # Part 2
    jmp_df = df[df.operation == "jmp"].reset_index()
    nop_df = df[df.operation == "nop"].reset_index()
    switch_df = jmp_df.append(nop_df)[["index", "operation"]].reset_index()
    s_idx = 0
    terminated_correctly = False
    while not terminated_correctly:
        new_df = df.copy(deep=True)
        new_df.at[switch_df.iloc[s_idx]["index"], "operation"] = (
            "nop" if switch_df.at[s_idx, "operation"] == "jmp" else "jmp"
        )
        acc, terminated_correctly = _run_program(new_df)
        s_idx += 1

    print(f"The acc value for part 2 is {acc}")


if __name__ == "__main__":
    game_stop()