import random
def roll():
    return random.randint(1, 6)
result = 0
while result != 6:
    result = roll()
    print("Result was:", result)

print("You got 6! Program stops.\n")
def roll(highest):
    return random.randint(1, highest)
number = int(input("How big do you want the dice to be? "))
result = 0
while result != number:
    result = roll(number)
    print("Result was:", result)

