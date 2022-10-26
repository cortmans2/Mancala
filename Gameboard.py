import numpy

class Gameboard:

    def __init__(self):

        self.gameboard = [[0, 4, 4, 4, 4, 4, 4, None],
                         [None, 4, 4, 4, 4, 4, 4, 0]]

    def __str__(self):

        return str(self.gameboard[0]) + "\n" + str(self.gameboard[1])

    def inWrongStore(self, current, direction, player):
        print("ran method")
        print("current = " + str(current))
        if player == 0 and current == [1, 7]:  # If player zero lands on player one's store, skip it
            if direction == 1:  # If approaching clockwise, set to the first hole in the top row
                current = [1, 6]
            else:  # If approaching counterclockwise, set to the first hole in the bottom row
                current = [0, 7]
        if player == 1 and current == [0, 0]:  # If player zero lands on player one's store, skip it
            print("store reached")
            if direction == 1:  # If approaching clockwise, set to the first hole in the top row
                current = [0, 1]
            else:  # If approaching counterclockwise, set to the first hole in the bottom row
                current = [1, 0]
        return current
    def sow(self, index, direction, player, playerCallbackReference):

        count = self.gameboard[(int)(player)][(int)(index)]
        current = [(int)(player), (int)(index)]
        self.gameboard[(int)(player)][(int)(index)] = 0
        for i in range(count):
            print("current = " + str(current) + " direction = " + str(direction))

            if direction == -1:  # Counterclockwise
                if current == [0, 0]:  # If the top left end is reached, set to the beginning of bottom row
                    current = [1, 0]
                elif current == [0, 7]:  # If the bottom right end is reached, set to top right
                    current = [1, 7]
                elif current[0] == 0:
                    current[1] -= 1
                elif current[0] == 1:
                    current[1] += 1
            else:  # Clockwise
                if current == [1, 0]:  # If the top right end is reached, set to the end of bottom row
                    current = [0, 1]
                elif current == [0, 7]:  # If the bottom left end is reached, set to top left
                    current = [1, 7]
                elif current[0] == 0:  # If the top right end is not reached, continue clockwise
                    current[1] += 1
                elif current[0] == 1:  # If the top right end is not reached, continue clockwise
                    current[1] -= 1

            print(str(current) + " Before add")

            current = self.inWrongStore(current, direction, player)

            if self.gameboard[current[0]][current[1]] is None:
                if current[0] == 0 and direction == 1:
                    current = [1, 7]
                elif current[0] == 0 and direction == -1:
                    current = [1, 0]
                elif current[0] == 1 and direction == 1:
                    current = [0, 0]
                else:
                    current = [1, 1]

            current = self.inWrongStore(current, direction, player)

            self.gameboard[current[0]][current[1]] += 1
            print(str(self.gameboard[0]) + "\n" + str(self.gameboard[1]) + "\n")

        # handle moving again, capturing
        if current[1] == 0 or current[1] == 7:
            print("MOVE AGAIN")
            playerCallbackReference.Move()


    def isGameOver(self):
        # get how many seeds are in each player's row (not store)
        player0RemainingSeeds = 0
        for i in range(1, 7):
            player0RemainingSeeds += self.gameboard[0][i]

        player1RemainingSeeds = 0
        for i in range(1, 7):
            player1RemainingSeeds += self.gameboard[1][i]

        #print(player0RemainingSeeds , ", " , player1RemainingSeeds)

        # return -1 if the game isn't over
        if int(player0RemainingSeeds) > 0 and int(player1RemainingSeeds) > 0:
            return -1
        # otherwise return whoever has more in their store
        self.gameboard[0][0] += player0RemainingSeeds
        self.gameboard[1][7] += player1RemainingSeeds
        if self.gameboard[0][0] > self.gameboard[1][7]:
            return 0
        else:
            return 1






#g1 = Gameboard()
#print(g1)
#g1.sow(6, -1, 0)
