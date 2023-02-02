student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for each_student in student_scores:
    number_to_convert = student_scores[each_student]
    if number_to_convert > 90:
        student_grades[each_student] = "Outstanding"
    elif number_to_convert > 80:
        student_grades[each_student] = "Exceeds Expectations"
    elif number_to_convert > 70:
        student_grades[each_student] = "Acceptable"   
    else:
        student_grades[each_student] = "Fail"   

# 🚨 Don't change the code below 
print(student_grades)