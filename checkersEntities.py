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
        return Position(self.row - 1, (ord(self.column) - ord('a')))

    def fromPosition(self, position):
        return self.__init__(chr(ord('a') + position.column), 7 - position.row)


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
        self.initialSetup()

    def makingACheckersMovement(self, sourcePosition, targetPosition):
        source = sourcePosition.toPosition()
        target = targetPosition.toPosition()

        self.validateSourcePosition(source)
        self.validateTargetPosition(target)

    def makeMove(self, sourcePosition, targetPosition):
        movingPiece = self.board.getPieceFromPosition(sourcePosition)

    def validateSourcePosition(self, source):
        if self.board.haveAPiece(source) == False:
            raise CheckersException("Não tem peça na posição selecionada.")

        if (self.currentPlayer != self.board.getPieceFromPosition(source).color):
            raise CheckersException("A peça escolhida não é do seu time.")

        # if (self.board.getPieceFromPosition(source).havePossibleMove() == False):
        #     raise CheckersException(
        #         "Não existem movimentos possíveis para a peça selecionada.")

    def validateTargetPosition(self, source, target):
        if (self.board.getPieceFromPosition(source).possibleMove(target) == False):
            raise CheckersException(
                "A peça escolhida nao pode se mover para a posição selecionada.")

    def placeNewPiece(self, column, row, piece):
        self.board.placePiece(
            piece, CheckersPosition(column, row).toPosition())
        self.piecesInGame.append(piece)

    def initialSetup(self):
        whitePositions = ['a8', 'c8', 'e8', 'g8', 'b7',
                          'd7', 'f7', 'h7', 'a6', 'c6', 'e6', 'g6']

        blackPositions = ['b1', 'd1', 'f1', 'h1', 'a2',
                          'c2', 'e2', 'g2', 'b3', 'd3', 'f3', 'h3']

        for i in whitePositions:
            self.placeNewPiece(
                i[0], int(i[1]), CheckersPiece(self.board, "white"))

        for i in blackPositions:
            self.placeNewPiece(
                i[0], int(i[1]), CheckersPiece(self.board, "black"))
