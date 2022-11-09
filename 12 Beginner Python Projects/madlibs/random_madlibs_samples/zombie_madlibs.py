# a zombie themed madlibs
def madlib():
    print("A zombie themed madlibs!")
    adj=input("Adjective: ")
    verb1=input("Verb: ").title()
    verb2=input("Verb: ")
    famous_person=input("Famous Person Name: ").title()
    
    madlib = f"{famous_person} has become a {adj} zombie! {verb1} is your only chance at survival! {famous_person} doesn't like {verb1} and will go into a fit of {verb2} if you are {verb1}."
    print(madlib)
    quit()