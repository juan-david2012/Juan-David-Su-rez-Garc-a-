#esto es un comentario de una sola linea
"""esto es un comentario
de varias lineas"""

#inicializando variables
nombre="Juan David Suarez Garcia"
edad=14
estado=True
nota=5.0

#mostrar el contenido de las variables print ()
print(nombre)
print(edad)
print(estado)
print(nota)

#que tipo de dato tiene cada variable
print(type(nombre))
print(type(edad))
print(type(estado))
print(type(nota))

#vamos a utilizar la funcion input para recolectar datos del teclado
nombre=input(" ¿como te llamas? ")
edad=input(" ¿que edad tienes? ")
estado=input(" ¿cual es tu estado? ")
nota=input("¿cual es tu nota?")

#para visualizar que guardamos en las variables anteriores
print("hola" , nombre, "un gusto conocerte")
print("tu edad es =" , edad)
print("tu estado es =" , estado)
print("tu nota es =" , nota)