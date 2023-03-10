import pdb
import random
from itertools import product
from functools import partial
from collections import defaultdict
from copy import deepcopy

from .models import CellState, Board


class World:
    def __init__(self):
        self._board = None
        self._deltas = [vector for vector in product([-1, 0, 1], [-1, 0, 1]) if not vector == (0, 0)]

    def __str__(self):
        cells = deepcopy(self._board).cells
        lines = []
        while cells:
            line, cells = cells[:self._board.width], cells[self._board.width:]
            lines.append("".join(map(str, line)))

        return "\n".join(lines)

    def has_life(self):
        cells_alive = [cell for cell in self._board.cells if cell == CellState.alive]
        return len(cells_alive) > 0

    def set_board(self, board: list[CellState]):
        self._board = board

        return self

    def play(self):
        pdb.set_trace()
        new_cells = [
            self._get_next_cell_value(index, cell)
            for index, cell in enumerate(self._board.cells)
        ]

        new_board = Board(cells=new_cells, width=self._board.width, height=self._board.height)
        self._board = new_board

        return self

    def _get_next_cell_value(self, index, cell):
        neighbors = self._get_neighbors(index)

        if cell == CellState.dead:
            return CellState.alive if neighbors[CellState.alive] == 3 else CellState.dead

        if neighbors[CellState.alive] > 3:
            return CellState.dead

        if neighbors[CellState.alive] < 2:
            return CellState.dead

        return CellState.alive

    def _get_neighbors(self, cell_number) -> list[bool]:
        cell_coordinates = self._get_coordinates(cell_number)
        move_from_cell = partial(self._get_vector_sum, cell_coordinates)
        neighborhood = map(move_from_cell, self._deltas)

        neighbors = defaultdict(lambda: 0)

        for value in map(self._get_value_at_coordinate, neighborhood):
            neighbors[value] += 1

        return neighbors

    def _get_coordinates(self, cell_number: int) -> (int, int):
        xpos = cell_number % self._board.height
        ypos = int(cell_number / self._board.width)

        return xpos, ypos

    def _get_vector_sum(self, a: (int, int), b: (int, int)) -> (int, int):
        x1, y1 = a
        x2, y2 = b

        x = (x1 + x2) % self._board.width
        y = (y1 + y2) % self._board.height

        return x, y

    def _get_value_at_coordinate(self, coordinate):
        x, y = coordinate
        index = self._board.width * y + x

        return self._board.cells[index]
