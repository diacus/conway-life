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
from scene import load_scene_by_name

app = typer.Typer()


@app.command()
def play():
    world = load_scene_by_name("space-ships")
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
