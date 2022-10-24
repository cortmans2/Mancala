from Gameboard import *
from Human import *
from Player import *


class Game:
    def __init__(self):
        self.gameboard = Gameboard()
        self.player0 = Human("placeholder1", 0, self.gameboard)
        self.player1 = Human("placeholder2", 1, self.gameboard)
        self.playerToMove = self.player0


    def getPlayerToMove(self):
        return self.playerToMove

    def getBoard(self):
        return self.gameboard

    def getPlayer0(self):
        return self.player0

    def getPlayer1(self):
        return self.player1

    def startGame(self):  # Starts game and does not stop until the game is over
        print(self.gameboard.isGameOver())
        while (self.gameboard.isGameOver() == -1):  # Runs until game is over
            self.playerToMove.Move()
            # reverses which player will move next round
            self.playerToMove = self.player1 if self.playerToMove.num == 0 else self.player0  # switches players turn
            #print("playerToMove: " + (str)(self.playerToMove.num))
        print("The Game Is Over")