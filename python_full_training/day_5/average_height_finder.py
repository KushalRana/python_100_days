# This is a simple project to calculate average of given numbers


student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total = 0
divider = 0

for num in student_heights:
    total += num
    divider += 1

average = total / divider

print(f"Average value of given numbers: {round(average)}")
