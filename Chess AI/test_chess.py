# pip3 install python-chess


import chess
import sys
from RandomAI import RandomAI
from HumanPlayer import HumanPlayer
from MinimaxAI import MinimaxAI
from AlphaBetaAI import AlphaBetaAI
from ChessGame import ChessGame
from IterativeDeepeningAI import IterativeDeepeningAI

# Initialize player 1 players
player1 = RandomAI()
#player1 = HumanPlayer()
#player1 = MinimaxAI(3)
#player1 = AlphaBetaAI(3)
#player1 = IterativeDeepeningAI(3)

# Initialize player 2 players
#player2 = RandomAI()
player2 = HumanPlayer()
#player2 = MinimaxAI(3)
#player2 = AlphaBetaAI(3)
#player2 = IterativeDeepeningAI(3)

game = ChessGame(player1, player2)

while not game.is_game_over():
    print(game)
    game.make_move()


if game.board.is_checkmate():
    if game.board.outcome().winner is False:
        print("Checkmate! The black team has won!")
    else:
        print("Checkmate! The white team has won!")
elif game.board.is_stalemate():
    print("The game has ended in a stalemate!")
else:
    print("Rage quit!")



#print(hash(str(game.board)))
