Chess Ranger Puzzle Solver

A Python program that solves the Chess Ranger Puzzle from https://www.puzzle-chess.com/chess-ranger/

---

 Features

- **User-Friendly Input:** Enter chessboard setup directly via the console using  chess notation.
- **Recursive Solver:** Finds a sequence of moves that reduces the board to a single piece or indicates if no solution exists.

---

 How It Works

1. Input Format
The program allows you to enter the chessboard setup in one of two formats:

    Standard Chess Notation:
        Enter the list of pieces and their positions, separated by spaces.
        Each piece is represented by its name (P for Pawn, N for Knight, R for Rook, B for Bishop, Q for Queen, K for King) followed by its position on the board (e.g., a6, b5).
        Example: Na6 Rb6 Bc5 Bd6 Pd5 Rd8 Pd7 Be5 Be6 Pf7 Pg1
    FEN Format:
        Alternatively, you can enter the board layout using FEN 
        Example : 8/5P2/6P1/2PPR3/1B1N4/1K3RB1/6r1/8 w - - 0 1
        The input is expected to follow the FEN standard, where numbers represent empty squares, and letters represent pieces (uppercase for white, lowercase for black).

2. Output
   - The program outputs a sequence of moves that solve the puzzle.
   - Moves are displayed in chess notation, e.g., `Rb6xc5` (Rook at b6 captures Bishop at c5).
  
   - 
