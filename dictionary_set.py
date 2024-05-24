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