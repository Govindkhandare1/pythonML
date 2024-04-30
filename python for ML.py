

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
