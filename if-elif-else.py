
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



