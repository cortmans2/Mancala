import numpy


class Gameboard:

    def __init__(self):

        self.gameboard = [[0, 4, 4, 4, 4, 4, 4, None],
                         [None, 4, 4, 4, 4, 4, 4, 0]]

    def __str__(self):

        return str(self.gameboard[0]) + "\n" + str(self.gameboard[1])

    def sow(self, index, direction, player):

        current = count = self.gameboard[player][index]
        self.gameboard[player][index] = 0

        for i in range(count):

            if player == 0:
                if direction == 0:
                    if current < 0:
                        current = self.gameboard[1][0]
                        direction = 1
                    current -= 1
                else:
                    if current > 7:
                        current = self.gameboard[1][7]
                        direction = 0
                    current += 1
            else:
                if direction == 0:
                    if current < 0:
                        current = self.gameboard[0][0]
                        direction = 1
                    current -= 1
                else:
                    if current > 7:
                        current = self.gameboard[0][7]
                        direction = 0
                    current += 1

        self.gameboard[current] += 1

g1 = Gameboard()
print(g1)
g1.sow(3, 1, 1)