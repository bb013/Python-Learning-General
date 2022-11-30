print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("You can ride the roller coaster")
    age = int(input("What's your age? "))
    if age < 12:
        print("Child tickets are $12")
        price = 5
    elif (age >= 12) and (age <= 18):
        print("Youth tickets are $12")
        price = 7
    elif age > 18:
        print("Adult tickets are $12")
        price = 12
    photo = input("Do you want a photo? Yes or No? ").lower()
    if photo == "yes":
        price += 3
        price = "{:.2f}".format(price)
    print(f"Your total is ${price}")
else:
  print("Sorry you are to short to safely ride the coaster")