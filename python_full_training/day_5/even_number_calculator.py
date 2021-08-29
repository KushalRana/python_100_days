# This code simply adds value of even numbers from 1 to 100

total = 0
for num in range(0, 101, 2):
    total += num
print(f"Total sum is {total}")
