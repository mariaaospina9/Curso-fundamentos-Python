text= "Ella sabe Python"
#Dar la posición []
print(text[1])

#último cáracter del texto
size = len(text)
print("size => ", size)
print(text[size - 1])

print(text[-1])

#Slicing - dar una cadena 
print(text[0:5])
print(text[:10]) #[0:10]

#Desde una posición hasta el final 
print(text[5:])
print(text[:])

# Número de saltos
print(text[10:16:2])
print(text[::2])