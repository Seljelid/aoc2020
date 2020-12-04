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
    print(f"There are {len(valid_passports)} valid passports in part 1.")

    # Part 2

    # Only keep passports which have valid byr
    valid_passports["valid"] = valid_passports.apply(
        lambda x: True if (int(x.byr) >= 1920 and int(x.byr) <= 2003) else False, axis=1
    )
    valid_passports = valid_passports[valid_passports.valid == True]

    # Only keep passports which have valid iyr
    valid_passports["valid"] = valid_passports.apply(
        lambda x: True if (int(x.iyr) >= 2010 and int(x.iyr) <= 2020) else False, axis=1
    )
    valid_passports = valid_passports[valid_passports.valid == True]

    # Only keep passports which have valid eyr
    valid_passports["valid"] = valid_passports.apply(
        lambda x: True if (int(x.eyr) >= 2020 and int(x.eyr) <= 2030) else False, axis=1
    )
    valid_passports = valid_passports[valid_passports.valid == True]

    # Only keep valid ecl
    colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    valid_passports["valid"] = valid_passports.apply(lambda x: x.ecl in colors, axis=1)
    valid_passports = valid_passports[valid_passports.valid == True]

    # Only keep valid hgt
    valid_passports["tmp_hgt"] = valid_passports.apply(
        lambda x: int(re.findall("(\d+)", x.hgt)[0]), axis=1
    )
    valid_passports["hgt_unit"] = valid_passports.apply(
        lambda x: re.split("(\d+)", x.hgt)[2], axis=1
    )
    valid_passports["valid"] = valid_passports.apply(
        lambda x: True
        if (
            (x.tmp_hgt >= 150 and x.tmp_hgt <= 193 and x.hgt_unit == "cm")
            or (x.tmp_hgt >= 59 and x.tmp_hgt <= 76 and x.hgt_unit == "in")
        )
        else False,
        axis=1,
    )
    valid_passports = valid_passports[valid_passports.valid == True]

    # Only keep valid hcl
    valid_passports["valid"] = valid_passports.apply(
        lambda x: True if x.hcl.startswith("#") else False, axis=1
    )
    valid_passports = valid_passports[valid_passports.valid == True]

    valid_passports["tmp_hcl"] = valid_passports.apply(
        lambda x: re.split("(#)", x.hcl)[2], axis=1
    )
    allowed_chars = {
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
    }
    valid_passports["valid"] = valid_passports.apply(
        lambda x: True
        if (len(x.tmp_hcl) == 6 and allowed_chars.issuperset(x.tmp_hcl))
        else False,
        axis=1,
    )
    valid_passports = valid_passports[valid_passports.valid == True]

    # Only keep valid pid
    valid_passports["valid"] = valid_passports.apply(
        lambda x: True if (len(x.pid) == 9 and x.pid.isnumeric()) else False, axis=1
    )
    valid_passports = valid_passports[valid_passports.valid == True]

    print(f"There are {len(valid_passports)} valid passports in part 2.")


if __name__ == "__main__":
    validate_passports()