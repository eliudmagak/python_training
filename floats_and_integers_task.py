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

####convert  float 56.8926 to 8.926
temp=56.8926 
temp=str(temp)

#convert float 5678.4567 to 5.678
temp=5678.4567
temp=str(temp)  
temp=temp[0:4] 
temp=temp[0]+'.'+temp[1:4]
print(temp)
temp=float(temp)
print(type(temp))

#convert float 5678.4567 to 456.7
temp=5678.4567
temp=str(temp)
temp=temp[5:9]
print(temp)
temp=temp[0:3]+'.'+temp[3:]
print(temp)
temp=float(temp)
print(type(temp))
