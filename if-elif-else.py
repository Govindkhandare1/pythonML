
# Conditional Statemen

'''if-elif-else   (SYNTAX)

if(condition):

Statement1

elif(condition):
Statement2

else:
StatementN
'''

age=int(input("enter age :"))

if (age>=18):
    print("eligible for Vote")
elif(age<18):
    print("wait for 1 year")
else:
    print("thanks") 


#Another Example
    

light = input("light color:")

if(light == "red"):
    print("Stop")
elif(light == "yello"):
    print("look")
elif(light == "Green"):
    print("go")
else:
    print("Light is broken")   


 # Another Example

# Grade of Student

marks = int(input("marks :"))
if(marks>=90):
    print("A")
elif(marks>=80 and marks <90):
    print("B")
elif(marks >= 70 and marks <80):
    print("C")
else:
    print("D")     




# Another example
    #Hello

'''
Truth Table for AND operator

A       B       A and B
--------------------------
True    True    True
True    False   False
False   True    False
False   False   False

OR operator Table Truth table

A       B       A or B
--------------------------
True    True    True
True    False   True
False   True    True
False   False   False


'''
# A= 5 & G= M
#A= 2 & G= F

A= int(input("A :"))
G= input("M/F :")
if((A==1 or A==2) and G== "M"):
    print("fee is 100")
elif(A==3 or A==4 or G == "F"):
    print("fee is 200")
elif(A==5 and G == "M"):
    print("fee is 300")
else:
    print("No fees")               


#single line if/Ternary operator

'''<var> if <condition> else <val2>
'''


food = input("food :")
eat = "Yes" if food == "cake" else "no"
print(eat)


#another example

food=input("food:")
print("sweet") if food =="cake" or food =="jamun" else print("not sweet")



'''clever if/ Ternary operator

<var> = (false_val,true_val) <condition>
'''

age = int(input("age:"))
vote = ("yes","no")[age<=18]
print(vote)

# Another example

sal = float(input("salary :"))
tax = sal*(0.1 ,0.2) [sal>=50000]
print(tax)




#other sample example
age = 17

if (age >= 18):
    print("eligible for vote")

elif(age==18):
    print("wait for wait till age 18")
else:
    print("you are minor")



#another sample example
Grade=int(input("Enter your Marks"))

if(Grade>=90):
    print("You are in Grade A")
elif(Grade>=80 and Grade<90):
    print("You Are in Grade B")
elif(Grade >=70 and Grade <80):
    print(" Your are in Geade C")
else:
    print("You are fail ")



#Nesting  we can use if staatemnt in same if statement 

age = 80
if(age>=18):
    if(age>=80):
        print("Your age is greater than 80 you are sinior citizen recommended to not drive ")
    else:    
        print("You can Drive")
else:
    print("Can not drive")   

# if user wants to enter age manually (take inout from the user)
    age = int(input("Enter your Age:"))
if(age>=18):
    if(age>=80):
        print("Your age is greater than 80 you are sinior citizen recommended to not drive ")
    else:    
        print("You can Drive")
else:
    print("Can not drive")




#Nesting  we can use if staatemnt in same if statement 

age = 80
if(age>=18):
    if(age>=80):
        print("Your age is greater than 80 you are sinior citizen recommended to not drive ")
    else:    
        print("You can Drive")
else:
    print("Can not drive")   

# if user wants to enter age manually (take inout from the user)
    age = int(input("Enter your Age:"))
if(age>=18):
    if(age>=80):
        print("Your age is greater than 80 you are sinior citizen recommended to not drive ")
    else:    
        print("You can Drive")
else:
    print("Can not drive")




'''
Practive Questions

write a programe to check if a number entered by the user is odd or even.
'''
num =int(input("Enter Number"))

if(num%2==0):
    print("this is even number")
else:
    print("this is ODD number")



#Another solution for this
num=int(input("Enter your number"))

rem=num%2

if(rem==0):
    print("this is even number")
else:
    print("This is Odd Number")



#Write a programe to find the greatest of 3 numbers entered by the user.


num1=int(input("Enter First number"))
num2=int(input("Enter Second number"))
num3=int(input("Enter Third number"))

if(num1>num2 and num1>num3):
    print("Num 1 is greated than all entered number num 2 and num 3")
elif(num2>num1 and num2>num3):
    print("Num 2 is greater than Numn 1 and Num 3")  
elif(num3>num1 and num3 >num1):
    print("Num 3 is greater than num 2 and num 1")
else:
    print("user entered same value for all 3 number")


 #another solution

    #Write a programe to find the greatest of 3 numbers entered by the user.


num1=int(input("Enter First number"))
num2=int(input("Enter Second number"))
num3=int(input("Enter Third number"))

if(num1>num2 and num1>num3):
    print("Num 1 is greated than all entered number num 2 and num 3:",num1)
elif(num2>num3):
    print("num 2 is greatest number than num 1 and num3 :", num2)
else:
    print("Thirs number is lagest number than num 1 and num 2:",num3)


#Write a programe to chek if a number is a multiple of 7 or not

a=int(input("enter number"))
b=a%7
if(b==0):
    print("this number is multiple of 7")
else:
    print("This number is not multiple of 7 check another number")


#another soultion
a=int(input("Enter a number"))

if(a%7==0):
    print("entered number is multiple of 7 ")

else:
    print("enter number is not multiple of 7 try another number") 