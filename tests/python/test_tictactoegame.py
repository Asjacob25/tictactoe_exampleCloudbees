
import unittest
from tictactoegame import TicTacToe


class TestMain(unittest.TestCase):
    new_game = TicTacToe()

    # def test_initial_board_size(new_game):
    #     assert new_game.board_size == 3

    # def test_print_board(capfd, new_game):
    #     new_game.print_board()
    #     out, _ = capfd.readouterr()
    #     assert '|   |   |   |\n|   |   |   |\n|   |   |   |\n' in out

    # def test_validate_move(new_game):
    #     assert new_game.validate_move(0) == (True, "Valid move")
    #     assert new_game.validate_move(9) == (False, "Move must be between 0 and 8")
    #     new_game.board[1] = 'X'
    #     assert new_game.validate_move(1) == (False, "Square already occupied")

    # def test_make_move(new_game):
    #     assert new_game.make_move(0) == (True, "Move successful")
    #     assert new_game.make_move(0) == (False, "Square already occupied")
    #     assert new_game.make_move(1) == (True, "Player X wins!")

    # def test_undo_move(new_game):
    #     new_game.make_move(0)
    #     assert new_game.undo_move() == (True, "Last move undone")
    #     assert new_game.undo_move() == (False, "No moves to undo")

    # def test_check_winner(new_game):
    #     new_game.board = ['X', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' ']
    #     assert new_game.check_winner(0)
    #     new_game.board = ['O', ' ', ' ', 'O', ' ', ' ', 'O', ' ', ' ']
    #     assert new_game.check_winner(6)
    #     new_game.board = ['O', ' ', 'X', ' ', 'X', ' ', 'X', ' ', 'O']
    #     assert new_game.check_winner(4)

    # def test_available_moves(new_game):
    #     new_game.board = ['X', ' ', 'O', 'O', 'X', ' ', ' ', 'O', 'X']
    #     assert new_game.available_moves() == [1, 5, 6]

    # def test_suggest_move(mock_random_choice, new_game):
    #     assert new_game.suggest_move() == 4

    # def test_is_board_full(new_game):
    #     new_game.board = ['X', 'X', 'O', 'O', 'X', 'X', 'X', 'O', 'O']
    #     assert new_game.is_board_full() == True

    # def test_reset_game(new_game):
    #     new_game.reset_game()
    #     assert new_game.board == [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    # def test_set_symbols(new_game):
    #     new_game.set_symbols('A', 'B')
    #     assert new_game.player_x == 'A'
    #     assert new_game.player_o == 'B'

    # def test_current_player_symbol(new_game):
    #     assert new_game.current_player_symbol() == "The current player is: X"

if __name__ == "__main__":
    unittest.main()