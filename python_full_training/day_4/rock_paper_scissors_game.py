import random

ROCK = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

PAPER = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

SCISSOR = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

set = [ROCK, PAPER, SCISSOR]

player1_score = 0
player2_score = 0
print("Welcome to rock paper scissor game !!!\---------------------------------------")

player1 = input("Enter first player's name: ")
print("---------------------------------------")
player2 = input("Enter second player's name: ")
print("---------------------------------------")
print(f"{player1} vs {player2}")
print("---------------------------------------")

for round in range(10):
    if round % 2 == 0:
        user = player1
    else:
        user = player2
    print("---------------------------------------")
    print(
        f"Score is:\n---------------------------------------\n{player1}:{player1_score}\n{player2}:{player2_score}"
    )
    print(
        f"---------------------------------------\nRound{round + 1}:\n---------------------------------------\n{user}'s turn\n---------------------------------------"
    )
    your_choice = int(input("Enter 0 for rock, 1 for paper, 2 for scissor: "))

    if your_choice > 2:
        print("Invalid choice !!!\nLost by default!!!")
    else:
        pc_choice = random.randint(0, 2)

        print(
            f"You played:\n{set[your_choice]}\n---------------------------------------\nComputer played:\n{set[pc_choice]}\n---------------------------------------"
        )
        if your_choice == pc_choice:
            print("It's a draw!!")
        elif your_choice == 2 and pc_choice == 0:
            print(f"{user} lost!!!")

        elif your_choice == 0 and pc_choice == 2 or your_choice > pc_choice:
            print(f"{user} won!!!")
            if player1 == user:
                player1_score += 1
            else:
                player2_score += 1
        else:
            print(f"{user} lost!!!")

if player1_score == player2_score:
    print("It's a Draw!!")
elif player1_score > player2_score:
    print(
        f"---------------------------------------\n---------------------------------------\nFinal winner is {player1}\n---------------------------------------\n---------------------------------------"
    )
else:
    print(
        f"---------------------------------------\n---------------------------------------\nFinal winner is {player2}\n---------------------------------------\n---------------------------------------"
    )
