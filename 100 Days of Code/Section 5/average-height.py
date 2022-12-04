# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
added_heights = 0
number_of_heights = 0
for each_student_height in student_heights:
    added_heights += each_student_height
    number_of_heights += 1
average_height = round(added_heights/number_of_heights)
print(average_height)