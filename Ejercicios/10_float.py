x = 3.3
y= 1.1 + 2.2
print(x)
print(y)
print(x == y) #No son iguales

#Con strings 
y_string = format(y, ".2g")
print("str =", y_string)
print( y_str == str(x))

#Forma matemática
print("*" *10)
print(y,x)
tolerance = 0.0001
print(abs(x - y) < tolerance)
