import Gameboard
import Human
import Player


class Game:
    def __init__(self, playerToMove, board, player0, player1):
        self.playerToMove = playerToMove
        self.board = board
        self.player0 = player0
        self.player1 = player1
        self.Gameboard = Gameboard()
        self.player0 = Player()
        self.player1 = Player()


    def getPlayerToMove(self):
        return self.playerToMove

    def getBoard(self):
        return self.board

    def getPlayer0(self):
        return self.player0

    def getPlayer1(self):
        return self.player1

    def startTurn():
        Move(index, direction, playerToMove)
        IsGameOver()
