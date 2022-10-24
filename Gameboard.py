import numpy


class Gameboard:

    def __init__(self):

        self.gameboard = [[0, 4, 4, 4, 4, 4, 4, None],
                         [None, 4, 4, 4, 4, 4, 4, 0]]

    def __str__(self):

        return str(self.gameboard[0]) + "\n" + str(self.gameboard[1])

    def sow(self, index, direction, player, playerCallbackReference):

        #print(index, direction, player)
        count = self.gameboard[(int)(player)][(int)(index)]
        current = [(int)(player), (int)(index)]
        self.gameboard[(int)(player)][(int)(index)] = 0
        for i in range(count):

            if player == 0:
                if direction == -1:
                    if current[1] < 0:
                        current = [1, 0]
                        direction = 1
                    else:
                        current[1] -= 1
                else:
                    if current[1] > 6:
                        current = [1, 7]
                        direction = -1
                    else:
                        current[1] += 1
            else:
                if direction == -1:
                    if current[1] < 0:
                        current = [0, 0]
                        direction = 1
                    else:
                        current[1] -= 1
                else:
                    if current[1] > 6:
                        current = [0, 7]
                        direction = -1
                    else:
                        current[1] += 1

            if self.gameboard[current[0]][current[1]] is None:
                if current[0] == 0 and direction == 1:
                    current[1] = 0
                elif current[0] == 0 and direction == -1:
                    current[1] = 6
                elif current[0] == 1 and direction == 1:
                    current[1] = 1
                else:
                    current[0] = 7

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
