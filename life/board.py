from .models import CellState, Cell, Board

class BoardFactory:
    def __init__(self):
        self._width = 0
        self._height = 0
        self._size = 0
        self._cells = []

    def build_board(self):
        cells = [CellState.dead] * self._size

        for cell in self._cells:
            index = (cell.y % self._height) * self._width + (cell.x % self._width)
            cells[index] = CellState.alive

        return Board(cells=cells, width=self._width, height=self._height)

    def add_pattern(self, pattern: list[Cell]):
        self._cells.extend(pattern)

        return self

    def set_width(self, width: int):
        self._width = width
        self._size = self._width * self._height

        return self

    def set_height(self, height: int):
        self._height = height
        self._size = self._width * self._height

        return self
