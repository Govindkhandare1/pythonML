'''
loops are used to repeat insrtuction

while loops 

while condition :

#some task



'''
count = 1
while count <= 5 :
    print("Govind")
    count += 1



# check count
    
    count = 1
while count <= 5 :
    print("Govind")
    count += 1
print(count)


#
count = 1
while count <= 5 :
    print("Govind", count)
    count += 1
print(count)

i = 1
while i <=100 :
    print("Govind python", i)
    i += 1



# Reverse loop

    
i = 5
while i >=1  :
    print("Govind python", i)
    i -= 1


 # Another solution
i = 5
while i >=1  :
    print("Govind python", i)
    i -= 1

print("Loop finished") 

# Practice questions 

# Print number from 1 to 100


i = 1
while i <=100  :
    print( i)
    i += 1

#Print numbers from 100 to 1
    

i = 100
while i >=1 :  # this is stopping condition for this loop
    print( i)
    i -= 1


#Print the multiplication table of a number n.
    
i = 1
while i <= 10 :
    print(3*i)
    i +=1


# another solution

    i = 1
while i <= 10 :
    print(5*i)
    i +=1


# we can take input from the user

n = int(input("Enter the number"))
i = 1
while i <= 10 :
    print(n*i)
    i +=1

 #Print the element of the following list using a loop :

#[1,4,9,25,36,49,64,81,100]

num = [1,4,9,16,25,36,49,64,81,100]

idx = 0
while idx < len(num) :
    print(num[idx])
    idx += 1


# search for a number X in this tuple using loop:
    
    #(1,4,9,16,25,36,49,64,81,100)

num = (1,4,9,16,25,36,49,64,81,100,36)
x = 36
i = 0  # initialization
while i < len(num):
    if(num[i]==x):
        print("index found", i)
    i += 1


# Break & Continue keyword

'''

 Break : used to terminate the loop when encountered

 continue : terminates execution in the current iteration & continues execution of the loop with the next iteration.

'''


