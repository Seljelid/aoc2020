import numpy as np


def jurassic_jigsaw():
    tiles = {}
    with open("data/20201220.txt") as f:
        lines = f.read().strip()
        images = lines.split("\n\n")
        for image in images:
            image_lines = image.split("\n")
            image = image_lines[1:]
            id = int(image_lines[0][5:-1])
            tiles[id] = image

    borders = {id: _get_borders_from_tile(tiles[id]) for id in tiles}
    n_shared = _get_n_shared_entries(borders, tiles)
    corner_tiles = [id for id in tiles if n_shared[id] == 2]

    print(f"Corner tile ids multiplied: {np.prod(corner_tiles)}")


def _get_n_shared_entries(borders, tiles):
    n_shared = {
        id_1: sum(
            [
                len([i for j in borders[id_2] for i in borders[id_1] if i == j])
                for id_2 in tiles
                if id_2 != id_1
            ]
        )
        / 2
        for id_1 in borders
    }
    return n_shared


def _get_borders_from_tile(tile):
    borders = [
        tile[0],
        tile[-1],
        "".join(line[0] for line in tile),
        "".join(line[-1] for line in tile),
    ]
    borders = borders + [b[::-1] for b in borders]
    return borders


if __name__ == "__main__":
    jurassic_jigsaw()