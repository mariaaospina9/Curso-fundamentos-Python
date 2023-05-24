#Tuplas - solo de lectura
#CRUD - no se puede modificar 
numbers= (1,2,3,5)
strings = ("nico", "zule", "santi")
print(numbers)
print(strings)

print(type(numbers))
print(type(strings))

#Buscar elementos
print("0 =>", numbers[0])
print("-1 =>", numbers[-1])

#Buscar posición 
print(strings)
print(strings.index("zule"))

#Conteo en tupla
print(strings.count("nico"))

#Transformación de tupla a lista
my_list = list(strings)
print(my_list)
print(type(my_list))

#Se puede comenzar a modificar
my_list[1]= "juli"
print(my_list)

#Trasnformación de lista a tupla
my_tuple= tuple(my_list)
print(my_tuple)