from boardEntities import *
from exceptions import CheckersException

# Nivel jogo de damas


class CheckersPosition:

    def __init__(self, column, row):
        if (column < 'a' or column > 'h' or row < 0 or row > 8):
            raise CheckersException("Insira uma posição válida (a1 a h8)")

        self.column = column
        self.row = row

    def toPosition(self):
        return Position(self.row, ord(self.column) - ord('a'))

    def fromPosition(self, position):
        return self.__init__(ord('a') + position.column, 8 - position.row)


class CheckersPiece(Piece):
    moveCount = 0

    def __init__(self, board, color):
        super().__init__(board)
        self.color = color

    def increaseMoveCount(self):
        self.moveCount += 1

    def decreaseMoveCount(self):
        self.moveCount -= 1

    def getCheckersPosition(self):
        return CheckersPosition.fromPosition(self.position)

    def haveAOpponentPiece(self, position):
        piece = getattr(self.board.getPieceFromPosition(
            position), CheckersPiece)

        return piece != None and piece.getColor() != self.color


class CheckersMatch:
    piecesInGame = []

    def __init__(self):
        self.board = Board(8, 8)
        self.currentPlayer = 'white'
        self.turn = 1
        # self.initialSetup()

    def placeNewPiece(self, column, row, piece):
        print("trying to put a", piece.color, "piece to the position:",
              column, ",", row)
        # self.board.placePiece(
        #     piece, CheckersPosition(column, row).toPosition())
        # self.piecesInGame.append(piece)

    def initialSetup(self):
        newPiece = CheckersPiece(self.board, 'white')
        self.placeNewPiece('a', 1, newPiece)
