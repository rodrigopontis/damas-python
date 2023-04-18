from boardEntities import *
from exceptions import CheckersException

# Nivel jogo de damas


class CheckersPosition:
    def __init__(self, column, row):
        if ord(column) < ord("a") or ord(column) > ord("h") or row < 0 or row > 8:
            raise CheckersException("Insira uma posição válida (a1 a h8)")

        self.column = column
        self.row = row

    def toPosition(self):
        return Position(self.row - 1, (ord(self.column) - ord("a")))

    def fromPosition(position):
        return CheckersPosition(chr(ord("a") + position.column), position.row + 1)

    def toString(self):
        return self.column + str(self.row)


class CheckersPiece(Piece):
    moveCount = 0

    def __init__(self, board, color):
        super().__init__(board)
        self.color = color

    def increaseMoveCount(self):
        self.moveCount += 1

    def decreaseMoveCount(self):
        self.moveCount -= 1

    def possibleMoves(self):
        moves = [
            [False for x in range(self.board.rows)] for y in range(self.board.columns)
        ]

        if self.color == "white":
            right = Position(self.position.row - 1, self.position.column + 1)
            left = Position(self.position.row - 1, self.position.column - 1)

            if self.board.positionExists(right):
                if self.board.haveAPiece(right) == False:
                    moves[right.row][right.column] = True
                elif self.haveAOpponentPiece(right):
                    print("Peça adversaria na direita")
                    moves[right.row - 1][right.column + 1] = True

            if self.board.positionExists(left):
                print("possible move left", left)

        return moves

    def getCheckersPosition(self):
        return CheckersPosition.fromPosition(self.position)

    def haveAOpponentPiece(self, position):
        piece = self.board.getPieceFromPosition(position)

        return piece != None and piece.color != self.color


class CheckersMatch:
    piecesInGame = []

    def __init__(self):
        self.board = Board(8, 8)
        self.currentPlayer = "white"
        self.turn = 1
        self.initialSetup()

    def makingACheckersMovement(self, sourcePosition, targetPosition):
        source = CheckersPosition(
            sourcePosition[0], int(sourcePosition[1])
        ).toPosition()
        target = CheckersPosition(
            targetPosition[0], int(targetPosition[1])
        ).toPosition()

        self.validateSourcePosition(source)
        # self.validateTargetPosition(source, target)

        self.makeMove(source, target)

    def makeMove(self, source, target):
        print("moving", source, "to", target)

    def possibleMoves(self, source):
        pos = CheckersPosition(source[0], int(source[1])).toPosition()
        self.validateSourcePosition(pos)

        return self.board.getPieceFromPosition(pos).possibleMoves()

    def validateSourcePosition(self, source):
        if self.board.haveAPiece(source) == False:
            raise CheckersException("Não tem peça na posição selecionada.")

        if self.currentPlayer != self.board.getPieceFromPosition(source).color:
            raise CheckersException("A peça escolhida não é do seu time.")

        # if (self.board.getPieceFromPosition(source).havePossibleMove() == False):
        #     raise CheckersException(
        #         "Não existem movimentos possíveis para a peça selecionada.")

    def validateTargetPosition(self, source, target):
        if self.board.getPieceFromPosition(source).possibleMove(target) == False:
            raise CheckersException(
                "A peça escolhida nao pode se mover para a posição selecionada."
            )

    def placeNewPiece(self, column, row, piece):
        self.board.placePiece(piece, CheckersPosition(column, row).toPosition())
        self.piecesInGame.append(piece)

    def initialSetup(self):
        # whitePositions = [
        #     "a8",
        #     "c8",
        #     "e8",
        #     "g8",
        #     "b7",
        #     "d7",
        #     "f7",
        #     "h7",
        #     "a6",
        #     "c6",
        #     "e6",
        #     "g6",
        # ]

        # blackPositions = [
        #     "b1",
        #     "d1",
        #     "f1",
        #     "h1",
        #     "a2",
        #     "c2",
        #     "e2",
        #     "g2",
        #     "b3",
        #     "d3",
        #     "f3",
        #     "h3",
        # ]

        # for i in whitePositions:
        #     self.placeNewPiece(i[0], int(i[1]), CheckersPiece(self.board, "white"))

        # for i in blackPositions:
        #     self.placeNewPiece(i[0], int(i[1]), CheckersPiece(self.board, "black"))

        # Setup de teste
        self.placeNewPiece("a", 8, CheckersPiece(self.board, "white"))
        self.placeNewPiece("b", 7, CheckersPiece(self.board, "black"))
