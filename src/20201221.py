def allergen_assessment():
    with open("data/20201221.txt") as f:
        lines = f.readlines()

    table_of_contents = []
    mapping = {}
    for line in lines:
        line = line.strip()
        ingredients, allergens = line.split("(contains")
        ingredients = set(ingredients.strip().split())
        allergens = allergens[:-1].strip().split(",")
        allergens = [a.strip() for a in allergens]
        table_of_contents.append((ingredients, allergens))
        for a in allergens:
            if a not in mapping:
                mapping[a] = set(ingredients)
            else:
                mapping[a] &= ingredients

    could_be_allergen = set()
    for ingredient in mapping.values():
        could_be_allergen |= ingredient

    is_not_allergen = []
    for ingredients, _ in table_of_contents:
        for ing in ingredients:
            if ing not in could_be_allergen:
                is_not_allergen.append(ing)

    print(f"{len(is_not_allergen)} ingredients can't contain an allergen")

    # Part 2
    allergen_ingredient = []
    ordered_allergens = sorted(mapping, key=lambda k: len(mapping[k]))
    for allergen in ordered_allergens:
        secured_ingredient = mapping[allergen].pop()
        allergen_ingredient.append((allergen, secured_ingredient))
        for v in mapping.values():
            v.discard(secured_ingredient)

    canonical_list = ",".join(a_i[1] for a_i in sorted(allergen_ingredient))

    print(f"Canonical list: {canonical_list}")


if __name__ == "__main__":
    allergen_assessment()