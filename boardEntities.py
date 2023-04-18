from exceptions import BoardException

# Nivel de tabuleiro


class Position:
    def __init__(self, row, column):
        self.row = row
        self.column = column

    def setValues(self, row, column):
        self.row = row
        self.column = column

    def __eq__(self, other):
        return self.column == other.column and self.row == other.row


class Piece:
    position = None

    def __init__(self, board):
        self.board = board

    def possibleMoves():
        return []

    def possibleMove(self, position):
        return self.possibleMoves()[position.row, position.column]

    def havePossibleMove(self):
        return True

    def isAPossibleMove(self):
        matrix = self.possibleMoves()

        for i in matrix:
            for j in matrix[i]:
                if matrix[i, j]:
                    return True

        return False


class Board:
    pieces = []
    rows = 0
    columns = 0

    def __init__(self, rows, columns):
        if rows < 1 or columns < 1:
            raise BoardException("Número de linhas ou colunas inválido.")

        self.rows = rows
        self.columns = columns
        self.pieces = [[None for x in range(rows)] for y in range(columns)]

    def getPieces(self):
        return self.pieces

    def getPieceFromPosition(self, position):
        if self.positionExists(position) == False:
            raise BoardException("Posição não encontrada.")

        return self.getPiece(position.row, position.column)

    def placePiece(self, piece, position):
        if self.haveAPiece(position):
            raise BoardException("Já existe uma peça nessa posição.")

        self.pieces[position.row][position.column] = piece
        piece.position = position

    def removePiece(self, position):
        if self.positionExists(position) == False:
            raise BoardException("Esta posição não existe no tabuleiro.")

        if self.getPieceFromPosition(position) == None:
            return None

        removedPiece = self.getPieceFromPosition(position)
        removedPiece.position = None
        self.pieces[position.row][position.column] = None

        return removedPiece

    def getPiece(self, row, column):
        return self.pieces[row][column]

    def positionExists(self, position):
        return (
            position.row >= 0
            and position.row < self.rows
            and position.column >= 0
            and position.column < self.columns
        )

    def haveAPiece(self, position):
        if self.positionExists(position) == False:
            raise BoardException("Posição não encontrada.")

        return self.getPieceFromPosition(position) != None
