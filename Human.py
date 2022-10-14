from Player import *
class Human(Player):

    def __init__(self, playerName, playerNum, gameboard): # just calls the super constructor
        super().__init__(playerName, playerNum, gameboard)

    def Move(self):
        try:
            indexToMove = 0
            while int(indexToMove) < 1 or int(indexToMove) > 6:
                indexToMove = (input("Index To Move (1 - 6) : "))
        except:
            print("Invalid Input. Index to move must be in the range of 1 - 6")
            self.Move()

        try:
            direction = 0
            while int(direction) != 1 and int(direction) != -1:
                direction = (input("Direction (-1 or 1) : "))
        except:
            print("Invalid Input. Direction must be -1 or 1")
            self.Move()

        super().gameboardReference.Sow(indexToMove, direction, self)
