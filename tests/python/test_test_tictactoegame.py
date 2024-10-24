```python
import pytest
from unittest.mock import patch
from tic_tac_toe import TicTacToe

@pytest.fixture
def new_game():
    return TicTacToe()

def test_validate_move():
    game = new_game()
    assert game.validate_move(-1) == (False, "Move must be between 0 and 8")
    assert game.validate_move(5) == (True, "Valid move")
    game.board[6] = 'X'
    assert game.validate_move(6) == (False, "Square already occupied")

def test_make_move():
    game = new_game()
    assert game.make_move(4) == (True, "Move successful")
    assert game.make_move(4) == (False, "Square already occupied")
    assert game.make_move(-1) == (False, "Move must be between 0 and 8")

def test_undo_move():
    game = new_game()
    game.make_move(4)
    assert game.undo_move() == (True, "Move undone. It's X's turn again.")
    assert game.undo_move() == (False, "No moves to undo!")

@patch('random.choice', return_value=0)
def test_suggest_move(mock_choice):
    game = new_game()
    assert game.suggest_move() == "Suggested move for X: 0"

def test_check_winner():
    game = new_game()
    game.board = ['X', 'O', ' ', ' ', 'X', 'O', ' ', ' ', 'X']
    assert game.check_winner(8) == True
    assert game.check_winner(4) == False

def test_available_moves():
    game = new_game()
    game.board = ['X', 'O', ' ', ' ', 'X', 'O', ' ', ' ', 'X']
    assert game.available_moves() == [2, 3, 6, 7]

def test_is_board_full():
    game = new_game()
    game.board = ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
    assert game.is_board_full() == True
    game.board = ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', ' ']
    assert game.is_board_full() == False

def test_reset_game():
    game = new_game()
    game.make_move(4)
    game.reset_game()
    assert game.board == [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    assert game.current_winner == None
    assert game.move_history == []
    assert game.current_player == 'X'

def test_print_scores(capfd):
    game = new_game()
    game.scores = {'X': 2, 'O': 1, 'Draws': 0}
    game.print_scores()
    out, _ = capfd.readouterr()
    assert out == "Scores: X - 2, O - 1, Draws - 0\n"
```