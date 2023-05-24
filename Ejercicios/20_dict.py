person = {
  "name": "Maria"
  "last_name": "Ospina"
  "langs": ["python", "javascript"]
  "age": 99
}

print(person)

#Actualización 
person["name"]= "Santi"
person["age"]-= 50
person["langs"].append("rust")
print(person)

#Eliminación 
del person["last_name"]
person.pop("age")
print(person)

#Orden 
print("items")
print(person.items())

print("keys")
print(person.keys())

print("values")
print(person.values())