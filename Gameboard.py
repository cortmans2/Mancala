import numpy


class Gameboard:

    def __init__(self):

        self.gameboard = [[0, 4, 4, 4, 4, 4, 4, None],
                         [None, 4, 4, 4, 4, 4, 4, 0]]

    def __str__(self):

        return str(self.gameboard[0]) + "\n" + str(self.gameboard[1])

    def sow(self, index, direction, player):

        count = self.gameboard[player][index]
        current = [player, index]
        self.gameboard[player][index] = 0

        for i in range(count):

            if player == 0:
                if direction == 0:
                    if current[1] < 0:
                        current = (1, 0)
                        direction = 1
                    current[1] -= 1
                else:
                    if current[1] > 7:
                        current = (1, 7)
                        direction = 0
                    current[1] += 1
            else:
                if direction == 0:
                    if current[1] < 0:
                        current = (0, 0)
                        direction = 1
                    current[1] -= 1
                else:
                    if current[1] > 7:
                        current = (0, 7)
                        direction = 0
                    current[1] += 1

            if self.gameboard[current[0]][current[1]] is None:
                if current[0] == 0:
                    current[1] += 1
                else:
                    current[1] -= 1

            self.gameboard[current[0]][current[1]] += 1
            print(str(self.gameboard[0]) + "\n" + str(self.gameboard[1]))


g1 = Gameboard()
print(g1)
g1.sow(3, 1, 1)
g1.sow(4, 1, 1)