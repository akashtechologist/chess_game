class Piece:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return self.symbol

class King(Piece):
    symbol = 'K'

class Queen(Piece):
    symbol = 'Q'

class Rook(Piece):
    symbol = 'R'

class Bishop(Piece):
    symbol = 'B'

class Knight(Piece):
    symbol = 'N'

class Pawn(Piece):
    symbol = 'P'

class Board:
    def __init__(self):
        self.board = [[' ' for _ in range(8)] for _ in range(8)]
        self.setup_board()

    def setup_board(self):
        for i in range(8):
            self.board[1][i] = Pawn('black')
            self.board[6][i] = Pawn('white')

        self.board[0][0] = self.board[0][7] = Rook('black')
        self.board[0][1] = self.board[0][6] = Knight('black')
        self.board[0][2] = self.board[0][5] = Bishop('black')
        self.board[0][3] = Queen('black')
        self.board[0][4] = King('black')

        self.board[7][0] = self.board[7][7] = Rook('white')
        self.board[7][1] = self.board[7][6] = Knight('white')
        self.board[7][2] = self.board[7][5] = Bishop('white')
        self.board[7][3] = Queen('white')
        self.board[7][4] = King('white')
        print("Game started");

    def print_board(self):
        for row in self.board:
            print(' '.join(str(piece) if piece != ' ' else '.' for piece in row))

    def move_piece(self, start, end):
        start_x, start_y = start
        end_x, end_y = end
        piece = self.board[start_x][start_y]
        if piece != ' ':
            self.board[end_x][end_y] = piece
            self.board[start_x][start_y] = ' '
        else:
            print("No piece at the starting position.")

class Game:
    def __init__(self):
        self.board = Board()
        self.turn = 'white'

    def play(self):
        while True:
            self.board.print_board()
            print(f"{self.turn}'s turn")
            start = input("Enter the starting position (e.g., 6 0): ").split()
            end = input("Enter the ending position (e.g., 4 0): ").split()

            start = (int(start[0]), int(start[1]))
            end = (int(end[0]), int(end[1]))

            self.board.move_piece(start, end)
            self.turn = 'black' if self.turn == 'white' else 'white'

if __name__ == '__main__':
    game = Game()
    game.play()
    print("game end");
