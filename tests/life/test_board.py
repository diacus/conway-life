from life.board import BoardFactory

def test_board_factory_injects_predefined_pattern(gliter_pattern):
    board = (
        BoardFactory()
        .set_height(10)
        .set_width(10)
        .add_pattern(gliter_pattern)
        .build_board()
    )

    expected_board = "\n".join([
        "░░░░░░░░░░",
        "░░░░░░░░░░",
        "░░░░█░░░░░",
        "░░█░█░░░░░",
        "░░░██░░░░░",
        "░░░░░░░░░░",
        "░░░░░░░░░░",
        "░░░░░░░░░░",
        "░░░░░░░░░░",
        "░░░░░░░░░░",
    ])


    assert expected_board == str(board)
