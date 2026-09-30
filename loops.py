      # Python Loops
#-> Used to perform repetitive tasks multiple times or until a certain condition is met.
#-> We have 3 main loop commands in python;
        #for loop
        #While loop

     # For loop
#-> Used to iterate over a sequence (strings,lists,tuples)

# Syntax
#for iterator in sequence:
   # block of code
# iterator-> represents each character/item in the swquence

fruits=['mango','oranges','apple','lemon','grapes']
for i in fruits:
    print(i)

    numbers=[10,20,30,40,50]
    for num in numbers:
        print('hello')

# Display Techcamp 20 times 
nums=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for i in nums:
    print('Techcamp')

# range(start,end+1)-> used to create a list of numbers
list=list(range(1,21))
for i in list: print('Eliud')