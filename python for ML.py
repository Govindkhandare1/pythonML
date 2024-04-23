

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



