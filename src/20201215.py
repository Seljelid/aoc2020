from collections import defaultdict

with open("data/20201215.txt") as f:
    line = f.readline()


def dont_speak():
    starting_numbers = line.strip().split(",")
    starting_numbers = [int(number) for number in starting_numbers]

    spoken_numbers = []
    for i in range(2020 - len(starting_numbers)):
        while len(starting_numbers):
            number_spoken = starting_numbers.pop(0)
            spoken_numbers.append(number_spoken)

        last_spoken = spoken_numbers[-1]
        if spoken_numbers.count(last_spoken) == 1:
            number_spoken = 0
            spoken_numbers.append(number_spoken)
        else:
            indices = [i for i, x in enumerate(spoken_numbers) if x == last_spoken]
            number_spoken = indices[-1] - indices[-2]
            spoken_numbers.append(number_spoken)

    print(f"The 2020th number spoken is {spoken_numbers[-1]}")


def no_doubt():
    numbers = line.strip().split(",")
    numbers = [int(number) for number in numbers]
    spoken_at = defaultdict(list)
    for idx, number in enumerate(numbers):
        spoken_at[number].append(idx)

    while len(numbers) < 30000000:
        last_spoken = numbers[-1]
        said_at = spoken_at[last_spoken]
        if len(said_at) < 2:
            numbers.append(0)
        else:
            age = spoken_at[last_spoken][-1] - spoken_at[last_spoken][-2]
            numbers.append(age)

        spoken_at[numbers[-1]].append(len(numbers) - 1)

    print(f"The number is: {numbers[-1]}")


if __name__ == "__main__":
    dont_speak()
    no_doubt()
