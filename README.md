# Reto-POO-No.1
### Punto 1
Crear una función que realice operaciones básicas (suma, resta, multiplicación, división) entre dos números, según la elección del usuario, la forma de entrada de la función será los dos operandos y el caracter usado para la operación. entrada: (1,2,"+"), salida (3).

**Idea:**
- Pedir al usuario los dos números y el signo.
- Usar `match case` para las operaciones.

### Punto 2
Realice una función que permita validar si una palabra es un palíndromo. Condición: No se vale hacer slicing para invertir la palabra y verificar que sea igual a la original.

**Idea:**
- Hacer una lista de palíndromos.
- Hacer una lista de palabras comunes.
- Crear una lista con ambos tipos de palabras.  
  (Por cada palabra en la tercera lista)
- Comparar el primer carácter con el último (sucesivamente, detenerse en la mitad de la palabra).
  - Si todas las comparaciones son iguales → La palabra es palíndroma.
  - Si no todas son iguales → La palabra no es palíndroma.
- Poner todos los palíndromos en una lista.
- Imprimir.

### Punto 3
Escribir una función que reciba una lista de números y devuelva solo aquellos que son primos. La función debe recibir una lista de enteros y retornar solo aquellos que sean primos.  

**Idea:**
- Crear una lista de números aleatorios de tamaño aleatorio.  
  Un número primo solo se puede dividir por 1 y por sí mismo.  
  (Por cada elemento *n* en la lista)
- Crear una lista de 1 hasta *n*.
- Dividir *n* por cada número de la lista.
- Si la división es entera en:
  - 2 ocasiones → *n* es primo.
  - Más de 2 ocasiones → *n* no es primo.
- Poner todos los números primos en una lista.
- Imprimir.

### Punto 4
Escribir una función que reciba una lista de números enteros y retorne la mayor suma entre dos elementos consecutivos.  

**Idea:**
- Crear una lista de números aleatorios de tamaño aleatorio.  
  (Por cada elemento *i* en la lista)
- Sumar *i* y el número siguiente, detenerse cuando la posición de *i* sea -1.
- Agregar todos los resultados a una lista.
- Ordenar la lista de mayor a menor.
- Imprimir el primer número de la lista.

### Punto 5
Escribir una función que reciba una lista de string y retorne unicamente aquellos elementos que tengan los mismos caracteres. e.g. entrada: ["amor", "roma", "perro"], salida ["amor", "roma"]

**Idea:**
- Pedir al usuario que ingrese las palabras.
- Hacer una lista con las palabras.  
  (Por cada palabra en la lista)  
  (Por cada letra)
  - Hallar ASCII.
- Guardar la palabra con su respectivo ASCII.
- Organizar los ASCII.
- Comparar cada palabra con las demás de la lista.
  - Si son iguales → agregar a una lista.
  - Si no → siguiente.
- Mostrar las palabras agregadas a la lista.
