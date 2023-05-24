#CRUD create, read, Update and Delete

numbers = [1, 2, 3, 4, 5]
print(numbers[1])
print[-1]= 10
print(numbers)

#Añadir valores al final de la lista
numbers.append(700)
print(numbers)

#Añadir valores en cierta posición de la lista
numbers.insert(0, "hola")
print(numbers)

numbers.insert(3, "change")
print(numbers)

#Union de listas
task=["todo 1", "todo 2","todo 3"]
new_list= numbers + task 
print(new_list)

#Saber posición de elemento 
index = new_list.index("Todo 2")
new_list[index]= "Todo changed"
print(new_list)

#Eliminación
new_list.remove("Todo 1")
print(new_list)

new_list.pop(0)
print(new_list)

#Eliminación último elemento 
new_list.pop()
print(new_list)

#Cambiar de posición 
new_list.reverse()
print(new_list)

#Ordenar
numbers_a = [1,4,6,3]
numbers_a.sort()
print(numbers_a)

strings = ["re", "ab", "ed"]
strings.sort()
print(strings)