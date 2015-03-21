# Entrega de Seminario 02 - Grupo 5 - Perez Rivera, Antonio Miguel y Rivas Troncoso, Jose Ruben

# Ejercicio que devolvera una lista de palabras, lo mas larga posible,(mayor racha de palabras que cumplen el siguiente requisito) de aquellas palabras que acaben por una letra y las siguientes comiencen 
# por dicha letra.


# Usamos una unica funcion que obtendra la mayor concatenacion de palabras que cumplan
# el requisito de comenzar la siguiente por la letra que acabe la anterior.

def calculaListado(fichero):                                       # Se le pasa el nombre del fichero como parametro para realizar la lectura sobre el.

   todos = open(fichero,'r').read().split()                        # Lectura del fichero y traspaso de lo leido a una lista que llamamos "todos".

   actual = []                                                     # Usamos dos listas que seran "actual" y "masLarga" para almacenar de manera temporal las palabras
   masLarga = []                                                   # y actualizar sobre la lista "masLarga".

   for palabra in todos:                                           # Recorremos la lista de todos los Pokemons almacenados en la lista "todos".
   	
   	  actual.append(palabra)                                       # Se adhiere el pokemon en concreto sobre el que estemos a la lista de "actual".

   	  cont = 0                                                     # Usamos una variable auxiliar en este caso contador, para recorrer todos mientras haya elementos.

   	  while cont < len(todos):

   	  	if(todos[cont] not in actual and actual[-1][-1] == todos[cont][0]):    
   	  	   # Comprobacion si la palabra que tratamos no se encuentra en actual y cumple el requisito con la siguiente de fin e inicio de
   	  	   # letra correspondientemente.

   	  		actual.append(todos[cont])         # Si se cumple se adhiere a la lista y reiniciamos contador a 0, de lo contrario compara con los siguientes pokemons.

   	  		cont = 0
   	  	else:
   	  		cont = cont + 1


            

   	  if(len(actual)>len(masLarga)):              # Comprobacion simple acerca de la longitud de las listas actual con masLarga.
   	  	
   	  	masLarga[:] = []                          # Si la actual es mayor que la que teniamos en masLarga, borramos masLarga y machacamos con la actual.

   	  	masLarga += actual

   	  actual[:] = []                           # Actualizamos a vacia de nuevo, la lista "actual", para continuar con el procedimiento y seguir comparando palabras.

   print masLarga


## Funcion principal del programa (MAIN)

print "Mayor lista de palabras que cumplen los requisitos:"              # Impresion por pantalla del resultado de la cadena mayor que cumple los requisitos 
                                                                         # obtenida en la funcion calculaListado.
calculaListado("pokemon.txt")
