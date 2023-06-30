import random
from itertools import product
from functools import partial
from collections import defaultdict

from tools import time_it

from .models import CellStatus, Board
from .board import BoardFactory


class World:
    def __init__(self):
        self.board = None
        self._deltas = [vector for vector in product([-1, 0, 1], [-1, 0, 1]) if not vector == (0, 0)]

    def __str__(self):
        return str(self.board)

    def has_life(self):
        cells_alive = self.board.get_life_count()
        return cells_alive > 0

    def set_board(self, board: list[CellStatus]):
        self.board = board

        return self

    @time_it
    def play(self):
        new_board = (
            BoardFactory()
            .set_size(self.board.size)
            .build_board()
        )

        for row_number, row in enumerate(self.board):
            for column_number, cell_status in enumerate(row):
                new_cell_status = self._get_next_cell_value(row_number, column_number, cell_status)
                new_board[row_number][column_number] = new_cell_status

        self.board = new_board

        return self

    def _get_next_cell_value(self, row, column, cell):
        neighbors = self._get_neighbors(row, column)

        if cell == CellStatus.dead:
            return CellStatus.alive if neighbors[CellStatus.alive] == 3 else CellStatus.dead

        if neighbors[CellStatus.alive] > 3 or neighbors[CellStatus.alive] < 2:
            return CellStatus.dead

        return CellStatus.alive

    def _get_neighbors(self, row, column) -> list[bool]:
        cell_coordinates = row, column
        move_from_cell = partial(self._get_vector_sum, cell_coordinates)
        neighborhood = map(move_from_cell, self._deltas)

        neighbors = defaultdict(lambda: 0)

        for value in map(self._get_value_at_coordinate, neighborhood):
            neighbors[value] += 1

        return neighbors

    def _get_vector_sum(self, source: (int, int), delta: (int, int)) -> (int, int):
        source_row, source_col = source
        delta_row, delta_col = delta

        size = self.board.size

        row = (source_row + delta_row) % size.row
        col = (source_col + delta_col) % size.col

        return row, col

    def _get_value_at_coordinate(self, coordinate):
        row, col = coordinate
        return self.board[row][col]
