# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = "Catherine Zeta-Jones" # input("What is your name? \n")
name2 = "Michael Douglas" #input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
compined_name = (name1 + name2).lower()
letters_true_count = 0
letters_true_count += compined_name.count("t")
letters_true_count += compined_name.count("r")
letters_true_count += compined_name.count("u")
letters_true_count += compined_name.count("e")

letters_love_count = 0
letters_love_count += compined_name.count("l")
letters_love_count += compined_name.count("o")
letters_love_count += compined_name.count("v")
letters_love_count += compined_name.count("e")

score = int(str(letters_true_count)+str(letters_love_count))
if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")