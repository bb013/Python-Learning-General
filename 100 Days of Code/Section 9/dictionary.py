# programming_dictionary = {
#   "Bug": "An error in a program that prevents the program from running as expected.",
#   "Function": "A piece of code that you can easily call over and over again.",
#   "Loop": "The Action of doing something over and over again.",
# }

#Retrieving items from a dictionary.
# print(programming_dictionary["Bug"])

programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.",
  "Function": "A piece of code that you can easily call over and over again.",
}

#Adding new items to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."

#Creat an empty dictionary
empty_dictionary = {}

# # Wipe an existing dictionary
# programming_dictionary = {}

# print(programming_dictionary)

#Edit an itme in a dictionary
programming_dictionary['Bug'] = "A moth in your computer."

#Loop through a dictionary
for key in programming_dictionary:
  print(key)
  print(programming_dictionary[key])