# Question 1
a,b,c = 24,1209.94,"python"
print (a,b,c)

# Question 2
d = (12+3j)
print (d)

# Question 3
a,d = d,a
print(a)
print(d)

#Question 4
i = eval(input("Enter any value: "))
print(i)

# Question 5
x,y=eval(input("Enter any two numbers between 1-10: "))
### 5.1
z = x+y
### 5.2
q = z+30
print(q)

# Question 6
a6 = eval(input("Enter any value: "))
print("the datatype for entered value is: ",type(a6))

# Question 7
# In Python, a variable holds the reference to the object. An object is a chunk of allocated memory that holds a value and a header. Object's header contains its type and a reference counter that denotes the amount of times this object is referenced in the source code so that Garbage Collection can identify whether an object can be collected.

#Now when you assign values to a variable, Python actually assigns references which are pointers to memory locations allocated to objects:
# x holds a reference to the memory location allocated for  
# the object(type=string, value="Hello World", refCounter=1)

# x = "Hello World"
# Now when you assign objects of different type to the same variable, you actually change the reference so that it points to a different object (i.e. different memory location). By the time you assign a different reference (and thus object) to a variable, the Garbage Collector will immediately reclaim the space allocated to the previous object, assuming that it is not being referenced by any other variable in the source code:
# # x holds a reference to the memory location allocated for  
# the object(type=string, value="Hello World", refCounter=1)

# x = "Hello World" 

# Now x holds the reference to a different object(type=int, value=10, refCounter=1)
# and object(type=string, value="Hello World", refCounter=0) -which is not refereced elsewhere
# will now be garbage-collected.
# x = 10 