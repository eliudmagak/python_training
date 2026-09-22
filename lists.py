fruits=['Mango','Banana','Lemon','Grapes','Oranges']
print(fruits)
print(type(fruits))

#indexing and slicing
print(fruits[3])
print(fruits[2])
print(fruits[-1])

#slicing used to extract a part of a list using index [start_index:end_index+1]

#create a list of days of the week
days_of_the_week= ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
#display day today
print(days_of_the_week[0])
#display wednesday to saturday
print(days_of_the_week[2:6])

#updating items in the list
# (change oranges to tomatoes)
print(fruits)
fruits[-1]='tomatoes' 
print(fruits)

#append()
#.append adds items at the end of the list
fruits.append('strawberries')
print(fruits)
fruits.append('apple')
print(fruits)

#insert()
#.insert adds items at a specified index 
fruits.insert(3,'watermelon')
print(fruits)

#update Thursday to Thur
print(days_of_the_week)
days_of_the_week[3]='Thurd'
print(days_of_the_week)

#add January at the end of the list
days_of_the_week.append('January')
print(days_of_the_week)

#add December between Wednesday and Thursday
days_of_the_week.insert(3,'December')
print(days_of_the_week)

#remove()
#.remove() removes a specified item from the list
print(fruits)
fruits.remove('Lemon')
print(fruits)

#pop()
#.pop() removes an item at a specified index and if index is not provided it removes the last item on the list
print(fruits)
fruits.pop(2)
print(fruits)
fruits.pop()
print(fruits)

#clear()
#.clear() erases all items from the list

#delete friday from the list
days_of_the_week= ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
days_of_the_week.pop(4)
print(days_of_the_week)

#delete the last item from the list
days_of_the_week.pop()
print(days_of_the_week)

#delete all the items from the list
days_of_the_week.clear()
print(days_of_the_week)

