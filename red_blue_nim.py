import argparse
import sys

# Class representing the Red-Blue Nim Game
class RedBlueNimGame:
    def __init__(self, num_red, num_blue, version, first_player, depth):
        # Initialize the game with the given parameters
        self.num_red = num_red
        self.num_blue = num_blue
        self.version = version
        self.current_player = first_player
        self.depth = depth if depth else float('inf')  # Set depth to infinity if not provided

    # Check if the game is over
    def is_game_over(self):
        return self.num_red == 0 or self.num_blue == 0

    # Get the current score based on the number of marbles
    def get_score(self):
        return 2 * self.num_red + 3 * self.num_blue

    # Make a move by removing the specified number of red and blue marbles
    def make_move(self, num_red, num_blue):
        if num_red <= self.num_red and num_blue <= self.num_blue and (num_red > 0 or num_blue > 0):
            self.num_red -= num_red
            self.num_blue -= num_blue
            return True
        return False

    # Switch the current player
    def switch_player(self):
        self.current_player = 'human' if self.current_player == 'computer' else 'computer'

    # Handle the human player's move
    def human_move(self):
        while True:
            print(f"Your turn. Red marbles: {self.num_red}, Blue marbles: {self.num_blue}")
            try:
                num_red = int(input("Enter number of red marbles to take: "))
                num_blue = int(input("Enter number of blue marbles to take: "))
                if self.make_move(num_red, num_blue):
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Please enter integers.")

    # Handle the computer player's move using the minimax algorithm
    def computer_move(self):
        best_score = -float('inf')
        best_move = None
        for move in self.generate_moves():
            score = self.minmax(move[0], move[1], self.depth, -float('inf'), float('inf'), False)
            if score > best_score:
                best_score = score
                best_move = move
        if best_move:
            print(f"Computer takes {best_move[0]} red marbles and {best_move[1]} blue marbles.")
            self.make_move(best_move[0], best_move[1])

    # Generate possible moves based on the game version
    def generate_moves(self):
        moves = []
        if self.version == 'standard':
            moves.extend([(2, 0), (0, 2), (1, 0), (0, 1)])
        else:
            moves.extend([(0, 1), (1, 0), (0, 2), (2, 0)])
        return [(r, b) for r, b in moves if self.num_red >= r and self.num_blue >= b]

    # Minimax algorithm with alpha-beta pruning to find the best move
    def minmax(self, num_red, num_blue, depth, alpha, beta, is_maximizing):
        self.make_move(num_red, num_blue)
        if self.is_game_over() or depth == 0:
            score = self.get_score()
            self.num_red += num_red
            self.num_blue += num_blue
            return score if self.version == 'standard' else -score

        if is_maximizing:
            max_eval = -float('inf')
            for move in self.generate_moves():
                eval = self.minmax(move[0], move[1], depth - 1, alpha, beta, False)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            self.num_red += num_red
            self.num_blue += num_blue
            return max_eval
        else:
            min_eval = float('inf')
            for move in self.generate_moves():
                eval = self.minmax(move[0], move[1], depth - 1, alpha, beta, True)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            self.num_red += num_red
            self.num_blue += num_blue
            return min_eval

    # Main game loop
    def play(self):
        while not self.is_game_over():
            if self.current_player == 'human':
                self.human_move()
            else:
                self.computer_move()
            self.switch_player()

        # Determine the winner based on the game version and the current player
        if self.version == 'standard':
            winner = 'computer' if self.current_player == 'human' else 'human'
        else:
            winner = 'human' if self.current_player == 'human' else 'computer'

        print(f"Game over! {winner} wins!")
        print(f"Final Score: {self.get_score()}")

# Function to parse command-line arguments
def parse_args():
    parser = argparse.ArgumentParser(description="Red-Blue Nim Game")
    parser.add_argument("num_red", type=int, help="Number of red marbles")
    parser.add_argument("num_blue", type=int, help="Number of blue marbles")
    parser.add_argument("--version", type=str, choices=['standard', 'misere'], default='standard', help="Game version")
    parser.add_argument("--first-player", type=str, choices=['human', 'computer'], default='computer', help="First player")
    parser.add_argument("--depth", type=int, help="Search depth for AI (optional)")
    return parser.parse_args()

# Main function to start the game
if __name__ == "__main__":
    args = parse_args()
    game = RedBlueNimGame(args.num_red, args.num_blue, args.version, args.first_player, args.depth)
    game.play()
