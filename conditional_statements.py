# Conditional statements
#-> Used to make decisions based on a result of a certain condition
#-> Conditions are created using comparison operators(==,<,>,!=,>=,<=)
#-> Conditions returns True or False.
#-> In python programming language we have 3 main key words for conditional statements(if,else and elif).

     #if statement
#=> Executes/run a block of code when the condition is True.

#    Syntax
#if condition:
   #if block

if 20>10:
    print('20 is greater')
else:
    print('20 is less')


age=20
if age>=18:
    print('Adult')
else:
    print('Minor')

# Users are allowed to join the website only if the age is from 18 to 60
age>=19
age<=60

if age>=18 and age<=60:
    print('Access Granted')
else:
      print('Access Denied')

# check if temperature is above 30 print too hot
temperature=35
if temperature>=30:
    print('too hot')
else:
    print('normal')

marks=20
if marks>50:
    print('Pass')
else:
    print('Fail')

#   if-else statement
#-> else executed the else block when the condition is false(otherwise of if) 
     
   #syntax
#if condition:
    #if block
#else:
    #else

#print access granted if password is similar to Admin@254! otherwise access Denied
password=input('Enter your password')

if password=='Admin@254!':
    print('access Granted')
else:
    print('access Denied')

#if-elif-else
# =>Elif is used when we have multiple conditions with different outcomes

# syntax   
#if condition:
   #if block
#elif condition:
   #elif block1
#elid condition:
   #elif block2

#temperature
temperature=20
if temperature>30:
    print('Too hot')
elif temperature>15:
    print('normal temperature')
else:
    print('cold temperature')


#age
age=10
#senior adult above 50
#above 20 adult
#above 12 teenager
#otherwise a child
if age>50:
    print('senior Adult')
elif age>20:
    print('Adult')
elif age>12:
    print('teenager')
else:
    print('child')

#marks
# print A if marks is above 80
# print B if marks is above 70
# print C if marks is above 60
# print D id marks is above 50
# otgerwise print E
marks=56

if marks>80:
    print('A')
elif marks>70:
    print('B')
elif marks>60:
    print('C')
elif marks>50:
    print('D')
else:
    print('E')


