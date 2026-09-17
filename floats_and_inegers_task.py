#Convert float to integer
temp=56.8926
temp=round(temp)
print(temp)

#convert float 56.8926 to 56.89
temp=56.8926
temp=round(temp,2)
print(temp)

#convert flloat 56.8926 to 56.893
temp=56.8926
temp=round(temp,3)  
print(temp)

#convert  float 56.8926 to 8.926
temp=56.8926 
temp=str(temp)   #'56.8926'
print(type(temp))
print(temp.find('8'))
print(temp[3:])  
print(temp[3:]+'.')