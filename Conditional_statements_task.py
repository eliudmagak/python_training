#1.Take three inputs from a user, separately. Print the largest of the numbers.
   # Hint: Determine what type of data is taken in as input.
num1=int(input('Enter the first number: '))
num2=int(input('Enter the second number: '))
num3=int(input('Enter the third number: '))

if num1 > num2 and num1 > num3:
    print('The largest number is:',num1)
elif num2 > num1 and num2 > num3:
    print('The largest number is:',num2)
else:
    print('The largest number is:',num3)


#2.Take as input from a user the temperature if the temperature is above 30°C display “The temperature is too high”,if the temperature is above 15 display “Normal temperature” otherwise display “Cold temperature”
temperature=float(input('Temperature: '))
if temperature > 30:
    print('The temperature is too high')
elif temperature > 15:
    print('Normal temperature')
else:
    print('Cold temperature')

#3.	Write a Python program that checks if a variable x is between 10 and 20 (inclusive)
    #and if another variable y is greater than 100. If both conditions are true, print "Conditions met", otherwise print "Conditions not met"
x=24
y=114
if 10<=x<=20 and y>100:
    print('Conditions met')
else:
    print('Conditions not met')

#4. Write a Python program that checks if a variable password is equal to the string "secret123". If it is, print "Access   granted", otherwise print "Access denied"
password=input('Enter your password:')
valid_password='secret123'
if password==valid_password:
    print('Access granted')
else:
    print('Access denied')

#1.Assume start_date = '2024-01-01' and end_date = '2024-12-31'. Write a conditional statement that checks:
  #If start_date comes before end_date, print "Valid period",
  #If start_date is after end_date, print "Invalid period".
  #If both dates are the same, print "One-day period".
start_date = '2024-01-01'
end_date = '2024-12-31'

if start_date< end_date:
    print('Valid period')
elif start_date>end_date:
    print('Invalid period')
else:
    print('One-day period')

#2.Given two strings str1 and str2, write a conditional statement that checks:
  #If str1 is longer than str2, print "str1 is longer".
  #If str2 is longer than str1, print "str2 is longer".
  #If both have equal length, print "Both are of equal length".
str1='I am learning python'
str2='I am a student learning python'

if len(str1)>len(str2):
    print('str1 is longer')
elif len(str2)>len(str1):
    print('str2 is longer')
else:
    print('Both are of equal length')

#3.Given a list valid_ids = [101, 102, 103] and a variable user_id = 105, write a conditional statement that:
  #Prints "Access Granted" if user_id is in valid_ids.
  #Prints "Access Denied" if user_id is not in valid_ids.
valid_ids = [101, 102, 103]
user_id = 105
if user_id in valid_ids:
    print('Access Granted')
else:
    print('Access Denied')

#4.Given a variable value that could be of any type, write a conditional statement that:
  #Prints "String Detected" if value is a string.
  #Prints "Integer Detected" if value is an integer.
  #Prints "Unknown Type" for any other type.
Value=25
if type(Value)==str:
    print('string Detected')
elif type(Value)==int:
    print('Integer Detected')
else:
    print('Unknown Type')

  #Write a Python program that checks if a variable student_score is greater than 90. If true, check if the attendance is greater than 80. If both conditions are true, print "Excellent student", otherwise print "Good score, but attendance needs improvement"


 #Write a program that:
#Takes a transaction amount and account type ("Standard" or "Premium") as input.
#f the account type is "Standard":
#Check if the amount is above 500:
#If it is, print "Transaction exceeds the limit for Standard accounts."
#If not, print "Transaction approved."
#If the account type is "Premium":
#Check if the amount is above 1,000:
#If it is, print "Transaction exceeds the limit for Premium accounts."
#If not, print "Transaction approved."
#Otherwise “Wrong account type” 


#Given x = 7 and y = 14, write nested conditional statements that print:
#"x and y are both even" if both x and y are even numbers.
#"Only y is even" if only y is even.
#"Neither x nor y are even" if both are odd.


