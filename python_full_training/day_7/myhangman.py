# This is a simplified program imitate a hangman game
import random

words = ["alpha", "beta", "charlie", "delta", "echo", "falcon"]
health = ["zero", "One", "Two", "Three", "four", "five", "six"]
hp = 7
output = []
random_list = list(random.choice(words))
for num in range(0, len(random_list)):
    # output[num] = output["_"]
    output.append("_ ")
while hp > 0:

    guess = input("entes your guess >>>  ").lower()
    if guess not in random_list:
        print("wrong guess")
        print("".join(output))
        hp -= 1
        print(f"remaining health = {health[hp]}")
        if not hp > 0:
            print("you lost")

    elif guess in random_list:
        n = 0
        for char in random_list:
            if guess == char:
                output[n] = char

            n += 1
        print("".join(output))
        print(f"remaining health = {health[hp-1]}")
        if "_ " not in output:
            print("you win")
            hp = 0
