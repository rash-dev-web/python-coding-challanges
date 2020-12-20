# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


# Write your code below this row 👇
avg_height = 0
count = 0
for st in student_heights:
    avg_height += st
    count += 1

print(round(avg_height / count))
