class BoardException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class CheckersException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
