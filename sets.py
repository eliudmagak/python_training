#Sets are data structures that stores multiple items that can be of any type.
#> Items in a set are unordered(no index)
#>Items in a set are unique (no duplicates)
#>Items are enclosed in curly braces {}
#>A set is mutable (can be changed) but the items in a set are immutable (cannot be changed)

fruits={'Mango','Oranges','Bananas','Lemon','Grapes'}
print(fruits)

#add()
fruits.add('strawberries')
print(fruits)

#remove()/discard()
fruits.remove('Bananas')
print(fruits)

days={'monday','tuesday','wednesday','thursday','friday','saturday','sunday','sunday','sunday'}
print(days)
#remove friday and sunday from the set using methods
days.remove('friday')
days.discard('sunday')
print(days)

#Add them back to the set
days.add('friday')
days.add('sunday')
print(days)