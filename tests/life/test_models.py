import pytest

from life.models import Board, BoardRow, CellStatus


class TestBoardRow:
    def test_only_appends_cell_status_values(self):
        row = BoardRow()
        with pytest.raises(TypeError):
            row.append("any value")

    def test_only_inserts_cell_status_values(self):
        row = BoardRow([CellStatus.alive])
        with pytest.raises(TypeError):
            row[0] = "any value"

    def test_is_printable(self):
        row = BoardRow([CellStatus.dead, CellStatus.alive, CellStatus.dead])

        assert "░█░" == str(row)

    def test_override_existing_value(self):
        row = BoardRow([CellStatus.dead] * 3)
        row[1] = CellStatus.alive

        assert "░█░" == str(row)


class TestBoard:
    def test_load_board(self):
        expected_board = "\n".join(["░░░░░"] * 3)
        cells = [[CellStatus.dead] * 5] * 3
        board = Board(width=5, height=3)
        board.extend(cells)

        assert  expected_board == str(board)

    def test_read_cell_from_board(self):
        expected_board = "\n".join(["░░░░░"] * 3)
        cells = [[CellStatus.dead] * 5] * 3
        cells[1][3] = CellStatus.alive
        board = Board(width=5, height=3)
        board.extend(cells)

        assert  CellStatus.alive == board[1][3]
