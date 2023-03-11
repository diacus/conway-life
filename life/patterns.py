from .models import Cell, CellStatus, Point


class CellPatternParser:
    def set_position(self, position: Point):
        self.position = position

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
        for cell_col, cell_value in enumerate(pattern_row):
            if not cell_value.isspace():
                cell_pos = Point(row=cell_row, col=cell_col)
                cell = Cell(status=CellStatus.alive, position=self.position + cell_pos)
                cells.append(cell)

        return cells
