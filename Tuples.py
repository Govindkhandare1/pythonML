tup = (2,1,3,1)
print(type(tup))
print(tup[3])



# we can create empty typle

tup = ()
print(tup)
print(type(tup))


tup = (5,)  #always use comma for single values if not then python cosider as a int.
print(tup)
print(type(tup))


#slicing also possible in tuple

tup =(1,2,4,5,6)

print(tup[1:3])


#Tuple Method

'''
tup.index(el) # Return index of first occurrence tup.index(1)is 1

tup.count(el) #counts total occurrences tup.count(1) is 2
'''
# tup.index(el) # Return index of first occurrence tup.index(1)is 1


tup =(1,2,4,5,6)

print(tup.index(6))


#tup.count(el) #counts total occurrences tup.count(1) is 2


tup =(1,2,4,5,6,5,7,8,9,5,5,5,5,5,5,5)

print(tup.count(5))



#practive questions

#write a program ask the user to enter names of their 3 favourite movies and store them in a list




movies = []

mov1 =input("Enter 1 st Movie name:")
mov2 = input("Enter 2nd movie name:")
mov3 = input("Enter 3 rd movie name:")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)

#Another soultion


movies = []

mov =input("Enter 1 st Movie name:")
movies.append(mov)
mov = input("Enter 2nd movie name:")
movies.append(mov)
mov = input("Enter 3 rd movie name:")
movies.append(mov)


print(movies)


# Another Solution


movies = []

movies.append(input("Enter 1 st Movie name:"))
movies.append(input("Enter 2nd movie name:"))
movies.append(input("Enter 3 rd movie name:"))

print(movies)


# write a programee to check if a list contains a palindrome of element . (Hint : use copy() method)

list1 =[1,2,1]
list2 =[1,2,3]

copy_list1 =list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")
else:
    print("Not Palindrome ")

#
#Write a programe to count the number of student with the "A" grade in the following tuple.
    
grade = ("C","D","A","A","B","B","A")
print(grade.count("A"))

#store the above values in a list and sort them "A" to "D"

    
grade = ["C","D","A","A","B","B","A"]
grade.sort()
print(grade)