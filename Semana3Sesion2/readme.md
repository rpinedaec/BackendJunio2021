# Ejercicios « Introducción informal

## Ejercicio 1


Identifica el tipo de dato (int, float, string o list) de los siguientes valores literales:

"Hola Mundo"     
[1, 10, 100]      
-25              
1.167             
["Hola", "Mundo"] 


## Ejercicio 2

Determina mentalmente (sin programar) el resultado que aparecerá por pantalla en las siguientes operaciones con variables:

a = 10

b = -5

c = "Hola "

d = [1, 2, 3] 

print(a * 5)

print(a - b)

print(c + "Mundo")

print(c * 2)

print(d[-1])

print(d[1:])

print(d + d) 

## Ejercicio 3

El siguiente código pretende realizar una media entre 3 números, pero no funciona correctamente. ¿Eres capaz de identificar el problema y solucionarlo?

numero_1 = 9
numero_2 = 3
numero_3 = 6

media = numero_1 + numero_2 + numero_3 / 3

print("La nota media es", media)  

## Ejercicio 4

A partir del ejercicio anterior, vamos a suponer que cada número es una nota, y lo que queremos es obtener la nota final. El problema es que cada nota tiene un valor porcentual:

-   La primera nota vale un 15% del total
-   La segunda nota vale un 35% del total
-   La tercera nota vale un 50% del total

Desarrolla un programa para calcular perfectamente la nota final:

nota_1 = 10

nota_2 = 7

nota_3 = 4

## Ejercicio 5

La siguiente matriz (o lista con listas anidadas) debe cumplir una condición, y es que en cada fila el cuarto elemento siempre debe ser el resultado de sumar los tres primeros. ¿Eres capaz de modificar las sumas incorrectas utilizando la técnica del slicing?

Ayuda

La función llamada  _sum(lista)_  devuelve una suma de todos los elementos de la lista ¡Pruébalo!

matriz =
[ 

    [1, 1, 1, 3],
    [2, 2, 2, 7],
    [3, 3, 3, 9],
    [4, 4, 4, 13]
]

## Ejercicio 6

Al realizar una consulta en un registro hemos obtenido una cadena de texto corrupta al revés. Al parecer contiene el nombre de un alumno y la nota de un exámen. ¿Cómo podríamos formatear la cadena y conseguir una estructura como la siguiente?

> **_Nombre_**  **_Apellido_**  ha sacado un  **_Nota_**  de nota.

# Ejercicios « Operadores y expresiones

## Ejercicio 1

Realiza un programa que lea 2 números por teclado y determine los siguientes aspectos (es suficiene con mostrar True o False):

-   Si los dos números son iguales
-   Si los dos números son diferentes
-   Si el primero es mayor que el segundo
-   Si el segundo es mayor o igual que el primero

## Ejercicio 2

Utilizando operadores lógicos, determina si una cadena de texto introducida por el usuario tiene una longitud mayor o igual que 3 y a su vez es menor que 10 (es suficiene con mostrar True o False).

## Ejercicio 3

Realiza un programa que cumpla el siguiente algoritmo utilizando siempre que sea posible operadores en asignación:

-   Guarda en una variable numero_magico el valor 12345679 (sin el 8)
-   Lee por pantalla otro numero_usuario, especifica que sea entre 1 y 9
-   Multiplica el numero_usuario por 9 en sí mismo
-   Multiplica el numero_magico por el numero_usuario en sí mismo
-   Finalmente muestra el valor final del numero_magico por pantalla


# Ejercicios « Colecciones de datos

## Ejercicio 1

Realiza un programa que siga las siguientes instrucciones:

-   Crea un conjunto llamado usuarios con los usuarios Marta, David, Elvira, Juan y Marcos
-   Crea un conjunto llamado administradores con los administradores Juan y Marta.
-   Borra al administrador Juan del conjunto de administradores.
-   Añade a Marcos como un nuevo administrador, pero no lo borres del conjunto de usuarios.
-   Muestra todos los usuarios por pantalla de forma dinámica, además debes indicar cada usuario es administrador o no.

Sugerencia

Los conjuntos se pueden recorrer dinámicamente utilizando el bucle  **for**  de forma similar a una lista.  
También cuentan con un método llamado  **.discard(elemento)**  que sirve para borrar o descartar un elemento.

## Ejercicio 2

Durante el desarrollo de un pequeño videojuego se te encarga configurar y balancear cada clase de personaje jugable. Partiendo que la estadística base es 2, debes cumplir las siguientes condiciones:

-   El caballero tiene el doble de vida y defensa que un guerrero.
-   El guerrero tiene el doble de ataque y alcance que un caballero.
-   El arquero tiene la misma vida y ataque que un guerrero, pero la mitad de su defensa y el doble de su alcance.
-   Muestra como quedan las propiedades de los tres personajes.

## Ejercicio 3

Durante la planificación de un proyecto se han acordado una lista de tareas. Para cada una de estas tareas se ha asignado un orden de prioridad (cuanto menor es el número de orden, más prioridad).

¿Eres capaz de crear una estructura del tipo cola con todas las tareas ordenadas pero sin los números de orden?

# Ejercicios « Entradas y salidas de datos

## Ejercicio 1

Formatea los siguientes valores para mostrar el resultado indicado:

-   "Hola Mundo" → Alineado a la derecha en 20 caracteres
-   "Hola Mundo" → Truncamiento en el cuarto carácter (índice 3)
-   "Hola Mundo" → Alineamiento al centro en 20 caracteres con truncamiento en el segundo carácter (índice 1)
-   150 → Formateo a 5 números enteros rellenados con ceros
-   7887 → Formateo a 7 números enteros rellenados con espacios
-   20.02 → Formateo a 3 números enteros y 3 números decimales

## Ejercicio 2

Crea un script llamado  **tabla.py**  que realice las siguientes tareas:

-   Debe tomar 2 argumentos, ambos números enteros positivos del 1 al 9, sino mostrará un error.
-   El primer argumento hará referencia a las filas de una tabla, el segundo a las columnas.
-   En caso de no recibir uno o ambos argumentos, debe mostrar información acerca de cómo utilizar el script.
-   El script contendrá un bucle for que itere el número de veces del primer argumento.
-   Dentro del for, añade un segundo for que itere el número de veces del segundo argumento.
-   Dentro del segundo for ejecuta una instrucción  **print(" * ", end='')**,  _(**end=''*_  evita el salto de línea)*.
-   Ejecuta el código y observa el resultado.
-   Intenta deducir dónde y cómo añadir otra instruccion  _print()_  para dibujar una tabla.

Recordatorio

Recordatorio: Los argumentos se envían como cadenas separadas por espacios, si quieres enviar varias palabras como un argumento deberás indicarlas entre comillas dobles "esto es un argumento". Para capturar los argumentos debes utilizar el módulo  **sys**  y su lista  **argv**:

`import sys
print(sys.argv) # argumentos enviados` 

## Ejercicio 3

Crea un script llamado  **descomposicion.py**  que realice las siguientes tareas:

-   Debe tomar 1 argumento que será un número entero positivo.
-   En caso de no recibir un argumento, debe mostrar información acerca de cómo utilizar el script.

El objetivo del script es descomponer el número en unidades, decenas, centenas, miles... tal que por ejemplo si se introduce el número 3647:

`python descomposicion.py 3647` 

El programa deberá devolver una descomposición línea a línea como la siguiente utilizando las técnicas de formateo:

0007

0040

0600

3000

Pista

Que el valor sea un número no significa necesariamente que deba serlo para formatearlo. Necesitarás jugar muy bien con los índices y realizar muchas conversiones entre tipos cadenas, números y viceversa

# Ejercicios « Programación de funciones

## Ejercicio 1

Realiza una función llamada  **area_rectangulo(base, altura)**  que devuelva el área del rectangulo a partir de una base y una altura. Calcula el área de un rectángulo de 15 de base y 10 de altura:

Recordatorio

El área de un rectángulo se obtiene al multiplicar la base por la altura.

## Ejercicio 2

Realiza una función llamada  **area_circulo(radio)**  que devuelva el área de un círculo a partir de un radio. Calcula el área de un círculo de 5 de radio:

Recordatorio

El área de un círculo se obtiene al elevar el radio a dos y multiplicando el resultado por el número pi. Puedes utilizar el valor 3.14159 como pi o importarlo del módulo math:

`import math`

`print(math.pi) `

`3.141592653589793` 

## Ejercicio 3

Realiza una función llamada  **relacion(a, b)**  que a partir de dos números cumpla lo siguiente:

-   Si el primer número es mayor que el segundo, debe devolver 1.
-   Si el primer número es menor que el segundo, debe devolver -1.
-   Si ambos números son iguales, debe devolver un 0.

Comprueba la relación entre los números: '5 y 10', '10 y 5' y '5 y 5'.

## Ejercicio 4

Realiza una función llamada  **intermedio(a, b)**  que a partir de dos números, devuelva su punto intermedio. Cuando lo tengas comprueba el punto intermedio entre -12 y 24:

Recordatorio

El número intermedio de dos números corresponde a la suma de los dos números dividida entre 2

## Ejercicio 5

Realiza una función llamada  **recortar(numero, minimo, maximo)**  que reciba tres parámetros. El primero es el número a recortar, el segundo es el límite inferior y el tercero el límite superior. La función tendrá que cumplir lo siguiente:

-   Devolver el límite inferior si el número es menor que éste
-   Devolver el límite superior si el número es mayor que éste.
-   Devolver el número sin cambios si no se supera ningún límite.

Comprueba el resultado de recortar 15 entre los límites 0 y 10.

## Ejercicio 6

Realiza una función  **separar(lista)**  que tome una lista de números enteros y devuelva dos listas ordenadas. La primera con los números pares y la segunda con los números impares.

Por ejemplo:

`pares, impares = separar([6,5,2,1,7])`

`print(pares)`

`print(impares)` 

`[2, 6]`

`[1, 5, 7]` 

Sugerencia

Para ordenar una lista automáticamente puedes utilizar el método  _.sort()_.

# Ejercicios « Métodos de las colecciones

## Ejercicio 1

Utilizando todo lo que sabes sobre cadenas, listas, sus métodos internos... Transforma este texto:

`un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro` 

En este otro:

Un día que el viento soplaba con fuerza...
- Mira como se mueve aquella banderola -dijo un monje.
- Lo que se mueve es el viento -respondió otro monje.
- Ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro.

**Lo único prohibido es modificar directamente el texto.**

## Ejercicio 2

Crea una función modificar() que a partir de una lista de números realice las siguientes tareas sin modificar la original:

-   Borrar los elementos duplicados.
-   Ordenar la lista de mayor a menor.
-   Eliminar todos los números impares.
-   Realizar una suma de todos los números que quedan.
-   Añadir como primer elemento de la lista la suma realizada.
-   Devolver la lista modificada.
-   Finalmente, después de ejecutar la función, comprueba que la suma de todos los números a partir del segundo, concuerda con el primer número de la lista, tal que así:

`nueva_lista = modificar(lista)`

`print( nueva_lista[0] == sum(nueva_lista[1:]) )` 

`True` 

Recordatorio

La función  _sum(lista)_  devuelve una suma de los elementos de una lista.

# Ejercicios « Módulos y paquetes

## Ejercicio 1

Crea el siguiente módulo:

-   El módulo se denominará  **operaciones.py**  y contendrá 4 funciones para realizar una  **suma**, una  **resta**, un  **producto**  y una  **division**  entres dos números. Todas ellas devolverán el resultado.
-   En las funciones del módulo deberá de haber tratamiento e invocación manual de errores para evitar que se quede bloqueada una funcionalidad, eso incluye:
    
    -   _TypeError_: En caso de que se envíen valores a las funciones que no sean números. Además deberá aparecer un mensaje que informe  **Error: Tipo de dato no válido**.
    -   _ZeroDivisionError_: En caso de realizar una división por cero. Además deberá aparecer un mensaje que informe  **Error: No es posible dividir entre cero**.

Una vez creado el módulo, crea un script  **calculos.py**  en el mismo directorio en el que deberás importar el módulo y realizar las siguientes instrucciones. Observa si el comportamiento es el esperado:

`from operaciones import * `

`a, b, c, d = (10, 5, 0, "Hola")`

print( "{} + {} = {}".format(a, b, suma(a, b) ) )

print( "{} - {} = {}".format(b, d, resta(b, d) ) )

print( "{} * {} = {}".format(b, b, producto(b, b) ) ) 

print( "{} / {} = {}".format(a, c, division(a, c) ) )

## Ejercicio 2

¿Eres capaz de desarrollar un reloj de horas, minutos y segundos utilizando el módulo datetime con la hora actual? Hazlo en un script llamado  **reloj.py**  y ejecútalo en la terminal:

Ayuda

El módulo  **time**  integra una función llamada  **sleep(segundos)**  que puede pausar la ejecución de un programa durante un tiempo. Así mismo el módulo  **os**  integra la función  **system('cls')**  y  **system('clear')**  para limpiar la pantalla de la terminal en sistemas Windows y Linux/Unix respecticamente.

## Ejercicio 3

Crea un script llamado  **generador.py**  que cumpla las siguientes necesidades:

-   Debe incluir una función llamada  **leer_numero()**. Esta función tomará 3 valores:  **ini**,  **fin**  y  **mensaje**. El objetivo es leer por pantalla un número >= que ini y <= que fin. Además a la hora de hacer la lectura se mostrará en el input el  **mensaje**  enviado a la función. Finalmente se devolverá el valor. Esta función tiene que devolver un número, y tiene que repetirse hasta que el usuario no lo escriba bien (lo que incluye cualquier valor que no sea un número del ini al fin).
-   Una vez la tengas creada, deberás crear una nueva función llamada generador, no recibirá ningún parámetro. Dentro leerás dos números con la función  **leer_numero()**:
    
    -   El primer numero será llamado  **numeros**, deberá ser entre 1 y 20, ambos incluidos, y se mostrará el mensaje  **¿Cuantos números quieres generar? [1-20]:**
    -   El segundo número será llamado  **modo**  y requerirá un número entre 1 y 3, ambos incluidos. El mensaje que mostrará será:  **¿Cómo quieres redondear los números? [1]Al alza [2]A la baja [3]Normal:**.
-   Una vez sepas los números a generar y cómo redondearlos, tendrás que realizar lo siguiente:
    
    -   Generarás una lista de  **números aleatorios decimales**  entre 0 y 100 con tantos números como el usuario haya indicado.
    -   A cada uno de esos números deberás redondearlos en función de lo que el usuario ha especificado en el modo.
    -   Para cada número muestra durante el redondeo, el número normal y después del redondeo.
-   Finalmente devolverás la lista de números redondeados.
    

El objetivo de este ejercicio es practicar la reutilización de código y los módulos random y math.

Recordatorio

El redondeo tradicional  _round()_  no requiere importar ningún módulo, es una función por defecto.