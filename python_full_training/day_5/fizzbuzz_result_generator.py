# This program calculates the result of fizzbuzz kid game from 1 to 100


for num in range(1, 101):
    if num % 5 == 0 and num % 3 == 0:
        print("fizzbuzz")
    elif num % 3 == 0:
        print("fizz")
    elif num % 5 == 0:
        print("buzz")
    else:
        print(num)
