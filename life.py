import random
from itertools import product
from functools import partial
from collections import defaultdict
from copy import deepcopy

from enum import Enum


class Cell(Enum):
    alive = "alive"
    dead = "dead"

    def __str__(self):
        if self == Cell.alive:
            return "█"

        return "░"



class World:
    def __init__(self):
        self._width = 0
        self._height = 0
        self._size = 0
        self._population = 0
        self._board = []
        self._deltas = [vector for vector in product([-1, 0, 1], [-1, 0, 1]) if not vector == (0, 0)]

    def __str__(self):
        board = deepcopy(self._board)
        lines = []
        while board:
            line, board = board[:self._width], board[self._width:]
            lines.append("".join(map(str, line)))

        return "\n".join(lines)

    def has_life(self):
        cells_alive = [cell for cell in self._board if cell == Cell.alive]
        return len(cells_alive) > 0

    def set_population(self, population: int):
        self._population = population

        return self

    def set_width(self, width: int):
        self._width = width
        self._size = self._width * self._height

        return self

    def set_height(self, height: int):
        self._height = height
        self._size = self._width * self._height

        return self

    def set_board(self, board: list[Cell]):
        self._board = board

        return self

    def generate_board(self):
        self._board = [Cell.dead] * self._size
        seeds = random.sample(range(self._size), self._population)

        for seed in seeds:
            self._board[seed] = Cell.alive

        return self

    def generate_next_board_configuration(self):
        new_board = [
            self._get_next_cell_value(index, cell)
            for index, cell in enumerate(self._board)
        ]

        self._board = new_board

        return self

    def _get_next_cell_value(self, index, cell):
        neighbors = self._get_neighbors(index)

        if cell == Cell.dead:
            return Cell.alive if neighbors[Cell.alive] == 3 else Cell.dead

        if neighbors[Cell.alive] > 3:
            return Cell.dead

        if neighbors[Cell.alive] < 2:
            return Cell.dead

        return Cell.alive

    def _get_neighbors(self, cell_number) -> list[bool]:
        cell_coordinates = self._get_coordinates(cell_number)
        move_from_cell = partial(self._get_vector_sum, cell_coordinates)
        neighborhood = map(move_from_cell, self._deltas)

        neighbors = defaultdict(lambda: 0)

        for value in map(self._get_value_at_coordinate, neighborhood):
            neighbors[value] += 1

        return neighbors

    def _get_coordinates(self, cell_number: int) -> (int, int):
        xpos = cell_number % self._height
        ypos = int(cell_number / self._width)

        return xpos, ypos

    def _get_vector_sum(self, a: (int, int), b: (int, int)) -> (int, int):
        x1, y1 = a
        x2, y2 = b

        x = (x1 + x2) % self._width
        y = (y1 + y2) % self._height

        return x, y

    def _get_value_at_coordinate(self, coordinate):
        x, y = coordinate
        index = self._width * y + x

        return self._board[index]
