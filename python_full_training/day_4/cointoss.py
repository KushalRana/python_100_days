# This is a cointoss program that will make a random cointoss

from random import random


import random

toss = random.randint(0, 1)

if toss == 0:
    print("It is Heads")

elif toss == 1:
    print("It is tails")
