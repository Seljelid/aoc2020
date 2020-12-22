import itertools
import re


def monster_messages():
    with open("data/20201219.txt") as f:
        lines = f.readlines()
    rules = {}
    messages = []
    for line in lines:
        if ":" in line:
            rule = line.split(": ")
            rules[int(rule[0])] = rule[1].strip()
        elif not line.isspace():
            messages.append(line.strip())

    rule_to_obey = 0
    valid_messages = set(_unravel_rule(rule_to_obey, rules))
    n_valid = sum(message in valid_messages for message in messages)
    print(f"There are {n_valid} valid messages")

    # Part 2
    rules[8] = "42 | 42 8"
    rules[11] = "42 31 | 42 11 31"
    r_42 = set(_unravel_rule(42, rules))
    r_31 = set(_unravel_rule(31, rules))
    l_r42 = [len(pattern) for pattern in r_42]
    l_r31 = [len(pattern) for pattern in r_31]
    chunk_l = min(l_r42 + l_r31)  # All are the same (8)

    agg = 0
    for message in messages:
        message_l = len(message)
        if message_l % chunk_l == 0:  # Can't be a match otherwise
            chunk_in_r42 = [
                message[i : i + chunk_l] in r_42 for i in range(0, message_l, chunk_l)
            ]
            chunk_in_r31 = [
                message[i : i + chunk_l] in r_31 for i in range(0, message_l, chunk_l)
            ]
            is_match = any(
                all(chunk_in_r42[:i])
                and all(chunk_in_r31[i:])
                and i > (len(chunk_in_r42) - i)
                for i in range(len(chunk_in_r42))
            )
            if is_match:
                agg += 1

    print(f"There are {agg} valid messages")


def _unravel_rule(rule_num: int, rules: dict):
    if '"' in rules[rule_num]:
        yield rules[rule_num][1:-1]
    else:
        for rule in rules[rule_num].split(" | "):
            for perm in itertools.product(
                *[_unravel_rule(int(r), rules) for r in rule.split()]
            ):
                yield "".join(perm)


if __name__ == "__main__":
    monster_messages()
