# a hunger games themed madlibs
def madlib():
    print("A hunger games themed madlibs!")
    adj=input("Adjective: ")
    verb1=input("Verb: ")
    verb2=input("Verb: ")
    famous_person=input("Famous Person Name: ").title()
    famous_person2=input("Another Famous Person's Name: ").title()
    
    madlib = f"{famous_person} and {famous_person2} have been thrown into the hungergames! But its okay because {famous_person} is {adj} and {famous_person2} is good at {verb1} and {verb2}."
    print(madlib)
    quit()