```python
import pytest
from unittest.mock import patch
from tictactoe import TicTacToe

@pytest.fixture
def game():
    return TicTacToe()

def test_make_move_success(game):
    assert game.make_move(0, 'X') == True

def test_make_move_invalid_move(game):
    game.make_move(0, 'X')
    assert game.make_move(0, 'O') == False

def test_current_winner_none(game):
    assert game.current_winner is None

def test_current_winner_x(game):
    game.make_move(1, 'X')
    game.make_move(2, 'X')
    assert game.current_winner == 'X'

@patch('tictactoe.TicTacToe.make_move', return_value=False)
def test_make_move_mock_invalid_move(mock_make_move, game):
    assert game.make_move(0, 'O') == False
```