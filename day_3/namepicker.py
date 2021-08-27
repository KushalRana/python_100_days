# This program will pick a random name from entered list of people

import random


names_strings = input(
    "Enter names to be included in random selection each seperated by comma. "
)
names = names_strings.split(", ")
print(f"Person to pay bills is {names[random.randint(0, len(names))]}")
