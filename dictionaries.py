#Dictionaries
#>Stores multiple properties in key-value pairs:(value)
#>Enclosed wit {curly brackets}
#>Keys are always strings but values can be of any type
#>Keys are unique
#>It belongs to class 'dict'

student1={
    'name':'alex',
      'age':20,
      'adm':'tech2015',
      'city':'Nairobi',
      'skills': ['UI', 'UX', 'Web']}

print(student1)
print(type(student1))

#displaying value
print(student1['name'])
print(student1['city'])

#adding and updating
#adding
student1['gender']='Male'
print(student1)

#updating
student1['age']=30
print(student1)

#display adm
print(student1['adm'])

#add a new key email with value
student1['email']='brian25@gmail.com'
print(student1)

#update name with a different name
student1['name']='brian'
print(student1)

#Delete a oroperty
del(student1['age'])
print(student1)

#.get() used to display values
print(student1.get('adm'))

#.keys Used to display a list of all keys
print(student1.keys())

#.values Used to display a list of all values
print(student1.values())

#.items Used to display list of tuples of each property
print(student1.items())

print(student1)