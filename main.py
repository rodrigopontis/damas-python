from checkersEntities import CheckersMatch
from ui import CheckersUI


def __main__():
    newMatch = CheckersMatch()

    interface = CheckersUI()
    interface.printBoard(newMatch.board.getPieces())


if (__name__ == '__main__'):
    __main__()
