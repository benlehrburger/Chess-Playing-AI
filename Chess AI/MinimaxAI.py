import chess
import math
import random

# Wrap a chess playing AI object with minimax search
class MinimaxAI():

    # Initialize instance variables
    def __init__(self, depth):
        # Save starting depth
        self.depth = depth
        # Track number of nodes visited
        self.nodes = []
        # Set max player
        self.player = True

    # Find best move for the maximizer
    def max_value(self, board, depth):

        # BASE CASE
        # If we reach the depth cutoff or the game is over
        if self.cutoff_test(board, depth):
            # Count up the utility of the terminal states
            return self.utility(board)

        # Best value is initially infinitely negative
        best_val = -math.inf

        # For each legal move on the board
        for action in board.legal_moves:
            # Execute that move
            board.push(action)
            # Increment the node tracker
            self.nodes.append(action)
            # Recurse to the minimizer and the next level in the game tree
            child_val = self.min_value(board, depth - 1)
            # Undo that move
            board.pop()
            # Save the maximum utility
            best_val = max(best_val, child_val)

        # Return the maximum utility
        return best_val

    # Find best move for the minimizer
    def min_value(self, board, depth):

        # BASE CASE
        # If we reach the depth cutoff or the game is over
        if self.cutoff_test(board, depth):
            # Count up the utility of the terminal states
            return self.utility(board)

        # Best value is initially infinitely positive
        best_val = math.inf

        # For each legal move on the board
        for action in board.legal_moves:
            # Execute that move
            board.push(action)
            # Increment the node tracker
            self.nodes.append(action)
            # Recurse to the maximizer and the next level in the game tree
            child_val = self.max_value(board, depth - 1)
            # Undo that move
            board.pop()
            # Save the maximum utility
            best_val = min(best_val, child_val)

        # Return the maximum utility
        return best_val

    # Choose a move for the current player
    def choose_move(self, board):

        # Boolean for current player; white is True, black is False
        self.player = board.turn

        # Shuffle the list of current board moves
        moves = list(board.legal_moves)
        random.shuffle(moves)

        # Best move is initially None
        best_move = None
        # Best value is initially infinitely negative
        best_val = -math.inf

        # For each legal move on the board
        for action in moves:
            # Execute that move
            board.push(action)
            # Recurse to the minimizer and the next level in the game tree
            child_val = self.min_value(board, self.depth - 1)
            # Undo that move
            board.pop()

            # Save the best move
            if child_val > best_val:
                best_move = action

        print("Checking " + str(len(self.nodes)) + " nodes")

        # Return the best move
        return best_move

    # Check if we have reached our base case
    def cutoff_test(self, board, depth):

        # Return True if we reach a depth of 0 or the game is over
        if depth == 0 or board.is_game_over():
            return True

    # EVALUATION FUNCTION
    # Calculate the utility of a terminal state
    def utility(self, board):

        # Utility is initially 0
        util = 0

        # Difference in number of pawns weighed by pawn value
        util += 1 * (len(board.pieces(chess.PAWN, self.player)) - len(board.pieces(chess.PAWN, not self.player)))
        # Difference in number of knights weighed by knight value
        util += 3 * (len(board.pieces(chess.KNIGHT, self.player)) - len(board.pieces(chess.KNIGHT, not self.player)))
        # Difference in number of bishops weighed by bishop value
        util += 3 * (len(board.pieces(chess.BISHOP, self.player)) - len(board.pieces(chess.BISHOP, not self.player)))
        # Difference in number of rooks weighed by rook value
        util += 5 * (len(board.pieces(chess.ROOK, self.player)) - len(board.pieces(chess.ROOK, not self.player)))
        # Difference in number of queens weighed by queen value
        util += 9 * (len(board.pieces(chess.QUEEN, self.player)) - len(board.pieces(chess.QUEEN, not self.player)))
        # Difference in number of kings weighed by king value
        util += 200 * (len(board.pieces(chess.KING, self.player)) - len(board.pieces(chess.KING, not self.player)))

        # Return utility
        return util
