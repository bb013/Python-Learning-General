#Write your code below this line 👇
def prime_checker(number):
    antiprime = None
    for each_number in range(2,number):
        if number % each_number == 0:
            antiprime = True

    if antiprime == True:
        print("It's not a prime number.")        
    else:
        print("It's a prime number.")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)