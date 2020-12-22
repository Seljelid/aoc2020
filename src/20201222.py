from collections import deque
from itertools import islice


def crab_combat():
    with open("data/20201222.txt") as f:
        lines = f.readlines()

    cards = [
        line.strip()
        for line in lines
        if not (line.startswith("Player") or line.isspace())
    ]
    player_1, player_2 = deque(cards[0 : len(cards) // 2]), deque(
        cards[len(cards) // 2 :]
    )

    player_1, player_2 = _play_game(player_1, player_2)
    winner = player_1 if player_1 else player_2
    winner.reverse()
    winning_score = 0
    for i, card in enumerate(winner):
        winning_score += (i + 1) * int(card)
    print(f"The winning score is: {winning_score}")

    # Part 2
    player_1, player_2 = deque(cards[0 : len(cards) // 2]), deque(
        cards[len(cards) // 2 :]
    )

    player_1, player_2 = _play_game(player_1, player_2, True)
    winner = player_1 if player_1 else player_2
    winner.reverse()
    winning_score = 0
    for i, card in enumerate(winner):
        winning_score += (i + 1) * int(card)
    print(f"The winning score is: {winning_score}")


def _play_game(player_1, player_2, recursive=False):
    prev = set()
    p1, p2 = player_1, player_2
    while p1 and p2:
        if (tuple(p1), tuple(p2)) in prev:
            return p1, p2
        else:
            prev.add((tuple(p1), tuple(p2)))

        if _p1_wins(p1, p2, recursive):
            p1.append(p1.popleft())
            p1.append(p2.popleft())
        else:
            p2.append(p2.popleft())
            p2.append(p1.popleft())

    return p1, p2


def _p1_wins(p1, p2, recursive=False) -> bool:
    cards = (int(p1[0]), int(p2[0]))
    if recursive and cards[0] < len(p1) and cards[1] < len(p2):
        p1, p2 = _play_game(
            deque(islice(p1, 1, cards[0] + 1)),
            deque(islice(p2, 1, cards[1] + 1)),
            recursive,
        )
        return bool(p1)
    else:
        return cards[0] > cards[1]


if __name__ == "__main__":
    crab_combat()