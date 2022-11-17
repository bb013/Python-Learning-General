# Python3 code to demonstrate working of
# Longest String in list
# using loop
  
# initialize list

# from wordlist import words the list I imported, it'll differ depending on your needs
test_list = words
  
# printing original list 
#print("The original list : " + str(test_list))

# Longest String in list
# using loop
max_len = -1
for ele in test_list:
    if len(ele) > max_len:
        max_len = len(ele)
        res = ele
  
# printing result
print("Maximum length string is : " + res)
print(f'Longest word lenght is: {max_len} ')