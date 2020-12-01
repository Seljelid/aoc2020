import pandas as pd
import numpy as np


def add_to_2020():
    with open("data/20201201.json") as f:
        data = pd.read_json(f)

    # data["missing"] = 2020 - data["data"]
    # df = data.loc[data["missing"].isin(data["data"])]
    # df["result"] = df["data"] * df["missing"]

    triplet = find_triplet(data.data, 2020)
    product = np.prod(triplet)
    print(product)


def find_triplet(series, sum):
    for i in range(0, len(series) - 1):
        s = set()
        current_sum = sum - series.iloc[i]
        for j in range(i + 1, len(series)):
            if current_sum - series.iloc[j] in s:
                triplet = [series.iloc[i], series.iloc[j], current_sum - series.iloc[j]]
                print(
                    "Triplet is:",
                    series.iloc[i],
                    series.iloc[j],
                    current_sum - series.iloc[j],
                )
                return triplet
            s.add(series.iloc[j])


if __name__ == "__main__":
    add_to_2020()