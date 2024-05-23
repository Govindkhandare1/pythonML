

#What is python

#python is simple and easy

#* free and open source

#* High level Language

#Developed by Guido van Rossum

#python is portable

#First Program

print("Hello world Govind")

# python character set

#letters - A to Z , a to z

#Digit - 0 to 9 
#Special Symbol - + - * / etc.
# whitespaces -- blank space , tab , carriage return ,newline,formfeed

#other characters - python can process all ASCII and Unicode characteres as part of data or literals


print("Govind is MY name","my age is 27")

print(10+20)


# variable
#A variable is a name given to a memory location in a program
name= "Bhola Govind"  #string
Age= 27
price= 12.33

print(name,Age)

print("My name is : ",name)
print("my age is : " ,Age)

print(type(name))
print(type(Age))
print(type(price))


# data Types

#integers
#positive , negative , 0 (25,-25,0)

#String "Govind" "Hello"   ""  ''  ''' '''
name = "GK"
name2= 'GK'
name3= '''GK'''

#Float

#1.22 any decimal value

#Boolean = True and False (First letter should be capital)

#none   no value stored


#keywords

#reserved words --and ,as assert,break class, continue,def,del,elif,else,except,finally,False,for,from,global,if,import,in,is,lambda
#nonlocal,None,not,or,pass,raise,return,True,try,with,while,yield

a=2
b=5
sum =a+b
print(sum)

#type of Tokens

#Punctuators 

#Punctuators are symbol to organize sentence structure in programming

#(),{},@,[],#, etc. and -=,+=,/=,*=,//=,= etc

###################################################################

# Time 50 min completed and Expression Execution chaper learn tom

#Today i can start from here 23 April 2024

#Expression execution 

#String and Numeric values can operate together with *
#A,B=2,4
Txt="@"
print(2*Txt*3)
#2*@*3  = @@@@@@  ----- python will consider @ print 6 times
#Output like @@@@@@

#String $String Can operate with +
A,B="2",3
Txt="@"
print((A+Txt)*B)

#2+@ = 2@ and * 3  ans will be 2@2@2@
#Output like  2@2@2@

###############Numeric values can operate with all arithmetic operators 

A,B =2,3
C=4
print(A+B*C)

#Ans = 14
############################Arithmetic expression with integer and float will result in float

A,B = 10,5.0
C=A*B
print(C)

#Ans 50.0
########Result of division operator with two integers will be float

A,B= 1,2
C=A/B
print(C)

#Ans 0.5


#######   integer division with float and int will give int displayed as float

A,B=1.5,3
C=A//B
print(C,A/B)

#Ans for C A//B = 0.0  and A/B = 0.5

########### Floor gives closest integer, which is lesser than or equal to the float value
#Result of (A//B) is same as floor(A/B)

A,B=12,5
C=A//B
print(C)

#C=12//5   and answer will perform like (12/5) = 2.4 but we will take closet interger 2
#Ans 2  get value closest integer like 0.1 = 0 closet integer 5.2 = 5 closet integer  another exammple -5.2 = -6  , 2=2 closet integer



A,B=-12,5
C=A//B
print(C)
#C=-12 //5     and answer will be (-12/5) =-2.4 but in negative values we will take closet integer = -3
# Ans = -3



A,B=12,-5
C=A//B
print(C)
#C=12 //-5     and answer will be (12/-5) =-2.4 but in negative values we will take closet integer = -3
# Ans = -3



###########   Remainder is begative when denominator is negative
#  modulo or reminder % 
#   n/denominator   
# case 1 -   +/+    Ans = +
# CASE 2 -   -/-    Ans = +
#CASE 3 -  +/_      Ans = -Ve
# case 4 -   -/+    Ans = +

A,B=-5,2
C=A%B
print(C)

#C =(-5/2)   ans will be 1

A,B=5,2
C=A%B
print(C)

#Ans 1


A,B=5,-2
C=A%B
print(C)

#Ans = -1

##############################################################

#Comments in Python

#Single line comment we use # 

#We can use for multi line comments""""

'''
this is a multi line
Comments

'''


##Input in Python

'''input() statement is used to accept values(using keyboard) from user'''

# String input 
# name= input("name:")


#int input 
#age = int(input("age:"))

#float input
#Price =float(input("price:"))


#Taking input from the user and printing it

name=input("name:")
print(name)



# taking int values

age= int(input("age :"))
print(age)

#Taking float values

price =float(input("price:"))
print(price)

# Print all input in single print statement
print("my name is ",name,"and i am ",age,"year","and price will be ",price,)

#############################################################

#Completed till 1 hour 16 min and topic is Practice time 



#state true and false

'''1) /* is a symbol used in python for single line comment.
Ans: False

2)2ndName is an invalid identifier in oython .
Ans: True

3) ** is a valid arithmetic operator in oython.
Ans:  True

4)in is a logic operator in oython.
Ans: False

5)variable declaration is implicit in oython.
Ans: True
'''


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


    #Another example

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

Or Table Truth table

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

#Operators
a=5
b=2

print(a!=b)
print(a>=b)
print(a>b)
print(a<b)
print(a<=b)

'''
Relational operator

(==,) Equal to
(!+) Not equal to

'''

# Completed till 2.05 hours (2 hour 5 min)

#Logical operators (not,and,or)
#Not Operator
'''not true = False
not False = True'''

print(not False)
print(not True)

a=50
b=30


print(not False)
print(not True)

print(not (a>b))

# And Operator
val1 = True
val2= True
print("and operator",val1 and val2)

val1 = True
val2= False
print("and operator",val1 and val2)


#OR OPERATOR

val1 = True
val2= False

print("and operator",val1 or val2)


#Type Conversion

a=int("2")
b=4.25
print(type(a))
print(a+b)


a=3.14
a=str(a)

print(type(a))

#Practice question
'''Write a program to input 2 numbers and pritn their sum'''

num1=int(input("Enter first number"))
num2=int(input("Enter Second Number"))

num=num1+num2
print("your total",num)

#another  solution
num1=int(input("Enter first number"))
num2=int(input("Enter Second Number"))


print("your total",num1+num2)


#Another question
'''WAP to input side of a square and print its area'''

side=int(input("Enter Square side :"))
side2=side*side
print("Area of Square is :",side2)

#amother
side=int(input("Enter Square side :"))

print("Area of Square is :",side*side)


#another solution

side=int(input("Enter Square side :"))

print("Area of Square is :",side**2)

#Another Questions
'''WAP to input 2 floating points numbers & pritn their average'''


num1=float(input("Enter first number:"))
num2=float(input("Enter Second Number"))

avg=(num1+num2)/2
print("AVergae of given float numbers",avg)

#Another solution
num1=float(input("Enter first number:"))
num2=float(input("Enter Second Number"))


print("AVergae of given float numbers",(num1+num2)/2)

#Write a Program to input 2 int numbers, a and B print True is a is greater than or equal to b. if not print False.

a= int(input("Enter First number"))
b=int(input("Enter second Number"))

print(a>=b)


##################################################################################################

#Chapter 2

'''String and Conditional statement'''

'''String is data type that stores a sequence  of characters'''



str1=" This is a string"
str2= 'This is string 2'
str3= """This is String three"""


'''escape sqquence characters'''

#\n for next line


str1=" This is a string.\n this is GOvind."
print(str1)

'''Concatenation  is adding two string into one with plus(+) operator
for example

"hello" + "World"  -------> "Helloworld"
'''

str="Hello"
str1="World"
print(str+str1)


#Length of str      len(str)   and space also count in length


str="Hello"
len1=len(str)
print(len1)


str1="World"
len2=len(str1)
print(len2)


print(len(str+str1))

print(len(str+" "+str1))


# Indexing

# indexing nothing but position

str="Hello World"
ch=str[0]
print(ch)


#Slicing basically used for ML

'''In Python, slicing is a technique used to extract a portion of a sequence (like lists, tuples, or strings) by specifying a range of indices. The syntax for slicing is sequence[start_index:end_index:step]. Here's an explanation of each component:

start_index: The index from where the slicing should begin. This index is inclusive, meaning the element at this index will be included in the slice.

end_index: The index where the slicing should end. This index is exclusive, meaning the element at this index will not be included in the slice.

step (optional): The step size used to skip elements while slicing. This is an optional parameter and is by default 1. 

A positive step means slicing forward through the sequence, while a negative step means slicing backward.'''



# Accessing parts of a string
'''
str[starting_idx:ending_idx] #ending idx is not included'''

str="Hello World"
str1=str[1:4] #is "ell"
print(str1)


str="Hello World"
str1=str[6:] #is "ell"
print(str1)

str="Hello World"
str1=str[:11] #is "ell"
print(str1)


#Negative indexing

str="Apple"
print(str[-5:-2])


# String Function Started
 # Time is 2 hours 52 min 




'''
String Functions
str = "I am a coder."
str.endswith("er.") #returns true if string ends with substr
str.capitalize() #capitalizes 1st char
str.replace old, new) #replaces all occurrences of old with new
str.find(word) #returns 1st index of 1st occurrence
str.count("am") #counts the occurrence of substr in string
'''

str = "i am studying python"
print(str.endswith("python"))




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

'''
Practive questions

Write a program users first name& print its length
'''

name=str(input("Enter First name :"))
print("lengt of yout name",len(name))



# write a programe to find the occurance of'$' in a string


str= "hi we are using a doller $ symbol to our payment gateway "
print(str.count("$"))



str= "hi we are using a $ doller $ symbol to our payment $ gateway  $100"
print(str.count("$"))


#conditional statement

#completed till 3 hour 2 min





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

a=int(input("enter number"))#with creating new variable
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


#Completed till 3 hour 27 min
#and started new chapter 3 List in python        
    

'''
In Python, a list is a built-in data structure used to store a collection of items. 
Lists are ordered, mutable (meaning you can change their elements), and can contain elements of different types. Y
ou can create a list by enclosing comma-separated values within square brackets 
'''

