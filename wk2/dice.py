# Random dice
import random               # random number

class Dice:
    def __init__(self, sides):      # Specify number of sides by sides=6, specifying 6 sides for the dice. Create dice2 = Dice() and Python will auto use 6 sided die
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)

dice = Dice(6)                          # change number in Dice() for sides of dice
print(dice.roll())
# Roll in a range of attempts
for roll in range(20):                 # change number in range() for number of throws
    print(dice.roll())

# dice2 = Dice()
# print(dice2.roll())