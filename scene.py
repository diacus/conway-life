import json

from pathlib import Path

from life.models import Point
from life.patterns import CellPatternParser
from life.board import BoardFactory
from life.world import World


def load_scene_by_name(scene_name):
    scene_path = Path(__file__).parent / "var" / f"{scene_name}.json"

    with open(scene_path) as stream:
        raw_scene = json.load(stream)

    scene_size = Point(row=raw_scene["size"]["height"], col=raw_scene["size"]["width"])

    board_factory = BoardFactory().set_size(scene_size)

    for settings in raw_scene["configuration"]:
        position = Point(row=settings["location"]["y"], col=settings["location"]["x"])
        pattern_name = settings["pattern"]
        raw_pattern = raw_scene["patterns"][pattern_name]

        pattern = (
            CellPatternParser()
            .set_position(position)
            .set_pattern(raw_pattern)
            .parse_cell_pattern()
        )
        board_factory.add_pattern(pattern)


    board = board_factory.build_board()

    world = World().set_board(board)

    return world
