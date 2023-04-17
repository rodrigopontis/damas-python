

class CheckersUI:

    def inputMovement(self):
        str = input("Movimentos possiveis de a1 a h8: ")
        print(str)

    def printPiece(self, piece):
        strPiece = ""
        if (piece == None):
            strPiece += "-"
        else:
            if (piece.color == "white"):
                strPiece += "W"
            else:
                strPiece += "B"

        return strPiece + " "

    def printBoard(self, pieces):
        strLines = ""
        for i in range(len(pieces)):
            strLines += str(i+1) + " "
            for j in pieces[i]:
                strLines += self.printPiece(j)
            print(strLines)
            strLines = ""

        strLines += " "
        for i in range(8):
            strLines += chr(i + 97) + " "

        print(" " + strLines)
