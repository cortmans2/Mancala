class Player:

    def __init__(self, playerName, playerNum, gameboard): # initializes the players name and num
        self.name = playerName
        self.num = playerNum
        self.gameboardReference = gameboard

    def Move(self): # doesn't have to actually do anything, will always be overwritten in sublasses
        return None
    