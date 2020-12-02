import pandas as pd


def validate_passwords():
    df = pd.read_csv(
        "data/20201202.txt",
        names=["low", "high", "letter", "pw"],
        sep="-| ",
        engine="python",
    )
    df.letter = df.letter.str.replace(r"\:", "")

    # Part 1
    # df["valid"] = df.apply(
    #     lambda x: (x.pw.count(x.letter) >= x.low) & (x.pw.count(x.letter) <= x.high),
    #     axis=1,
    # )
    # print(df.valid.value_counts())

    # Part 2
    df["valid"] = df.apply(
        lambda x: (x.pw.count(x.letter, x.low - 1, x.low) == 1)
        ^ (x.pw.count(x.letter, x.high - 1, x.high) == 1),
        axis=1,
    )
    print(df.valid.value_counts())


if __name__ == "__main__":
    validate_passwords()
