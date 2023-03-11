import json
import os
import random
from time import sleep
from pathlib import Path

import typer
from rich import print

from life.world import World
from life.patterns import CellPatternParser
from life.board import BoardFactory


app = typer.Typer()

def load_patterns():
    pwd = Path(__file__).parent

    with open(pwd / "var" / "patterns.json") as stream:
        patterns = json.load(stream)

    return patterns


@app.command()
def play(width: int = 80, height: int = 25):
    patterns = load_patterns()
    glider_pattern = patterns["glider"]

    pattern_1 = (
        CellPatternParser()
        .set_position(glider_pattern["location"]["x"], glider_pattern["location"]["y"])
        .set_pattern(glider_pattern["pattern"])
        .parse_cell_pattern()
    )

    pattern_2 = (
        CellPatternParser()
        .set_position(10, 4)
        .set_pattern(glider_pattern["pattern"])
        .parse_cell_pattern()
    )

    board = (
        BoardFactory()
        .set_width(width)
        .set_height(height)
        .add_pattern(pattern_1)
        .add_pattern(pattern_2)
        .build_board()
    )

    world = World().set_board(board)
    try:
        while world.has_life():
            os.system("clear")
            print(world)
            world = world.play()
            sleep(0.15)

        print("there is no live now")

    except KeyboardInterrupt:
        print("bye")

    return 0


if __name__ == "__main__":
    app()
