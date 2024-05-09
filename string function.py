

'''
String Functions
str = "I am a coder."
str.endswith("er.") #returns true if string ends with substr

str.capitalize() #capitalizes 1st char

str.replace old, new) #replaces all occurrences of old with new

str.find(word) #returns 1st index of 1st occurrence

str.count("am") #counts the occurrence of substr in string
'''

str = "I am a coder."
str.endswith("er.") #returns true if string ends with substr

str = "i am studying python"
print(str.endswith("python"))



str.capitalize() #capitalizes 1st char

str = "i am studying python"
print(str.capitalize())  # system create new string to print out 
print(str)  # this print function not capitalize first letter again becaue we are not changing original string


str = "i am studying python"
str=str.capitalize()
print(str)




#str.replace old, new) #replaces all occurrences of old with new

str = "i am studying python online"
print(str.replace("python","javascript"))


#str.find(word) #returns 1st index of 1st occurrence

str = "i am studying python online"
print(str.find("s"))


str = "i am studying python online"
print(str.find("not available")) # print -1 if value not find




#str.count("am") #counts the occurrence of substr in string
str = "i am studying python online"
print(str.count("online"))





