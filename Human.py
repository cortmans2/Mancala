from Player import *
class Human(Player):

    def __init__(self, playerName, playerNum, gameboard): # calls the super constructor
        super().__init__(playerName, playerNum, gameboard)

    def Move(self): # Gets which pit to move and which direction to move from player
                    # and then calls sow(in Gameboard) which acually moves them
        # Index Input

        indexToMove = 0
        direction = 0

        try:  # If invalid input, calls method again
            indexToMove = 0
            while int(indexToMove) < 1 or int(indexToMove) > 6:  # only runs if indexToMove is invalid
                indexToMove = (input("<Player" + ("1" if self.num == 0 else "2") + "> Index To Move (1 - 6) : "))
        except:
            print("Invalid Input. Index to move must be in the range of 1 - 6")
            self.Move()
            return

        if (self.gameboardReference.gameboard[int(self.num)][int(indexToMove)] == 0):
            # Checks if pit selected has seeds in it
            print("Invalid Input. You must select a pit with seeds in it")
            self.Move()
            return

        # Direction Input
        try:   # If invalid input, calls method again
            direction = 0
            while int(direction) != 1 and int(direction) != -1:  # only runs if direction is invalid
                direction = (input("<Player" + ("1" if self.num == 0 else "2") + "> Direction (-1 or 1) : "))
        except:
            print("Invalid Input. Direction must be -1 or 1")
            self.Move()
            return

        self.gameboardReference.sow(int(indexToMove), int(direction), int(self.num), self)

