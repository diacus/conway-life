from tools import  time_it
from .models import CellStatus, Cell, Board, Point

class BoardFactory:
    def __init__(self):
        self.size = Point(row=0, col=0)
        self._cells = []

    @time_it
    def build_board(self):
        width, height = self.size.col, self.size.row
        cells = [[CellStatus.dead] * width] * height
        new_board = Board(size=self.size)
        new_board.extend(cells)

        if self._cells:
            for cell in self._cells:
                new_board[cell.position.row % height][cell.position.col % width] = cell.status

        return new_board

    def add_pattern(self, pattern: list[Cell]):
        self._cells.extend(pattern)

        return self

    def set_size(self, size: Point):
        self.size = size

        return self
