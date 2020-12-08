from collections import Counter


def bags():
    file = open("data/20201207.txt")
    lines = file.readlines()
    bags = {}
    for line in lines:
        line = line.strip()
        main_parts = line.split("contain")
        outer = main_parts[0].split("bags")[0].strip()
        contents = main_parts[1][:-1].split(",")
        contents = [content.strip() for content in contents]
        try:
            content_dict = {
                content[1:].split("bag")[0].strip(): int(content[0])
                for content in contents
            }
        except:
            content_dict = {}
        bags[outer] = content_dict

    def _extract_bags(bag: dict, current_collection: dict) -> dict:
        next_level = [Counter(bags[k]) for k in bag.keys()]
        next_bag = Counter()
        for elem, multiplier in zip(next_level, bag.values()):
            for k in elem.keys():
                elem[k] = elem[k] * multiplier
            next_bag += elem

        if bool(next_bag):
            current_collection = dict(Counter(current_collection) + next_bag)
            return _extract_bags(next_bag, current_collection)
        else:
            return current_collection

    bag_dict = {}
    for outer_bag in bags.keys():
        inner_bags = _extract_bags(bags[outer_bag], bags[outer_bag])
        bag_dict[outer_bag] = inner_bags

    counter = 0
    for contents in bag_dict.values():
        if "shiny gold" in contents:
            counter += 1
    print(f"There can be shiny golden bags in {counter} bag types")

    bags_inside_golden = sum(bag_dict["shiny gold"].values())
    print(f"A shiny golden bag contains {bags_inside_golden} other bags")


if __name__ == "__main__":
    bags()