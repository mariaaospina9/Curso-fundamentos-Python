name = "Maria"
last_name= "Ospina"
print(name)
print(last_name)

full_name = name + " "+ last_name
print(full_name)

quote = "I' am Maria"
print(quote)

#format
template = "Hola, mi nombre es " + name + " y mi apellido es " + last_name
print("v1",template)

template = "Hola, mi nombre es {} y mi apellido es {}". format(name,last_name)
print("v2",template)

template= f"Hola, mi nombre es {name} y mi apellido es {last_name}"
print("v3", template)