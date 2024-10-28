import random
import json

class TicTacToe:
    def __init__(self, board_size=3):
        self.board_size = board_size
        self.board = [' ' for _ in range(board_size * board_size)]
        self.current_winner = None
        self.move_history = []
        self.scores = {'X': 0, 'O': 0, 'Draws': 0}
        self.current_player = 'X'

    def print_board(self):
        for row in range(self.board_size):
            print('| ' + ' | '.join(self.board[row*self.board_size:(row+1)*self.board_size]) + ' |')

    def validate_move(self, square):
        if not 0 <= square < self.board_size * self.board_size:
            return False, "Move must be between 0 and {}".format(self.board_size * self.board_size - 1)
        if self.board[square] != ' ':
            return False, "Square already occupied"
        return True, "Valid move"

    def make_move(self, square):
        valid, message = self.validate_move(square)
        if not valid:
            return False, message
        self.board[square] = self.current_player
        self.move_history.append((square, self.current_player))
        if self.check_winner(square):
            self.current_winner = self.current_player
            self.scores[self.current_player] += 1  # Update score for the winner
            return True, "Player {} wins!".format(self.current_player)
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        return True, "Move successful"

    def undo_move(self):
        """Undo the last move made, if any."""
        if not self.move_history:
            return False, "No moves to undo."
        last_move, last_player = self.move_history.pop()
        self.board[last_move] = ' '
        self.current_player = last_player
        return True, "Last move undone."

    def check_winner(self, square):
        row_ind = square // self.board_size
        col_ind = square % self.board_size
        row = self.board[row_ind*self.board_size:(row_ind+1)*self.board_size]
        col = [self.board[col_ind+i*self.board_size] for i in range(self.board_size)]

        def check_line(line):
            return all(spot == self.current_player for spot in line)

        if check_line(row) or check_line(col):
            return True
        if square % (self.board_size + 1) == 0:  # Check diagonal
            if check_line([self.board[i] for i in range(0, self.board_size*self.board_size, self.board_size+1)]):
                return True
        if square % (self.board_size - 1) == 0:  # Check anti-diagonal
            if check_line([self.board[i] for i in range(self.board_size-1, self.board_size*self.board_size-1, self.board_size-1)]):
                return True
        return False

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == ' ']

    def is_board_full(self):
        return ' ' not in self.board

    def reset_game(self):
        self.board = [' ' for _ in range(self.board_size * self.board_size)]
        self.current_winner = None
        self.move_history = []
        self.current_player = 'X'
        print("Game has been reset!")

    def print_scores(self):
        print(f"Scores: X - {self.scores['X']}, O - {self.scores['O']}, Draws - {self.scores['Draws']}")

    def reset_scores(self):
        """Reset the scores for both players."""
        self.scores = {'X': 0, 'O': 0, 'Draws': 0}
        print("Scores have been reset!")

    def suggest_move(self):
        """Suggest a random available move for the current player."""
        moves = self.available_moves()
        if moves:
            suggestion = random.choice(moves)
            print(f"Suggested move for {self.current_player}: {suggestion}")
            return suggestion
        return None

    def save_game(self, filename="tictactoe_save.json"):
        """Save the current game state to a file."""
        game_state = {
            "board": self.board,
            "scores": self.scores,
            "current_player": self.current_player,
            "move_history": self.move_history
        }
        with open(filename, "w") as f:
            json.dump(game_state, f)
        print(f"Game saved to {filename}.")

    def board_to_json(self):
        """Returns the current board state as a JSON object."""
        board_json = {
            "board": [self.board[i*self.board_size:(i+1)*self.board_size] for i in range(self.board_size)],
            "current_player": self.current_player,
            "current_winner": self.current_winner,
            "move_history": self.move_history
        }
        return json.dumps(board_json, indent=2)
    
    def display_move_history(self):
        """Displays a list of all moves made in the game with the player and position."""
        if not self.move_history:
            print("No moves have been made yet.")
        else:
            print("Move History:")
            for move_num, (position, player) in enumerate(self.move_history, start=1):
                print(f"Move {move_num}: Player {player} to position {position}")

    
    def game_status(self):
        """Returns a brief summary of the game status."""
        if self.current_winner:
            return f"Player {self.current_winner} has won the game!"
        elif self.is_board_full():
            return "It's a draw!"
        else:
            return f"Game is ongoing. It's {self.current_player}'s turn."

    def load_game(self, filename="tictactoe_save.json"):
        """Load the game state from a file."""
        try:
            with open(filename, "r") as f:
                game_state = json.load(f)
                self.board = game_state["board"]
                self.scores = game_state["scores"]
                self.current_player = game_state["current_player"]
                self.move_history = game_state["move_history"]
            print(f"Game loaded from {filename}.")
        except FileNotFoundError:
            print(f"No saved game found at {filename}.")

    def game_summary(self):
        """Prints a summary of the current game status, including board state, move history, scores, and winner status."""
        print("\nGame Summary:")
        print("Board:")
        self.print_board()
        print(f"Current Player: {self.current_player}")
        print(f"Move History: {self.move_history}")
        print(f"Scores - X: {self.scores['X']}, O: {self.scores['O']}, Draws: {self.scores['Draws']}")
        if self.current_winner:
            print(f"Winner: {self.current_winner}")
        else:
            print("No winner yet.")
        print("\n")

    def current_player_symbol(self):
        """Return the symbol of the current player."""
        return f"The current player is: {self.current_player}"
    
    def reset_board(self):
        """Resets the board to start a new game."""
        self.board = [" " for _ in range(9)]  # Set all cells to empty
        self.current_winner = None
        return "Board has been reset."
    
    def get_game_state(self):
        """Return the current game state as a dictionary."""
        return {
            "board": self.board,
            "current_player": self.current_player,
            "current_winner": self.current_winner,
            "move_history": self.move_history,
            "scores": self.scores
        }
    
    def get_center_square(self):
        """Return the center square index if available, or None if it's occupied."""
        center = (self.board_size * self.board_size) // 2
        return center if self.board[center] == ' ' else None
    
    def get_player_moves(self, player):
        """Return a list of moves made by the specified player."""
        if player not in ['X', 'O']:
            raise ValueError("Player must be 'X' or 'O'.")
        return [index for index, value in enumerate(self.board) if value == player]

    def get_available_corners(self):
        """Return a list of available corner squares on the board."""
        corners = [0, self.board_size - 1, 
                self.board_size * (self.board_size - 1), 
                self.board_size * self.board_size - 1]
        return [corner for corner in corners if self.board[corner] == ' ']
    
    def is_game_over(self):
        """Return True if the game is over (win or draw), otherwise False."""
        return self.current_winner is not None or self.is_board_full()

    def print_divider(self):
        """Prints a visual divider for better readability between game updates."""
        print("\n" + "-" * (self.board_size * 4) + "\n")

    def board_to_string(self):
        """Returns the current board state as a formatted string."""
        rows = ["| " + " | ".join(self.board[i*self.board_size:(i+1)*self.board_size]) + " |" for i in range(self.board_size)]
        return "\n".join(rows)
    
    def set_symbols(self, player_x='X', player_o='O'):
        """Sets custom symbols for player X and player O."""
        self.player_x = player_x
        self.player_o = player_o
        print(f"Player X symbol set to: {self.player_x}")
        print(f"Player O symbol set to: {self.player_o}")

    def get_remaining_moves_count(self):
        """Returns the count of remaining available moves on the board."""
        return len(self.available_moves())

def play_game():
    game = TicTacToe()
    print("Welcome to Tic Tac Toe!")
    print("Enter -1 at any time to reset the game.")
    print("Enter -2 to undo the last move.")
    print("Enter -3 to get a move suggestion.")
    print("Enter -4 to save the game.")
    print("Enter -5 to load a saved game.")
    while True:
        game.print_board()
        try:
            square = int(input(f"Turn for {game.current_player}. Move on which space? (0-{game.board_size*game.board_size - 1}): "))
            if square == -1:  # Check if the reset command is entered
                game.reset_game()
                continue
            elif square == -2:  # Undo last move
                success, msg = game.undo_move()
                print(msg)
                continue
            elif square == -3:  # Suggest a move
                game.suggest_move()
                continue
            elif square == -4:  # Save the game
                game.save_game()
                continue
            elif square == -5:  # Load a saved game
                game.load_game()
                continue
            success, msg = game.make_move(square)
            print(msg)
            if success:
                if msg.startswith("Player"):
                    print("Game Over")
                    game.print_board()  # Show the final board
                    game.print_scores()  # Print scores after game ends
                    break
                elif game.is_board_full():
                    print("It's a tie!")
                    game.scores['Draws'] += 1  # Update score for a draw
                    game.print_board()  # Show the final board
                    game.print_scores()  # Print scores after game ends
                    break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == '__main__':
    play_game()
