import numpy

class Gameboard:

    def __init__(self):

        self.gameboard = [[0, 4, 4, 4, 4, 4, 4, None],
                         [None, 4, 4, 4, 4, 4, 4, 0]]

    def __str__(self):

        return str(self.gameboard[0]) + "\n" + str(self.gameboard[1])

    def inWrongStore(self, current, direction, player):
        #print("ran method")
        #print("current = " + str(current))
        if player == 0 and current == [1, 7]:  # If player zero lands on player one's store, skip it
            if direction == 1:  # If approaching clockwise, set to the first hole in the top row
                current = [1, 6]
            else:  # If approaching counterclockwise, set to the first hole in the bottom row
                current = [0, 7]
        if player == 1 and current == [0, 0]:  # If player zero lands on player one's store, skip it
            #print("store reached")
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
            #print("current = " + str(current) + " direction = " + str(direction))

            if direction == -1:  # Counterclockwise
                if current == [0, 0]:  # If the top left end is reached, set to the beginning of bottom row
                    current = [1, 0]
                elif current == [1, 7]:  # If the bottom right end is reached, set to top right
                    current = [0, 7]
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

            #print(str(current) + " Before add")

            current = self.inWrongStore(current, direction, player)

            if self.gameboard[current[0]][current[1]] is None:
                #print("none")
                if current[0] == 0 and direction == 1:
                    current = [1, 7]
                elif current[0] == 0 and direction == -1:
                    current = [0, 6]
                elif current[0] == 1 and direction == 1:
                    current = [0, 0]
                else:
                    current = [1, 1]

            current = self.inWrongStore(current, direction, player)

            self.gameboard[current[0]][current[1]] += 1
            #print(str(self.gameboard[0]) + "\n" + str(self.gameboard[1]) + "\n")

        print(str(self.gameboard[0]) + "\n" + str(self.gameboard[1]) + "\n")

        # handle moving again
        if current[1] == 0 or current[1] == 7:
            if self.isGameOver() == -1:
                print("MOVE AGAIN")
                playerCallbackReference.Move()

        # handles capturing
        if player == 0 and current[0] == 0 and self.gameboard[0][current[1]] == 1 and self.gameboard[1][current[1]] != 0:
            seedsToCapture = self.gameboard[1][current[1]] + 1
            self.gameboard[0][current[1]] = 0
            self.gameboard[1][current[1]] = 0
            self.gameboard[0][0] += seedsToCapture
            print("CAPTURED", seedsToCapture, "SEEDS")
            print(str(self.gameboard[0]) + "\n" + str(self.gameboard[1]))
        if player == 1 and current[0] == 1 and self.gameboard[1][current[1]] == 1 and self.gameboard[0][current[1]] != 0:
            seedsToCapture = self.gameboard[0][current[1]] + 1
            self.gameboard[1][current[1]] = 0
            self.gameboard[0][current[1]] = 0
            self.gameboard[1][7] += seedsToCapture
            print("CAPTURED", seedsToCapture, "SEEDS")
            print(str(self.gameboard[0]) + "\n" + str(self.gameboard[1]))


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
        player0Total = self.gameboard[0][0] + player0RemainingSeeds
        player1Total = self.gameboard[1][7] + player1RemainingSeeds
        if player0Total > player1Total:
            return 0
        else:
            return 1

#g1 = Gameboard()
#print(g1)
#g1.sow(6, -1, 0)



# Alternative way of determining the next index to go to.
# To implement, just set 'current' inside of sow to getNextIndex()
def getNextIndex(self, player, dir, currentI):

    # should never be sent [1, 7]
    p1d1NextIndexArray = [[[0,1], [0, 2], [0,3], [0,4], [0,5], [0,6], [1,6], None],
                          [None, [0,0], [1,1], [1,2], [1,3], [1,4], [1,5], [1,6]]]
    # should never be sent [1, 7]
    p1dn1NextIndexArray = [[[1,1], [0, 0], [0,1], [0,2], [0,3], [0,4], [0,5], None],
                          [None, [1,2], [1,3], [1,4], [1,5], [1,6], [0,6], [0,6]]]
    # should never be sent [0,0]
    p2d1NextIndexArray = [[[1,1], [1, 1], [0,1], [0,2], [0,3], [0,4], [0,5], None],
                          [None, [1,2], [1,3], [1,4], [1,5], [1,6], [1,7], [0,6]]]
    # should never be sent [0,0]
    p2dn1NextIndexArray = [[[0,1], [0, 2], [0,3], [0,4], [0,5], [0,6], [1,7], None],
                          [None, [0,1], [1,1], [1,2], [1,3], [1,4], [1,5], [1,6]]]
    if player == 0 and dir == 1:
        return p1d1NextIndexArray[currentI]
    elif player == 0 and dir == -1:
        return p1dn1NextIndexArray[currentI]
    elif player == 1 and dir == 1:
        return p2d1NextIndexArray[currentI]
    elif player == 1 and dir == -1:
        return p2dn1NextIndexArray[currentI]

