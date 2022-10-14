from Player import *

class Computer(Player):

    def __init__(self, playerName, playerNum, gameboard):
        super().__init__(playerName, playerNum, gameboard)

    def Move(self):
        indexToMove = DecideIndex()
        direction = DecideDirection()
        super().gameboardReference.Sow(indexToMove, direction, self)

