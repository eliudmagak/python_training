#-> They store multiple items that can be of any datatype just like lists
#-> Items are ordered (have index)
#-> Items in a tuple are immutable(cannot be changed)>thus is the main difference between tuples and list
#-> Items are enclosed with normal brackets()
#-> All tuples belong to class tuple

fruits=('Mango','Banana','Lemon','Grapes','Oranges')
print(fruits)
print(type(fruits))
print(fruits[2])
print(fruits[1:4])

#convert turple to list form using list() inorder to make changes
fruits=list(fruits)
print(type(fruits))
fruits[2]='strawberries'
print(fruits)
fruits.append('watermelon')
print(fruits)

#convert back to tuples using tuple()
fruits=tuple(fruits)
print(type(fruits))

days=('monday','tuesday','wednesday','thursday','friday','saturday','sunday')
print(type(days))
#find wednesday using an index
print(days[2])

#using a function find the length of the tuple
print(len(days))

#replace thursday with thur
days=list(days)
days[3]='thur'  
days=tuple(days)
print(days)


