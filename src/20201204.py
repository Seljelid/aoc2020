import pandas as pd
import re


def validate_passports():
    fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
    file = open("data/20201204.txt")
    lines = file.readlines()
    passports = []
    passport = ""
    for idx, line in enumerate(lines):
        if not line.isspace():
            passport += line
        else:
            passports.append(passport)
            passport = ""
        if idx == len(lines) - 1:
            passports.append(passport)

    passport_list = []
    for passport in passports:
        psp = {}
        for field in fields:
            matches = re.findall(f"(?<={field}:).*?(?=\s)", passport)
            psp[field] = matches[0] if len(matches) else None
        passport_list.append(psp)

    df = pd.DataFrame(passport_list)
    df = df.drop(columns=["cid"])  # This field is not required
    valid_passports = df.dropna()
    print(f"There are {len(valid_passports)} valid passports.")


if __name__ == "__main__":
    validate_passports()