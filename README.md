Chess Ranger Puzzle Solver

A Python program that solves the Chess Ranger Puzzle from https://www.puzzle-chess.com/chess-ranger/

---

 Features

- **User-Friendly Input:** Enter chessboard setup directly via the console using  chess notation.
- **Recursive Solver:** Finds a sequence of moves that reduces the board to a single piece or indicates if no solution exists.

---

 How It Works

1. Input Format
   - The program will ask you to type the list of pieces and their positions, separated by spaces.
     Each piece is represented by its name (P for pawn N for Knight R for Rook B for Bishop Q for Queen K for King) followed by the position on the board (e.g., a6). After typing the pieces, press Enter
   - Example: `Na6 Rb6 Bc5 Bd6 Pd5 Rd8 Pd7 Be5 Be6 Pf7 Pg1`
   - Input is case sensitive so qa6 will not work

2. Output
   - The program outputs a sequence of moves that solve the puzzle.
   - Moves are displayed in chess notation, e.g., `Rb6xc5` (Rook at b6 captures Bishop at c5).
