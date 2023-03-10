from enum import Enum

from pydantic import BaseModel


class CellState(Enum):
    alive = "alive"
    dead = "dead"

    def __str__(self):
        if self == CellState.alive:
            return "█"

        return "░"


class Cell(BaseModel):
    state: CellState
    x: int
    y: int


class Board(BaseModel):
    cells: list[CellState]
    width: int
    height: int
