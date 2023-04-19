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

    def __eq__(self, other):
        return self.column == other.column and self.row == other.row

    def toString(self):
        return self.column + str(self.row)


class CheckersPiece(Piece):
    moveCount = 0
    piecesToEat = []

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
            right = self.directions(self.position)["ne"]
            left = self.directions(self.position)["nw"]

            if self.board.positionExists(right):
                # verificando se existe uma peça
                # na posicao a direita
                if self.board.haveAPiece(right) == False:
                    moves[right.row][right.column] = True

                # caso tenha uma peça
                # verifica se é inimiga
                elif self.haveAOpponentPiece(right):
                    # caso exista um espaço vazio
                    # depois da peça inimiga
                    # verifica se tem a possibilidade
                    # de comer mais de uma peça
                    checkingPos = Position(right.row - 1, right.column + 1)
                    if (
                        self.board.positionExists(checkingPos)
                        and self.board.haveAPiece(checkingPos) == False
                    ):
                        newPos = self.eatPiece(checkingPos)
                        moves[newPos.row][newPos.column] = True

            if self.board.positionExists(left):
                if self.board.haveAPiece(left) == False:
                    moves[left.row][left.column] = True
                elif self.haveAOpponentPiece(left):
                    checkingPos = Position(left.row - 1, left.column - 1)
                    if (
                        self.board.positionExists(checkingPos)
                        and self.board.haveAPiece(checkingPos) == False
                    ):
                        newPos = self.eatPiece(checkingPos)
                        moves[newPos.row][newPos.column] = True

        return moves

    def eatPiece(self, position):
        possibilities = []
        self.verifyAllDirections(position, possibilities)

        if len(possibilities) > 0:
            return possibilities.pop()
        else:
            return position

    def verifyAllDirections(self, position, stack):
        if (
            self.board.positionExists(position)
            and self.board.haveAPiece(position) == False
        ):
            print("Verifying", CheckersPosition.fromPosition(position).toString())
            stack.append(position)
            for direction in self.directions(position):
                pos = self.directions(position)[direction]
                if pos != position and self.haveAOpponentPiece(pos):
                    if direction == "ne":
                        newPos = Position(pos.row - 1, pos.column + 1)
                        self.verifyAllDirections(newPos, stack)
                    if direction == "nw":
                        newPos = Position(pos.row - 1, pos.column - 1)
                        self.verifyAllDirections(newPos, stack)
                    if direction == "se":
                        newPos = Position(pos.row + 1, pos.column + 1)
                        self.verifyAllDirections(newPos, stack)
                    if direction == "sw":
                        newPos = Position(pos.row + 1, pos.column - 1)
                        self.verifyAllDirections(newPos, stack)

    def directions(self, position):
        d = {}

        # programação defensiva
        if self.board.positionExists(Position(position.row - 1, position.column + 1)):
            d["ne"] = Position(position.row - 1, position.column + 1)

        if self.board.positionExists(Position(position.row - 1, position.column - 1)):
            d["nw"] = Position(position.row - 1, position.column - 1)

        if self.board.positionExists(Position(position.row + 1, position.column + 1)):
            d["se"] = Position(position.row + 1, position.column + 1)

        if self.board.positionExists(Position(position.row + 1, position.column - 1)):
            d["sw"] = Position(position.row + 1, position.column - 1)

        return d

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
        self.placeNewPiece("d", 8, CheckersPiece(self.board, "white"))
        self.placeNewPiece("c", 7, CheckersPiece(self.board, "black"))
        self.placeNewPiece("e", 7, CheckersPiece(self.board, "black"))
        self.placeNewPiece("g", 5, CheckersPiece(self.board, "black"))
        self.placeNewPiece("g", 3, CheckersPiece(self.board, "black"))
        self.placeNewPiece("c", 5, CheckersPiece(self.board, "black"))
