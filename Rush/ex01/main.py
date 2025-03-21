import sys
from checkmate import checkmate

def is_valid_board(board):
    rows = board.splitlines()
    if len(rows) == 0:
        return False
    
    length = len(rows[0])
    for row in rows:
        if len(row) != length:
            return False
    return True

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.read().strip()
    except Exception:
        return None

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <file1> [file2 ...]")
        sys.exit(1)
    
    for file in sys.argv[1:]:
        board = read_file(file)
        if board is None or not is_valid_board(board):
            print("Error")
        else:
            checkmate(board)

if __name__ == "__main__":
    main()
