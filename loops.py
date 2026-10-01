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
lst=list(range(1,21))
for i in lst: print('Eliud')

# display even numbers between 1 and 100
lst1=list(range(1,101))
for i in lst1:
    if i%2==0:
        print(i)    

#display numbers divisible by 5 from numbers between 100 and 150
lst2=list(range(100,151))
num1=[]
for i in lst2:
    if i%5==0:
        num1.append(i)
print(num1)

#display odd numbers between 1 and 100
lst3=list(range(1,101))
odd=[]
for i in lst3:
    if i%2!=0:        #or if i%2==1
        odd.append(i)
print(odd)       
      
        

#display numbers divisible by 3 and 5 from numbers between 100 and 200
lst4=list(range(100,201))
divisible=[]
for i in lst4:
    if i%3==0 and i%5==0:
        divisible.append(i)
print(divisible)

#display in a list numbers divisible by 5 and 7 drom numbers between 1 and 100
lst5=list(range(1,101))
div5=[]
for i in lst5:
    if i%5==0 and i%7==0:
        div5.append(i)
print(div5)   

# break-> Used to stop the loop.
lst5=list(range(1,101))
for i in lst5:
    print('test')
    if i==5:
        break

# simcard pin
lsts=list(range(1,4))
attempts=3
for x in lsts:
    pin=input('Enter your pin: ')
    correct_pin='1234'
    if pin==correct_pin:
        print('Access granted')
        break
    else:
        rem=attempts-x
        if rem==0:
            print('Account blocked')
        else:
            print(f'Wrong pin try again you have {rem} attempts remaining')


