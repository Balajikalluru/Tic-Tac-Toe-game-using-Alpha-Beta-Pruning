# Tic-Tac-Toe-game-using-Alpha-Beta-Pruning
### Overview
This project implements a Tic Tac Toe game in Python with an AI opponent that uses the Alpha Beta Pruning algorithm.
The AI is designed to make optimal moves, providing a challenging and engaging gameplay experience.

### Features
Two-player Mode: Play against an AI opponent or a human.<br/>
AI Mode: AI uses Alpha Beta Pruning for efficient decision-making.<br/>
Interactive Console: User-friendly console interface.<br/>
Game States: Real-time game board updates and outcome display (win, lose, draw).<br/>
### Alpha Beta Pruning
Alpha Beta Pruning is an optimization for the minimax algorithm.
It reduces the number of nodes evaluated in the game tree by eliminating branches that do not affect the final decision.
This makes the AI opponent both efficient and effective in determining the best possible moves.

### How to Play
The game is played on a 3x3 grid.<br/>
Players take turns placing X or O on the grid.<br/>
The first player to align three marks (horizontal, vertical, or diagonal) wins.<br/>
If all nine squares are filled without alignment, the game ends in a draw.<br/>

#### Code Structure
Tic_Tac_Toe.py: Main game script containing the game logic and Alpha Beta Pruning implementation.<br/>

##### Prerequisites<br/>
Python 3.x<br/>

#### Acknowledgments
This project was inspired by various resources on game AI and Alpha Beta Pruning.
