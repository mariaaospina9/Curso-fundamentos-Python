# Curso-fundamentos-Python
Ejercicios de curso práctico de platzi

##  ¿Por que utilizar Python? ##
1. Python siempre ocupa los primeros puestos de los lenguajes mas queridos. En el año 2021 en la encuesta realizada por "Developer Survey" ocupa el cuarto puesto.

2. Es fácil de aprender. Su curva de aprendizaje no es tan pronunciada.

3. Esta en el top 20 de los lenguajes de programación mejor pagos.

4. Puede ser utilizado en diferentes áreas, especialmente en Análisis de datos (51%) y desarrollo web (45%).

5. Tiene una gran demanda laboral en el mundo de la tecnología.

## Herrameintas utilizadas en el curso ##

Se utilizará "Replit" que permite realizar códigos desde el navegador 

## Algunas herramientas de la industria ##

1. **Visual Studio Code** que es un editos de código.

2. **Terminal y línea de comandos** en diversos sistemas operativos.

3. **Jupyter Notebooks** para data science.

4. **Git** para control de versiones.

5. Para entornos virtuales con **PIP**.

6. Para entornos integrados de desarrollo (IDE) como **PyCharm, Visual Studio o DataSpell**.

![Herramientas](Herramientas.jpg)

## Print () ##

Se utiliza para imprimir notas o resultados 

```python
print("Hola, mi nombre es Maria Antonia")
```
## Uso de las comillas triples y numeral ##

Se utilizan normalmente para dejar comentarios entre líneas

```python
# Dejar comentarios entre lineas
""" Dejar comentarios un poco mas 
extensos """
```
## Variables de programación ## 

Todas las variables están nombradas para ser reconocidas durante la ejecución del código 

```python
my name= "Maria"
print("Mi nombre es",my_name)
```

## Input

Se utiliza para obtener una entrada de texto del usuario a través de la consola

```python
my_name= input("¿Cuál es tu nombre?")
print("Mi nombre es", my name)
```
# Tipos de datos

## Tipos de datos primitivos

**Strings:** Cadena de caracteres (texto)

```python
my name="Maria"
print("myname =>", my name)

#Para diferenciar la variable
print(type(my_name))
```

**Integers:** Números Enteros

```python
my_age=12
print("my age", my_age)
print(tupe(my_age))
```

**Boolean:** Boolenaos (Verdadero o Falso)

```python
is_single = True
print("is_single => ", is_single)
print(type(is_single))
```

**Floats:** Números de punto flotante (decimales)

## Tipos de dato adicionales

**- Datos en texto:** str

**- Datos numéricos:** int, float, complex

**- Datos en secuencia:** list, tuple, range

**- Datos de mapeo:** dict

**- Set Types:** set, frozenset

**- Datos booleanos:** bool

**- Datos binarios:** bytes, bytearray, memoryview

# Strings

*Cadena de caracteres (texto)*

```python
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
```
# Numbers


*Las variables tipo numero pueden ser enteras o flotantes y siempre se declaran sin estar encerradas entre comillas ya que de lo contrario serian tipo string.*

## Int
```python
lives = 3
print(type(lives))
```

## Float 
```python
temperature = 12.12
print(type(temperature))
```
*Podemos realizar operaciones con la misma variable y para esto tenemos 2 formas de hacerlo, la cual la segunda es la forma simplificada donde se utilizan operadores de asignacion*

```python
lives = lives - 1
lives - =1
print(lives)

lives + =5
print(lives)
```

*Python nos muestra en notación científica números cuyo valor es muy grande o muy pequeño*

```python
#Valores extremadamente grandes 
number = 45000000000000000000000000000
print(number)

#Valores extremadamente pequeños
number_b= 0.00000000001
print(number_b)
```
## Booleans

*Tipo de dato que solo tiene 2 estados: True o False, y nos permiten saber si un objeto tiene o no un estado*

```python
is_single= True
print(type(is_single))
is_singlesigle= False
print(is_single)

#Para invertir el valor
print(not True)
print(not False)

is_single= not is_single
print(is_single)
```

# Transformación de datos

Pasar un dato hacia un string para utilizarlo en la función print()

```python
age = input("Escribe tu edad")
print(type(age))
age = int(age)
age += 10
print(f"Tu edad en 10 años será {age}")
```

# Operadores aritméticos 

Nos permiten reliazar cálculos tales como suma (+), resta (-), multuplicación (*), división (/), residuo (%), división con valor entero (//) y exponenciación (**) 

``` python 
print (10 + 20)
print (10 - 5)
print (10 * 2)
print (10/2)

#Contanenación
print( "Hola" + "mundo")

#Repetición de cadena
print("Hola" *3)

#Operador de módulo - residuo 
print (10 % 2)

#Operador de módulo entero 
print(10//3)

#Operador exponencial 
print(2**3)
print(2**3 + 3 - 7 /1)
```

*Se debe de tener en cuenta la prioridad de la ecuación*

![PEMDAS](PEMDAS.JPG)

# Operadores de comparación 

Comparan dos expresiones y devuelven un valor Boolean que representa la relación de sus valores

![OperadoresComparacion](OperadoresComparacion.JPG)


``` python 
# >
print(7>3)
print (3>7)

# <
print (5>6)
print(6<5)

# >=
print(2 >= 1)
print(2 >= 3)
print(2 >= 2)

age = 18
print(age >= 18)

# ==
print (6==6)
print("Apple" == "Apple")
print("1"==1) #Son diferentes

# != Valor diferente
print(6 != 10)
```
