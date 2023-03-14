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

from gui.scene import Scene as GuiScene

app = typer.Typer()


@app.command()
def play(scene_name: str):
    world = load_scene_by_name(scene_name)
    scene = GuiScene()
    try:
        while world.has_life() and not scene.should_quit:
            os.system("clear")
            scene.draw(world.board)
            world = world.play()

        print("there is no live now")

    except KeyboardInterrupt:
        print("bye")

    return 0


if __name__ == "__main__":
    app()
