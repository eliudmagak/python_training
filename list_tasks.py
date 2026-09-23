trainees = ["John", [2, ["James","Mary"]]] #this is a list within a list
print(len(trainees))

#1. Display 2 from the list.
print(trainees[1][0])

#Output James  from the list.
print(trainees[1][1][0])

# Using a method add 56 at the end of the list.
trainees.append(56)
print(trainees)
    
# Using a method add the name Mike between James and Mary
trainees[1][1].insert(1, "Mike")
print(trainees)

# Change the value of 2 to 8
trainees[1][0] = 8
print(trainees)

# Remove John and Mary from the list.
trainees.remove("John")
print(trainees)
trainees[0][1].remove("Mary")
print(trainees) #you can also use the pop() method to remove items from the list.

# Using a function, determine the length of the list
trainees_length = len(trainees)
print(trainees_length)

employees = ["TechElar",[4, ["Kevin", "Brian", "Alice"]]]

# 1. Display the number 4.
print(employees[1][0])

# 2. Display "Brian" from the list.
print(employees[1][1][1])

# 3. Display "Alice" from the list.
print(employees[1][1][2])

# 4. Using a list method, add the number 7 at the end of the outer list. #why does it bring none when I say employees=employees.append
employees.append(7)
print(employees)

# 5. Add "David" between "Brian" and "Alice".
employees[1][1].insert(2,'David')
print(employees)

# 6. Change the number 4 to 10.
employees[1][0]=10
print(employees)

# 7. Change "Kevin" to "James".
employees[1][1][0]='James'
print(employees)

# 8. Remove "TechElar" from the list.
employees.pop(0)
print(employees)

# 9. Remove "Alice" from the nested list.  # I failed to use.pop but managed to use .remove
employees[0][1].remove('Alice')
print(employees)

# 10. Add "Mary" at the beginning of the nested list.
employees[0][1].insert(0,'Mary')
print(employees)

# 11. Using len(), find the number of items
#     in the nested employee list.
print(len(employees[0][1]))

# 12. Print the final list.
print(employees)
