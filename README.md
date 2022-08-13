# Chess-Playing-AI

I implemented three different search algorithms to inform a chess-playing AI. The algorithms are: minimax, alpha-beta pruning, and iterative deepening. The program is intelligent at all three stages and can beat most competent human opponents.

The first search algorithm that I programmed was minimax. The algorithm assumes that its opponent is using an optimal strategy, which allows it to calculate the future utility of its present moves. Each legal move represents a node in a game tree. The first level of the game tree is the maximizer, the current player. The second level of the tree is the opponent's move, whose utility the maximizer tries to make as little as possible. Each consecutive level in the game tree oscillates between the maximizer and their opponent's moves. The minimax object accepts a maximum depth as a parameter, which represents the base case of the recursion. The other base case is if the game is in a checkmate or stalemate. If the algorithm does not reach a terminal state before the depth limit is exceeded, it calculates the utilities of those terminal nodes and bubbles upwards through the game tree. The maximizer levels choose the minimum utility at the level below, and vice versa for their opponent's levels. At last, the algorithm returns a move with the highest possible utility.

Without a utility calculator, the algorithm is not particularly intelligent. Once I calculated the utility at a terminal state in my heuristic evaluation function, however, the algorithm was able to gain some foresight. I chose to calculate utility as the difference between the maximizer and their opponent's pieces on the board, each weighed by that piece's respective value. Those values are as follows:

Pawn: 1  
Knight: 3  
Bishop: 3  
Rook: 5  
Queen: 9  
King: 200  

I then implemented the minimax algorithm with alpha-beta pruning to decrease the number of nodes that the algorithm has to visit before returning a best move. Alpha represents the best choice that we have found so far at any point along the path of the maximizer, while beta is the best choice we have found so far at any point along the path of the minimizer. It reduces computational demand by stopping minimax from evaluating more nodes when at least one possibility has been found that proves the move to be worse than a previously examined one because those nodes need not be expanded.

Lastly, I programmed an iterative deepening algorithm. It works identically to the minimax algorithm, except at each depth in the game tree prior to reaching our terminal state, the algorithm saves that level's best move. This helps ensure that our algorithm is choosing the optimal move at each turn. One would think that minimax does this, but it is possible that there is a move with higher utility higher up in the game tree that is invisible to us from just judging the utility of our terminal states. So, iterative deepening prevents that possibility by choosing the overall best move available from all levels.
