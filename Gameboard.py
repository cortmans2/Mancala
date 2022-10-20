import numpy


class Gameboard:

    def __init__(self):

        self.gameboard = [[0, 4, 4, 4, 4, 4, 4, None],
                         [None, 4, 4, 4, 4, 4, 4, 0]]

    def __str__(self):

        return str(self.gameboard[0]) + "\n" + str(self.gameboard[1])

    def sow(self, index, direction, player):

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
                    current[1] = 7

            self.gameboard[current[0]][current[1]] += 1
            print(str(self.gameboard[0]) + "\n" + str(self.gameboard[1]) + "\n")

    def isGameOver(self):
        return -1

#g1 = Gameboard()
#print(g1)
#g1.sow(6, -1, 0)
