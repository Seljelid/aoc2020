from collections import deque
from itertools import islice
import copy


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

    winner = _play_game(player_1, player_2)
    winning_score = 0
    for i, card in enumerate(winner):
        winning_score += (i + 1) * int(card)
    print(f"The winning score is: {winning_score}")

    # Part 2
    player_1, player_2 = deque(cards[0 : len(cards) // 2]), deque(
        cards[len(cards) // 2 :]
    )
    winner = _play_game(player_1, player_2, True)
    winning_score = 0
    for i, card in enumerate(winner):
        winning_score += (i + 1) * int(card)
    print(f"The winning score is: {winning_score}")


def _play_game(player_1: list, player_2: list, recursive: bool = False):
    prev_1 = []
    prev_2 = []
    while player_1 and player_2:
        cards = (player_1[0], player_2[0])
        if recursive:
            if "".join(list(player_1)) in prev_1 and "".join(list(player_2)) in prev_2:
                win_1 = True
            else:
                prev_1.append("".join(list(player_1)))
                prev_2.append("".join(list(player_2)))
                p1 = copy.deepcopy(player_1)
                p2 = copy.deepcopy(player_2)
                if len(p1) - 1 >= int(cards[0]) and len(p2) - 1 >= int(cards[1]):
                    p1 = deque(islice(p1, 1, int(cards[0]) + 1))
                    p2 = deque(islice(p2, 1, int(cards[1]) + 1))
                    while p1 and p2:
                        p1, p2 = _high_card_wins(p1, p2)
                    win_1 = bool(p1)
                else:
                    win_1 = int(cards[0]) > int(cards[1])
            if win_1:
                player_1.append(player_1.popleft())
                player_1.append(player_2.popleft())
            else:
                player_2.append(player_2.popleft())
                player_2.append(player_1.popleft())
        else:
            player_1, player_2 = _high_card_wins(player_1, player_2)

    winner = player_1 if player_1 else player_2
    winner.reverse()
    return winner


def _high_card_wins(p1, p2):
    c = (int(p1[0]), int(p2[0]))
    if c[0] > c[1]:
        p1.append(p1.popleft())
        p1.append(p2.popleft())
    elif c[1] > c[0]:
        p2.append(p2.popleft())
        p2.append(p1.popleft())

    return p1, p2


if __name__ == "__main__":
    crab_combat()