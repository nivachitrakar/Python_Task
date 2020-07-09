# Question 1
x = eval(input("enter any number: "))
if(x%3==0):
    print("Consultadd")
elif(x%5==0):
    print("C")

if(x%3==0 and x%5==0):
    print("Consultadd Python Training")

# Question 2
a = eval(input("enter the number from 1 to 5: "))

if(a==1):
    i,j = eval(input("enter any two numbers for addition: "))
    ans = i+j
    print(ans)
elif(a==2):
    i,j = eval(input("enter any two numbers for substraction: "))
    ans = i-j
    print(ans)
elif(a==3):
    i,j = eval(input("enter any two numbers for division: "))
    ans = i/j
    print(ans)
elif(a==4):
    i,j = eval(input("enter any two numbers for multiplication: "))
    ans = i*j
    print(ans)
elif(a==5):
    i,j = eval(input("enter any two numbers for average: "))
    ans = (i+j)/2
    print(ans)    
else:
    print("Zsa")  

# Question 3
age = 38
if(age >= 11):
    print("You are eligible to see the football match")
    if(age<=20 | age>=60):
        print("The ticket price is $12.")
    else:
        print("The ticket price is $20")
else:
    print("You are not eligible to buy the ticket.")

# Question 5
for x in range(2000,3200):
    if(x%7 == 0 and not(x%7==0 and x%5==0)):
        print(x)
#Question 6 
#6.1
x=123 
   	   for i in x:
   		print(i)
# Output: Syntax error, we need to put range() for x so that it prints the number from 0 to 122

#6.2
i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break
else:
    print(“error”)
# Output :
# 0 
# 1 
# 2

#6.3
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break
# Output:
# 0
# 1
# 2
# 3
# 4

# Question 7
for x in range(6):
    if (x == 3 or x==6):
        continue
    print(x,end=' ')

# Question 8
s = input("Input a string: ")
d=l=0
for c in s:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass
print("Letters", l)
print("Digits", d)

# Question 9 part 1
x=24
num = eval(input("Guess the lucky number: "))
while(x!=num):
    print("You didn't guess the lucky number")
else:
    print("You guessed the lucky number!")


# Question 9 part 2
x=24
num = eval(input("Guess the lucky number: "))
while(x!=num):
    print("You didn't guess the lucky number")
    num = eval(input("Would you like to guess the lucky number again: "))
else:
    print("you guessed the lucky number")

# Question 10
counter=1
while counter <= 5:
    num = input("Guess the lucky number ")
    if(num!=24):
        print("you have missed your", counter,"chance")
        
    else:
        print("Good Guess!!")
    counter=counter+1
else:
    print("Game Over")

# Question 11
counter=1
while counter <= 5:
    num = input("Guess the lucky number ")
    if(num!=24):
        print("you have missed your", counter,"chance")
        
    else:
        print("Good Guess!!")
        break
    counter=counter+1
else:
    print("Sorry but that was not very successful")

