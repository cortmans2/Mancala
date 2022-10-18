import Gameboard
import Human
import Player


class Game:
    def __init__(self, playerToMove, player0, player1):
        self.playerToMove = playerToMove
        self.gameboard = Gameboard()
        self.player0 = Player(playerName, 0, gameboard)
        self.player1 = Player(playerName, 1, gameboard)


    def getPlayerToMove(self):
        return self.playerToMove

    def getBoard(self):
        return self.board

    def getPlayer0(self):
        return self.player0

    def getPlayer1(self):
        return self.player1

    def startTurn(self):
        Move(index, direction, playerToMove)
        IsGameOver()
