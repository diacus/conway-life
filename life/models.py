import operator
from enum import Enum
from collections import UserList
from collections.abc import Iterable
from functools import reduce


from pydantic import BaseModel


class CellStatus(Enum):
    alive = "█"
    dead = "░"

    def __str__(self):
        return self.value


class Point(BaseModel):
    row: int
    col: int

    def __add__(self, other):
        return Point(row=self.row + other.row, col=self.col + other.col)


class Cell(BaseModel):
    status: CellStatus
    position: Point


class BoardRow(UserList):
    def __setitem__(self, index: int, item: CellStatus):
        self._validate(item)
        self.data[index] = item

    def __str__(self):
        return "".join(map(str, self.data))

    def __repr__(self):
        as_list = [str(item) for item in self.data]
        return repr(as_list)

    def _validate(self, item: CellStatus):
        if not isinstance(item, CellStatus):
            raise TypeError("expected item to be CellStatus, but got %s", type(item))

    def append(self, item: CellStatus):
        self._validate(item)
        self.data.append(item)

    def extend(self, more_items: Iterable):
        if not isinstance(more_items, Iterable):
            raise TypeError("Trying to extend collection with non iterable argument")

        map(self._validate, more_items)
        self.data.extend(more_items)

    def insert(self, index: int, item: CellStatus):
        self._validate(item)
        self.data.insert(index, item)

    def get_life_count(self):
        alive_cells = map(lambda cell: cell == CellStatus.alive, self.data)
        return len(list(alive_cells))


class Board(UserList):
    def __init__(self, *args, size: Point = Point(row=0, col=0), **kwargs):
        self.size=size
        super().__init__(*args, **kwargs)

    def __setitem__(self, index: int, item: CellStatus):
        self._validate(item)
        self.data[index % self.size.row] = item

    def __str__(self):
        return "\n".join(map(str, self.data))

    def _validate(self, item: BoardRow):
        if not isinstance(item, BoardRow):
            raise TypeError("expected item to be BoardRow, but got %s", type(item))

        size = len(BoardRow)

        if not size == self.width:
            raise ValueError(
                "board row has not the right size, got %d when expected %d",
                size,
                self.width
            )

    def append(self, item: BoardRow):
        self._validate(item)
        self.data.append(item)

    def extend(self, more_items: Iterable[BoardRow]):
        if not isinstance(more_items, Iterable):
            raise TypeError("Trying to extend collection with non iterable argument")

        map(self._validate, more_items)
        self.data.extend(map(BoardRow, more_items))

    def insert(self, index: int, item: CellStatus):
        self._validate(item)
        self.data.insert(index % self.size.col, item)

    def get_life_count(self):
        life_count_per_row = map(lambda row: row.get_life_count(), self.data)
        return reduce(operator.add, life_count_per_row, 0)
