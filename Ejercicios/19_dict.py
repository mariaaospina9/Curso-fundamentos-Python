my_dict= {}
print(type(my_dict))

my_dict= {
  "avion": "bla bla bla"
  "name": 'Maria'
  "last name": "Molina"
  "age": 87
}
print(my_dict)

#Número de elementos
print(len(my_dict))

#Leer ese diccionario
print(my_dict["age"])
print(my_dict["last name"])
print(my_dict.get("age")) #si no existe - dira none (nada definido)

#Palabra se encuentra en diccionario 
print("avion" in my_dict)