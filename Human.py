from Player import *
class Human(Player):

    def __init__(self, playerName, playerNum, gameboard): # just calls the super constructor
        super().__init__(playerName, playerNum, gameboard)

    def Move(self):
        # Index Input

        indexToMove = 0
        direction = 0

        try:
            indexToMove = 0
            while int(indexToMove) < 1 or int(indexToMove) > 6:
                indexToMove = (input("<Player" + ("1" if self.num == 0 else "2") + "> Index To Move (1 - 6) : "))
        except:
            print("Invalid Input. Index to move must be in the range of 1 - 6")
            self.Move()


        # Direction Input
        try:
            direction = 0
            while int(direction) != 1 and int(direction) != -1:
                direction = (input("<Player" + ("1" if self.num == 0 else "2") + "> Direction (-1 or 1) : "))
        except:
            print("Invalid Input. Direction must be -1 or 1")
            self.Move()

        self.gameboardReference.sow(indexToMove, direction, (int)(self.num))
