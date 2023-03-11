from life.board import BoardFactory
from life.world import World


def test_play(gliter_pattern):
    board = (
        BoardFactory()
        .set_height(10)
        .set_width(10)
        .add_pattern(gliter_pattern)
        .build_board()
    )

    world = World().set_board(board)
    print(world._board)

    world.play()

    print(world._board)

    assert False, "debug time"
