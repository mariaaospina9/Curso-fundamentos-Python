text = "Ella sabe programar en Python"
print("JavaScript" in text)
print("Python" in text)

if "Python" in text:
  print("Elegiste bien!")
else:
  print("Tambien elegiste bien")

#TAMAÑO DE TEXTO 
size = len("text")
print(size)

#Mayusculas
print(text)
print(text.upper())

#Minusculas
print(text.lower())

#Número de apariciones de una letra
print(text.count("a"))

#Pasar lo que esta en min a may y de may a min
print(text.swapcase())

#El texto inicia con...
print(text.startswith("Ella"))

#El texto finaliza con...
print(text.endswith("Python"))

#Reemplazar
print(text.replace("Python", "Go"))

#Poner el primer caracter en mayuscula
text_2 = "este es un titulo"
print(text_2)
print(text_2.capitalize())

#Incio de cada palabra en mayuscula
print(text_2.title())

#Saber ssi es un digito 
print(text_2.isdigit())