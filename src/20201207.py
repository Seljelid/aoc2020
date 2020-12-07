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

    def _extract_bags(bag: dict, current_collection: dict):
        next_level = [bags[k] for k in bag.keys()]
        next_level = list(filter(None, next_level))
        next_bag = dict((key, k[key]) for k in next_level for key in k)
        if bool(next_bag):
            current_collection.update(next_bag)
            return _extract_bags(next_bag, current_collection)
        else:
            return current_collection

    bag_dict = {}
    for outer_bag in bags.keys():
        inner_bags = _extract_bags(bags[outer_bag], bags[outer_bag])
        bag_dict[outer_bag] = inner_bags

    counter = 0
    for k, v in bag_dict.items():
        if "shiny gold" in v.keys():
            counter += 1
    print(f"There can be shiny golden bags in {counter} bag types")


if __name__ == "__main__":
    bags()