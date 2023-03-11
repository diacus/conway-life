from .models import Cell, CellStatus


class CellPatternParser:
    def set_position(self, x, y):
        self._x = x
        self._y = y

        return self

    def set_pattern(self, raw_pattern: list[str]):
        self._raw_pattern = raw_pattern

        return self

    def parse_cell_pattern(self):
        cells = []
        for row_number, pattern_row in enumerate(self._raw_pattern):
            cell_row = self._parse_row(row_number, pattern_row)
            cells.extend(cell_row)

        return cells

    def _parse_row(self, cell_row, pattern_row):
        cells = []
        for cell_column, cell_value in enumerate(pattern_row):
            if not cell_value.isspace():
                x = self._x + cell_row
                y = self._y + cell_column
                cell = Cell(status=CellStatus.alive, x=x, y=y)
                cells.append(cell)

        return cells
