import pytest
import project

board = project.Board()
board.add_pieces()

def test_roll_dice():
    for _ in range(10):
        assert project.roll_dice() in [0, 1, 2, 3, 4]

def test_change_player():
    assert project.change_player(project.PLAYER_1) == project.PLAYER_2
    assert project.change_player(project.PLAYER_2) == project.PLAYER_1

def test_choose_piece():
    player = project.PLAYER_1
    for i in range(1, 7):
        assert isinstance(project.choose_piece(i, player, board), project.Piece) == True
    player = project.change_player(player)
    for i in range(1, 7):
        assert isinstance(project.choose_piece(i, player, board), project.Piece) == True
    for i in range(8, 10):
        with pytest.raises(KeyError):
            isinstance(project.choose_piece(i, player, board), project.Piece)
    player = project.change_player(player)
    for i in range(8, 10):
        with pytest.raises(KeyError):
            isinstance(project.choose_piece(i, player, board), project.Piece)


def test_can_move():
    assert project.can_move(15, project.PLAYER_1, board) == True
    assert project.can_move(16, project.PLAYER_1, board) == False
    assert project.can_move(15, project.PLAYER_2, board) == True
    assert project.can_move(16, project.PLAYER_2, board) == False

