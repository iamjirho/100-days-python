from operator import*

student_heights = input("Input a list of student heights ").split() #string
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

sum = 0
for item in student_heights:
  sum = add(item, sum)

average = int(sum/len(student_heights) + 0.5)
print(average)


