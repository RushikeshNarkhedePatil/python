"""
Dice Game
"""
import random
print('Welcome to Dice Roll Game'.center(50,'*'))
player1 = 0
player2= 0
for i in range(10):
     player1val= random.randint(1, 6)
     player2val = random.randint(1, 6)
     print("Player 1 rolled: ", player1val)
     print("Player 2 rolled: ", player2val)
     if player1val > player2val:
         print("player 1 wins.")
         player1 = player1 + 1 
     elif player2val > player1val:
         print("player 2 wins")
         player2 = player2 + 1
     else:
         print("It's a draw")
         input("Press enter to continue.") 
         print("Game Over".center(50,"*"))
         print("Player 1 score:", player1)
         print("Player 2 score:", player2)