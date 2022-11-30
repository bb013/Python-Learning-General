# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = round(float(weight) / float(height) **2)
if bmi <= 18.5:
    statement = "you are underweight"
elif bmi <= 25:
    statement = "you have a normal weight"
elif bmi <= 30:
    statement = "you are slightly overweight"
elif bmi <= 35:
    statement = "you are obese"
elif bmi > 35:
    statement = "you are clinically obese"
print(f"Your BMI is {bmi}, {statement}.")


# "Your BMI is 18, you are underweight."
# "Your BMI is 22, you have a normal weight."
# "Your BMI is 28, you are slightly overweight."
# "Your BMI is 33, you are obese."
# "Your BMI is 40, you are clinically obese."

# print(bmi)
# It should tell them the interpretation of their BMI based on the BMI value.

#     Under 18.5 they are underweight
#     Over 18.5 but below 25 they have a normal weight
#     Over 25 but below 30 they are slightly overweight
#     Over 30 but below 35 they are obese
#     Above 35 they are clinically obese.
