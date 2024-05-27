'''
dictionary are used to store data values in key:value pairs

they areunordered, mutable(changeble) & dontt allow duplicate keys

dict = {

"name" : "Govind"
"cgpa" :9.5,
"marks" : [98,97,99]

dict ["name"],dict["cgpa"],dict["marks"]

dict["key"] ="value  #to assign or add new

}

'''


info = {

"key" : "value",
"name" : "Govind Technologies",
"learning" : "coding",

}

print(info)

##########################

info = {

"name" : "Govind Technologies",
"Subject" : ["Python", "ML" ," AI"],
"Topic" :(),
"age" : 35,
"is_adult" :True,
"marks" : 99,

}

print(info)


##################################################
#check data type
info = {

"name" : "Govind Technologies",
"Subject" : ["Python", "ML" ," AI"],
"Topic" :(),
"age" : 35,
"is_adult" :True,
"marks" : 99,

}

print(info)
print(type(info))


################################
# to access perticular value
dict = {

"name" : "Govind Technologies",
"Subject" : ["Python", "ML" ," AI"],
"Topic" :(),
"age" : 35,
"is_adult" :True,
"marks" : 99,

}

print(dict["name"])


###################################


dict = {

"name" : "Govind Technologies",
"Subject" : ["Python", "ML" ," AI"],
"Topic" :(),
"age" : 35,
"is_adult" :True,
"marks" : 99,

}

print(dict["name"])

print(dict["age"])

################################

#modifiy existing data and print that one

dict = {

"name" : "Govind Technologies",
"Subject" : ["Python", "ML" ," AI"],
"Topic" :(),
"age" : 35,
"is_adult" :True,
"marks" : 99,

}

dict["name"] = "Khandare Corporation"

print(dict)


##############

dict = {

"name" : "Govind Technologies",
"Subject" : ["Python", "ML" ," AI"],
"Topic" :(),
"age" : 35,
"is_adult" :True,
"marks" : 99,

}

dict["name"] = "Khandare Corporation"



print(dict["name"])


######

# we can print null dictionary

dict = {

"name" : "Govind Technologies",
"Subject" : ["Python", "ML" ," AI"],
"Topic" :(),
"age" : 35,
"is_adult" :True,
"marks" : 99,

}

dict["name"] = "Khandare Corporation"

null_dict = {}


print(null_dict)

print(dict["name"])


##################################


# nested dictionaries 


student = {

"name" : "Govind Khandare",
"subjects" : {
"math" : 88,
"chem" :98,
"phy" :88,


}

}

# nested dictionary

print(student)


#print perticular data

student = {

"name" : "Govind Khandare",
"subjects" : {
"math" : 88,
"chem" :98,
"phy" :88,


}

}

# nested dictionary

print(student["subjects"])

# Print specfic object
student = {

"name" : "Govind Khandare",
"subjects" : {
"math" : 88,
"chem" :98,
"phy" :88,


}

}

# nested dictionary

print(student["subjects"]["math"]) # we made changes in print statement

#

'''
Dictionary methods

myDict.keys() #return all keys


myDict.values() #return all values

myDict.items () # return all (key , val) pair as tuples

mydict.get("key") # return the key according to value

mydict.update(newDict) # insert the specfied items to the dictionary





'''

# keys will return

#myDict.keys() #return all keys

student = {

"name" : "Govind Khandare",
"subjects" : {
"math" : 88,
"chem" :98,
"phy" :88,


}

}

print(student.keys())


#convert in list

student = {

"name" : "Govind Khandare",
"subjects" : {
"math" : 88,
"chem" :98,
"phy" :88,


}

}

print(student.keys())

print(list(student.keys()))


########
# check list length

student = {

"name" : "Govind Khandare",
"subjects" : {
"math" : 88,
"chem" :98,
"phy" :88,


}

}

print(student.keys())

print(len(student.keys()))

#########

#myDict.values() #return all values

student = {

"name" : "Govind Khandare",
"subjects" : {
"math" : 88,
"chem" :98,
"phy" :88,


}

}

print((student.values()))


#myDict.items () # return all (key , val) pair as tuples


student = {

"name" : "Govind Khandare",
"subjects" : {
"math" : 88,
"chem" :98,
"phy" :88,


}

}

print((student.items()))

#print in list
student = {

"name" : "Govind Khandare",
"subjects" : {
"math" : 88,
"chem" :98,
"phy" :88,


}

}

print(list(student.items()))

# another solution

student = {

"name" : "Govind Khandare",
"subjects" : {
"math" : 88,
"chem" :98,
"phy" :88,


}

}

pairs=(list(student.items()))

print(pairs[1])

#mydict.get("key") # return the key according to value


student = {

"name" : "Govind Khandare",
"subjects" : {
"math" : 88,
"chem" :98,
"phy" :88,
}
}

#print(student["name"]) # error
#print(student.get("name")) # no error


#print(student["name2"]) # error
print(student.get("name2")) # no error will retunn none



#mydict.update(newDict) # insert the specfied items to the dictionary


student = {

"name" : "Govind Khandare",
"subjects" : {
"math" : 88,
"chem" :98,
"phy" :88,
}
}

student.update({"City" : "Pune"})

print(student)


#another solution with new dict

student = {

"name" : "Govind Khandare",
"subjects" : {
"math" : 88,
"chem" :98,
"phy" :88,
}
}
new_dict = {"city" : "Pune" , "age " : "16"}
student.update(new_dict)

print(student)


#Set in Python.......................................Set in python

'''
set is the collection of the unordered items.
Each element in the set must be unique & immutable

nums = {1,2,3,4}
set2 = {1,2,2,2}
# repeated elements stored only once , so it resolved to {1,2}

null_set = set() # empty set syntax


'''

collection = {1,2,3,4}

print(collection)
print(type(collection))


# duplicate item will not execute system will ignore duplicate values

collection = {1,2,3,4,4,2,4,3, "Hello" , "Govind","Govind","Hello"}

print(collection)
print(type(collection))


# Len also ignore duplicate items

collection = {1,2,3,4,4,2,4,3, "Hello" , "Govind","Govind","Hello"}

print(collection)
print(len(collection))


#Empty set

collection = set()
print(type(collection))

######### Set Method

'''
Note : 
sets -> Mutable

set -> Elements -> immutable

# Below are the methods

set.add(el)  # add elements

set.remove (el) # Remove the elem an

set.clear() # empties the set

set.pop() # remove a random value

set.union(set2) # combine both set values & retuns new

set.intersection(set2) # combine common values & returns new


'''

#set.add(el)  # add elements and ignore duplicate values




collection = set()

collection.add(1)
collection.add(2)
collection.add(2)

print(collection)



#Another example
collection = set()
collection.add(1)
collection.add(2)
collection.add(2)

collection.add("Govind")
collection.add((1,2,4))
print(collection)

# set.remove (el) # Remove the elem an



collection = set()


collection.add(1)
collection.add(2)
collection.add(2)

collection.remove(1)

print(collection)


#set.clear() # empties the set


collection = set()


collection.add(1)
collection.add(2)
collection.add(2)

collection.add("Govind")
collection.add((1,2,4))

collection.clear()

print(len(collection))


#set.pop() # remove a random value


collection = {"Hello" , "Govind Tech", "World " , "Codind" , "Python"}

print(collection.pop())

#another example
collection = {"Hello" , "Govind Tech", "World " , "Codind" , "Python"}

print(collection.pop())

print(collection.pop())


#set.union(set2) # combine both set values & retuns new


set1 = {1,2,3}
set2 = {3,4,5}

print(set1.union(set2))  # {1,2,3,4,5}  Duplicate values ignored



#set.intersection(set2) # combine common values & returns new


set1 = {1,2,3}
set2 = {3,4,5}

print(set1.intersection(set2))

#Practice Questions


# store following word meaning in a python dictionary:

'''
 table : "a piece of furniture " , "list of facts & figurs"

 cat : "a small animal"

'''

# Solution

dict = {


    "cat": "a small animal",
    "table" : ["a piece of furniture" , "list of facts & figures"]
}

print(dict)



#You are given a list of subject for students . Assume one classroom is required for 1 subject. How many classroom are needed by all students.

# "python" , "java" , "C++", "javascripts" ,
#"java" , "python","java", "C++" , "C"


# Solution

subject = {

 "python" , "java" , "C++", "javascripts" ,
"java" , "python","java", "C++" , "C"

}


print(len(subject))


# Write a programe to enter marks of 3 subjects from the user and store them in a dictionary . start with an empty dictionary
# and add one by one . Use subjects name as key & marks as value.


#Solution

marks = {}

a = (input("Enter phy marks"))
marks.update({"phy": a})


a = (input("Enter math marks"))
marks.update({"math": a})


a = (input("Enter phy marks"))
marks.update({"chem": a})



print(marks)


'''
figure out a way to store 9 and 9.0 as seprate values in the set.
(you can take help of built-in data types)
'''


#Solution

values = {9,"9.0"}  # use as string to print value
print(values)


# Another solution

values = {

("float" , 9.0),
("int", 9 ),
}
print(values)

