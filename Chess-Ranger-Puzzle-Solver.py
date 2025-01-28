from copy import deepcopy

# Define movement rules for each piece
MOVES = {
    'P': lambda x, y, board: [(x + dx, y + dy) for dx, dy in [(-1, -1), (-1, 1)] if is_valid(x + dx, y + dy, board)],
    'N': lambda x, y, board: [(x + dx, y + dy) for dx, dy in [(2, 1), (1, 2), (-1, 2), (-2, 1),
                                                              (-2, -1), (-1, -2), (1, -2), (2, -1)]
                              if is_valid(x + dx, y + dy, board)],
    'B': lambda x, y, board: sliding_moves(x, y, board, [(1, 1), (1, -1), (-1, 1), (-1, -1)]),
    'R': lambda x, y, board: sliding_moves(x, y, board, [(0, 1), (1, 0), (0, -1), (-1, 0)]),
    'Q': lambda x, y, board: sliding_moves(x, y, board, [(1, 1), (1, -1), (-1, 1), (-1, -1),
                                                         (0, 1), (1, 0), (0, -1), (-1, 0)]),
    'K': lambda x, y, board: [(x + dx, y + dy) for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1),
                                                              (1, 1), (-1, 1), (-1, -1), (1, -1)]
                              if is_valid(x + dx, y + dy, board)],
}

def is_valid(x, y, board):
    """Check if a position is valid and contains an opponent piece."""
    return 0 <= x < 8 and 0 <= y < 8 and board[x][y] is not None

def sliding_moves(x, y, board, directions):
    """Generate moves for sliding pieces like bishops, rooks, and queens."""
    moves = []
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        while 0 <= nx < 8 and 0 <= ny < 8:  # Stay within board boundaries
            if board[nx][ny] is not None:  # If a piece is encountered
                moves.append((nx, ny))  # Capture it
                break  # Stop sliding in this direction
            nx, ny = nx + dx, ny + dy
    return moves

def get_valid_moves(x, y, piece, board):
    """Get all valid capture moves for a piece at position (x, y)."""
    return [(nx, ny) for nx, ny in MOVES[piece](x, y, board) if board[nx][ny] is not None]

def coords_to_chess_notation(x, y):
    """Convert board coordinates to chess notation (e.g., (0, 0) -> 'a8')."""
    col_to_file = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}
    row_to_rank = {0: '8', 1: '7', 2: '6', 3: '5', 4: '4', 5: '3', 6: '2', 7: '1'}
    return f"{col_to_file[y]}{row_to_rank[x]}"

def solve(board, move_history):
    """Recursively solve the Chess Ranger puzzle."""
    # Check if the board has only one piece left
    pieces = [(x, y, board[x][y]) for x in range(8) for y in range(8) if board[x][y] is not None]
    if len(pieces) == 1:
        return True, move_history  # Solution found

    for x, y, piece in pieces:
        valid_moves = get_valid_moves(x, y, piece, board)
        for nx, ny in valid_moves:
            # Create a new board state
            new_board = deepcopy(board)
            new_board[nx][ny] = piece  # Move the piece
            new_board[x][y] = None  # Remove the piece from the original position
            # Record the move
            move = f"{piece}{coords_to_chess_notation(x, y)}x{coords_to_chess_notation(nx, ny)}"
            # Recursively solve the updated board
            solved, solution = solve(new_board, move_history + [move])
            if solved:
                return True, solution

    return False, []  # No solution found

def chess_notation_to_coords(notation):
    """Convert chess square notation (e.g., 'a6') to board coordinates (row, col)."""
    file_to_col = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
    rank_to_row = {'1': 7, '2': 6, '3': 5, '4': 4, '5': 3, '6': 2, '7': 1, '8': 0}
    col = file_to_col[notation[0]]
    row = rank_to_row[notation[1]]
    return row, col

def initialize_board(pieces):
    """Convert a list of pieces in chess notation to an 8x8 board."""
    board = [[None for _ in range(8)] for _ in range(8)]  # Empty board
    for piece in pieces:
        piece_type = piece[0]  # First character is the piece type
        position = piece[1:]  # Remaining characters are the square
        row, col = chess_notation_to_coords(position)
        board[row][col] = piece_type
    return board

def parse_fen(fen):
    """Parse a FEN string and return the board state as a list of pieces."""
    board = [[None for _ in range(8)] for _ in range(8)]
    
    # Take the board layout before the first space (ignoring turn and game state info)
    board_part = fen.split(' ')[0]
    
    rows = board_part.split('/')
    for i, row in enumerate(rows):
        col = 0
        for char in row:
            if char.isdigit():  # Empty squares
                col += int(char)
            else:
                board[i][col] = char  # Use the piece as is (keep case)
                col += 1
    return board

# Prompt user to input chessboard setup
print("You can enter the chessboard setup in either of these formats:")
print("1. Standard chess notation: e.g., 'Na6 Rb6 Bc5'.")
print("2. FEN format: e.g., 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'")

user_input = input("Enter your chessboard setup: ").strip()

# Check if the input contains '/' indicating it could be a FEN string
if "/" in user_input:
    user_input = user_input.upper()

    board = parse_fen(user_input)  # User entered FEN format
elif " " in user_input:
    user_input = user_input.title()

    pieces = user_input.split()  # User entered standard chess notation
    board = initialize_board(pieces)
else:
    print("Invalid input format. Please try again.")
    exit()

# Solve the puzzle
solved, solution = solve(board, [])
if solved:
    print("Solution Found!")
    for step, move in enumerate(solution):
        print(f"Step {step + 1}: {move}")
else:
    print("No solution exists.")
