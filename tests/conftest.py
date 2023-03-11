import pytest

from life.board import BoardFactory
from life.patterns import CellPatternParser


@pytest.fixture
def gliter_pattern():
    pattern = [
        "  █",
        "█ █",
        " ██"
    ]

    return (
        CellPatternParser()
        .set_pattern(pattern)
        .set_position(2, 2)
        .parse_cell_pattern()
    )


@pytest.fixture
def simple_board(gliter_pattern):
    return (
        BoardFactory()
        .set_width(10)
        .set_height(10)
        .build_board()
    )
