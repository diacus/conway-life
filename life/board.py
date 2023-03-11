from .models import CellStatus, Cell, Board

class BoardFactory:
    def __init__(self):
        self._width = 0
        self._height = 0
        self._cells = []

    def build_board(self):
        cells = [[CellStatus.dead] * self._width] * self._height
        new_board = Board(width=self._width, height=self._height)
        new_board.extend(cells)

        if self._cells:
            for cell in self._cells:
                new_board[cell.x][cell.y] = cell.status

        return new_board

    def add_pattern(self, pattern: list[Cell]):
        self._cells.extend(pattern)

        return self

    def set_width(self, width: int):
        self._width = width

        return self

    def set_height(self, height: int):
        self._height = height

        return self
