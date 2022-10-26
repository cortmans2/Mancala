from Player import *
from Human import *
from Game import *
from Gameboard import *

# printing instructions and first board
print("The game will ask you to enter in an Index to move, \nthis number corresponds to the pits on the board, \n"
      "1 being the pit furthest to the left ignoring the store \n6 will be the furthest to the right ignoring the store \n"
      "You will then be asked to enter direction, \n1 for clockwise and -1 for counterclockwise \n"
      "After you enter in these to inputs the new board will print \nand the next players turn will start and the proccess will repete"
      "\nWhoever has the most pits in their store at the end of the game wins! \nHave Fun!")
print(str(Gameboard()))

#running the game
game1 = Game()
game1.startGame()