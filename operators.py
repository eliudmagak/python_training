#operators
#>Special symbols or keywords used to perfom operations on values and variables

     #Categories of operators
#->Arithmetic Operators->Used to perform calculations(%,//,-,**,+,*,/)

#->Comparison operators->Used to compare values or variables(>,<,==,>=,<=)
#>They return boolean(true or false)
#>create conditions
print(10==10)

#->Logical operators->Used to combine conditions
#>and-> returns true if all conditions are true
print(20<10 and 40<50)
print(20>10 and 40<50)

#> or-> returns true if at least one condition is true.
print(20<10 or 40<50)

#> not->Inverts the result of a condition
print(not 10<20)
print(not False)
print(not True)

#->Assignment operators->Used to assign values to variables(=,+=)
x=20
y=30
x=x+y  #/ x+=y
print(x)

x=x/y  #? x/=x
