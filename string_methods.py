#clean sentence 1 to 'python programming'
sentence1='    PYThon ProgrammING'
sentence1=sentence1.strip().lower()
print(sentence1)

#Clean sentence2 to 'SOFTWARE DEVELOPMENT'
sentence2='    Software DEVELOPMENT    '
sentence2=sentence2.strip().upper()
print(sentence2)    

#Clean sentence3 to 'computer science'
sentence3='COMputer ScieNCE'
sentence3=sentence3.strip().lower()
print(sentence3)   

#Clean sentence4 to 'Techcamp Kenya'
sentence4='TECHcamp Kenya'
sentence4=sentence4.strip().title()
print(sentence4)

# Replace
sentence5='I am a python Developer'
sentence6=sentence5.replace('python','Java')
print(sentence6)

#Count
print(sentence5.count('e'))

#split
sentence7=sentence5.split('t') 
print(sentence7)

#index
print(sentence5.index('y'))
print(sentence5.index('e',18))

# people prefer.find() method over index() because it returns -1 if the substring is not found, while index() raises an error.

#change sentence7 to Alex Mwangi
sentence7='Alex Kimani'
print(sentence7)
sentence7=sentence7.replace('Kimani','Mwangi')
print(sentence7)

# count the number of times o has appeared in sentence8
sentence8='python programming'
print(sentence8.count('o'))

#split sentence9 using the colon
sentence9='Alex:Brian:Mike:Kevin'
print(sentence9.split(':'))
