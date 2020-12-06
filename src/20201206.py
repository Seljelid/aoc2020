def customs_control():
    file = open("data/20201206.txt")
    lines = file.readlines()
    groups = []
    group = set()
    for idx, line in enumerate(lines):
        if not line.isspace():
            group = group.union(set(list(line[:-1])))
        else:
            groups.append(group)
            group = set()
        if idx == len(lines) - 1:
            groups.append(group)

    common_count = [len(group) for group in groups]
    print(f"The sum of common answers in: {sum(common_count)} in part 1")

    # Part 2
    groups = []
    group = []
    for idx, line in enumerate(lines):
        if not line.isspace():
            group.append(list(list(line[:-1])))
        else:
            groups.append(group)
            group = []
        if idx == len(lines) - 1:
            groups.append(group)

    common_elements = [list(set.intersection(*map(set, grp))) for grp in groups]
    common_count = [len(common) for common in common_elements]
    print(f"The sum of common answers in: {sum(common_count)} in part 2")


if __name__ == "__main__":
    customs_control()
