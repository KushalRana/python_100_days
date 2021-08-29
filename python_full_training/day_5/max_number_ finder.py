# This program helps to find highest number among given numbers


student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

max = 0

for number in student_scores:
    if number > max:
        max = number

print(f"Max number is {max} ")
