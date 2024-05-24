
#Completed till 3 hour 27 min
#and started new chapter 3 List in python
marks =[12,132,34 ,45,56, 67]
print(marks)

print(type(marks))
print(len(marks))


student = ["Govind",88 ,24 ,"Pune"]
print(student[0])
student[0] = "Kanchan"
print(student)


#List slicing

'''
list_name[starting_idx : ending_idx] ending idx is not included

'''


marks= [55,66,77,88,99]
print(marks[1:4])
print(marks[:4])
print(marks[1:])

print(marks[-3:-1])


'''
List Method

list =[2,1,3]

list.append(4) #adds one element at the end [2,1,3,4]

list.sort(reverse =True) #sort in descending order [3,2,1]

list.reverse() #reverses list [3,1,2]

list.insert(idx,el) #insert element at index

list.remove(1) #Remove first occurrence of the element

list.pop(idx) #remove element at idx

'''

#list.append(4) #adds one element at the end [2,1,3,4]
marks = [10,20,30]
marks.append (30)
print(marks)


#list.sort(reverse =True) #sort in descending order [3,2,1]

marks = [10,20,30,4,5,2,5,0,56]

print(marks.sort())

print(marks)

#another

list = [10,20,30,4,5,2,5,0,56]
print(list.sort())
print(list)


#list.reverse() #reverses list [3,1,2]

list = [10,20,30,4,5,2,5,0,56]
print(list.sort(reverse=True))
print(list)






list = ["Banana", "Apple" ,"Mango"]
print(list.sort())
print(list.sort(reverse=True))
print(list)


#list.reverse() #reverses list [3,1,2]




list = ["Banana", "Apple" ,"Mango"]
list.sort()

print(list)


#list.insert(idx,el) #insert element at index

list =[2,1,3]
list.insert(1,5)
print(list)


#list.remove(1) #Remove first occurrence of the element


list =[1,5,3,1]
list.remove(1)
print(list)


#list.pop(idx) #remove element at idx

list =[1,5,3,1]
list.pop(1)
print(list)





