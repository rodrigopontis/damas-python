from checkersEntities import CheckersMatch
from ui import CheckersUI


def __main__():
    newMatch = CheckersMatch()
    piecesInMatch = newMatch.board.getPieces()

    interface = CheckersUI()
    interface.printBoard(piecesInMatch)
    source = input("Select a source: ")

    # TODO: após selecionar uma peça devera
    # ser chamado o metodo que atualiza os
    # movimentos possiveis da peça
    # mas o metodo fica no checkersmatch
    possibleMoves = newMatch.possibleMoves(source)
    interface.printPossibleMoves(piecesInMatch, possibleMoves)

    # target = input("Select a target: ")

    # newMatch.makingACheckersMovement(source, target)


if __name__ == "__main__":
    __main__()
