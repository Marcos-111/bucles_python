#!/usr/bin/env python
'''
Bucles [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para que practiquen los conocimietos
adquiridos durante la semana
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

# Variable global utilizada para el ejercicio de nota
notas = [70, 82, -1, 65, 55, 67, 87, 92, -1]

# Variable global utilizada para el ejercicio de temperaturas
temp_dataloger = [12.8, 18.6, 14.5, 20.8, 12.1, 21.2, 13.5, 18.6,
                  14.7, 19.6, 11.2, 18.4]


def ej1():
    print('Comenzamos a ponernos serios!')

    '''
    Realice un programa que pida por consola dos números que representen
    el principio y fin de una secuencia numérica.
    Realizar un bucle "for" que recorra esa secuencia armada con "range"
    y cuante cuantes números ingresados hay y la sumatoria de todos los números
    Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
    sino que va hasta el anterior
    '''

    inicio = int(input("Ingrese el primer numero de la serie: \n"))
    fin = int(input("Ingrese el segundo numero de la serie: \n"))
    cantidad_numeros = 0
    sumatoria = 0
    
    
    for numero in range(inicio, fin):
        cantidad_numeros += 1
        sumatoria += numero
        continue
    print("cantidad de numeros: ", cantidad_numeros)
    print("La suma de todos los numeros es: ", sumatoria)

    # bucle.....

    # Al terminar el bucle calcular el promedio como:
    promedio = sumatoria / cantidad_numeros
    print("Promedio entre la sumatoria y la cantidad de numeros :", promedio)

    # Imprimir resultado en pantalla


def ej2():
    print("Mi Calculadora (^_^)")

    '''
    Tome el ejercicio de clase:
    <condicionales_python /  ejercicios_practica / ej3>,
    copielo a este ejercicio y modifíquelo, ahora se deberá ejecutar
    indefinidamente hasta que como operador se ingrese la palabra "FIN",
    en ese momento debe terminar el programa

    Se debe debe imprimir un cartel de error si el operador ingresado no es
    alguno de lo soportados o no es la palabra "FIN"
    '''
    
    numero_1 = 33
    numero_2 = 47
    suma = numero_1 + numero_2
    resta = numero_1 - numero_2
    multiplicacion = numero_1 * numero_2
    division = numero_1 / numero_2
    potencia = numero_1 ** numero_2
    condicion = True
    
    while condicion:
        # Inove: Como alternativa adicional, se podría solicitar el ingreso de los
        # numemeros numero_1 y numero_2 en cada iteracion de while para realizar
        # nuevos cálculos
        operador = str(input("Ingrese el simbolo de la operacion que desea ejecutar:\n"))
        
        if operador == "FIN":
            break
       
        elif operador == "+":
            print("El resultado de la suma entre",numero_1,"y",numero_2,"es",suma)
        
        elif operador == "-":
            print("El resultado de la resta entre",numero_1,"y",numero_2,"es",resta)

        elif operador == "*":
            print("El resultado de multiplicar",numero_1,"y",numero_2,"es",multiplicacion)
    
        elif operador == "/":
            print("El resultado de dividir",numero_1,"dividido",numero_2,"es",division)

        elif operador == "**":
            print("El resultado de",numero_1,"elevado a la",numero_2,"es",potencia)

        elif operador != "+" and "-" and "**" and "+" and "/":
            print("error")
            
       # Inove: La setencia elif operador != "+" and "-" and "**" and "+" and "/": no falla dado el contexto,
       # pero en realidad no está chequeando todas las condiciones, solo la primera, dado que para cada
       # sentencia condicional se debe agregar el o los "sujetos", a que me refiero:
       # elif operador != "+" and operador != "-" and operador != "**" and operador != "+" and operador != "/":
       # Ahora si se estaría evaluando en todos los casos contra "operador", se podría agregar "()" para mejorar
       # la interpretración a primera vista:
       # elif (operador != "+") and (operador != "-") and (operador != "**") and (operador != "+") and (operador != "/"):
       # ¿Por qué como estaba antes igual no fallaba? A pesar de no estar evaluando el operador contra todos los símbolos?
       # Esto es por los "elif" anidadso, en todos los "elif" anterior se fue evaluando contra todos los operadores
       # aceptados, por lo que al llegar al final, si se llega hasta ese "elif", es porque ya sabemos que el operador
       # no es válido. Conclusión podría directamente haberse reemplazado el último "elif" por:
       # else:
       #     print("Error, el operador ingresado {} es incorrecto!".format(operador))

def ej3():
    print("Mi organizador académico (#_#)")


    '''
    Tome el ejercicio de "calificaciones":
    <condicionales_python / ejercicios_clase / ej3>,
    copielo a este ejercicio y modifíquelo para cumplir
    el siguiente requerimiento

    Las notas del estudinte se encuentran almacenadas en una
    lista llamada "notas" que ya hemos definido al comienzo del archivo

    Debe caluclar el promedio de todas las notas y luego transformar
    la califiación en una letra según la escala establecida en el ejercicio
    "calificaciones" <condicionales_python / ejercicios_clase / ej3>

    A medida que recorre las notas, no debe considerar como válidas aquellas
    que son negativas, en ese caso el alumno estuvo ausente

    Debe contar la cantidad de notas válidas y la cantidad de ausentes
    '''

    # Para calcular el promedio primero debe obtener la suma
    # de todas las notas, que irá almacenando en esta variable
    sumatoria = 0           # Ya le hemos inicializado en 0

    cantidad_notas = 0      # Aquí debe contar cuantas notas válidas encontró
    cantidad_ausentes = 0   # Aquí debe contar cuantos ausentes hubo

    # Realice aquí el bucle para recorrer todas las notas
    # y cacular la sumatoria
    for numero in notas:
        if numero < 0:
            cantidad_ausentes += 1
        elif numero >= 0:
            cantidad_notas += 1
            sumatoria += numero
    # Terminado el bucle calcule el promedio como
    promedio = sumatoria / cantidad_notas

    if promedio >= 90:
        print("A")
    else:
        if promedio >= 80:
            print("B")
        else:
            if promedio >= 70:
                print("C")
            else:
                if promedio >= 60:
                    print("D")
                else:
                    if promedio < 60:
                        print("F")

    print("Cantidad de ausentes :",cantidad_ausentes)
    # Utilice la nota promedio calculada y transformela
    # a calificación con letras, imprima en pantalla el resultado

    # Imprima en pantalla al cantidad de ausentes


def ej4():
    print("Mi primer pasito en data analytics")

    '''
    Tome el ejercicio:
    <condicionales_python / ejercicios_practica /ej5>,
    copielo a este ejercicio y modifíquelo para cumplir el
    siguiente requerimiento

    En este ejercicio se lo provee de una lista de temperatuas,
    esa lista de temperatuas corresponde a los valores de temperaturas
    tomados durante una temperorada del año en Buenos Aires.
    Ustede deberá analizar dicha lista para deducir
    en que temporada del año se realizó el muestreo de temperatura.
    La variable con la lista de temperaturas se llama "temp_dataloger"
    definida al comienzo del archivo

    Debe recorrer la lista "temp_dataloger" y obtener los siguientes
    resultados

    1 - Obtener la máxima temperatura
    2 - Obtener la mínima temperatura
    3 - Obtener el promedio de las temperatuas

    Los resultados se deberán almacenar en las siguientes variables
    que ya hemos preparado para usted
    '''

    temperatura_max = None      # Aquí debe ir almacenando la temp máxima
    temperatura_min = None      # Aquí debe ir almacenando la temp mínima
    temperatura_sumatoria = 0   # Aquí debe ir almacenando la suma de todas las temp
    temperatura_promedio = 0    # Al finalizar el loop deberá aquí alamcenar el promedio
    temperatura_len = 0         # Aquí debe almacenar cuantas temperatuas hay en la lista

    
    
    for temperatura in temp_dataloger:

        if (temperatura_max is None) or (temperatura > temperatura_max):
            temperatura_max = temperatura

        elif (temperatura_min is None) or (temperatura < temperatura_min):
            temperatura_min = temperatura

        temperatura_sumatoria += temperatura
        temperatura_len = len(temp_dataloger)   # Inove: Este cálculo podría ejecutarse una única vez fuera del bucle
        temperatura_promedio = temperatura_sumatoria / temperatura_len # Inove: Este cálculo podría ejecutarse una única vez fuera del bucle

    
        
    print("Máxima temperatura: ", temperatura_max)
    print("Máxima temperatura con Python = ", max(temp_dataloger))

    print("Minima temperatura: ", temperatura_min)
    print("Minima temperatura con Python = ", min(temp_dataloger))

    print("Sumatoria temperaturas: ", temperatura_sumatoria)
    print("Sumatoria temperaturas con Python = ", sum(temp_dataloger))

    print("Cantidad de temperaturas: ", temperatura_len)
    print("La temperatura promedio es: ", temperatura_promedio)
        




    

    # Al finalizar el bucle compare si el valor que usted calculó para
    # temperatura_max y temperatura_min coincide con el que podría calcular
    # usando la función "max" y la función "min" de python
    # función "max" --> https://www.w3schools.com/python/ref_func_max.asp
    # función "min" --> https://www.w3schools.com/python/ref_func_min.asp

    # Al finalizar el bucle debe calcular el promedio como:
    # temperatura_promedio = temperatura_sumatoria / cantidad_temperatuas

    # Corroboren los resultados de temperatura_sumatoria
    # usando la función "sum"
    # función "sum" --> https://www.w3schools.com/python/ref_func_sum.asp

    '''
    Una vez que tengamos nuestros valores correctamente calculados debemos
    determinar en que epoca del año nos encontramos en Buenos Aires utilizando
    la estadística de años anteriores. Basados en el siguiente link realizamos
    las siguientes aproximaciones:

    verano -->      min = 19, max = 28
    otoño -->       min = 11, max = 24
    invierno -->    min = 8, max = 14
    primavera -->   min = 10, max = 24

    Referencia:
    https://es.weatherspark.com/y/28981/Clima-promedio-en-Buenos-Aires-Argentina-durante-todo-el-a%C3%B1o
    '''
    if temperatura_max and temperatura_min:
        
        if temperatura_max <= 28 and temperatura_min >= 19:
            print("Verano")
        elif temperatura_max <= 24 and temperatura_min >= 11:
            print("Otoño")
        elif temperatura_max <= 14 and temperatura_min >= 8:
            print("Invierno")
        elif temperatura_max <= 24 and temperatura_min >= 10:
            print("Primavera")
        
        
         
    # En base a los rangos de temperatura de cada estación,
    # ¿En qué época del año nos encontramos?
    # Imprima el resultado en pantalla
    # Debe utilizar temperatura_max y temperatura_min para definirlo


def ej5():
    print("Ahora sí! buena suerte :)")

    condicion = True
    lista_palabras = []
    palabra_oa = None
    palabra_cl = None

    while condicion:
        accion = int(input("Ingrese 1 para orden alfabetico 2 para orden segun cantidad de letras o 3 para finalizar:\n"))
        if accion != 1 and accion != 2 and accion != 3:
            print("ERROR")
        
        elif accion == 3:
            print("Programa finalizado")
            break

        elif accion == 1 or 2:

            if accion == 1 or 2:

                # Inove: Esta perfecto el procedimiento de solicitar 3 palabras
                # como alternativa (para automatizarlo) se podría utilizar un bucle para ello:
                # palabras_deseadas = 3
                # for i in range(palabras_deseadas):
                #     palabra = str(input("Ingrese la palabra", i, ":\n"))
                #     lista_palabras.append(palabra)
                
                palabra_1 = str(input("Ingrese la primera palabra:\n"))
                lista_palabras.append(palabra_1)
                
                palabra_2 = str(input("Ingrese la segunda palabra:\n"))
                lista_palabras.append(palabra_2)

                palabra_3 = str(input("Ingrese la tercera palabra:\n"))
                lista_palabras.append(palabra_3)

                if accion == 1:
                    for palabra in lista_palabras:
                        if (palabra_oa is None) or (palabra > palabra_oa):
                            palabra_oa = palabra
                    print(lista_palabras)
                    print("Palabra mas grande alfaneticamente: ",palabra_oa)
                    lista_palabras = []    
                    # Inove: Excelente! Muy bien el detalle de vaciar la lista!
                    # Como notar de color está perfecto utilizar lista_palabras = []
                    # Hay un método de "lista" que hace justamente este trabajo, y es "clear()"
                    # lista_palabras.clear()
                    # Lo dejo como nota de color ya que a la "vista" se entiende de primera
                    # que la intención fue vaciar la lista.
                    

                elif accion == 2:
                    for palabra in lista_palabras:
                        if(palabra_cl is None) or (len(palabra) > len(palabra_cl)):
                            palabra_cl = palabra
                    print(lista_palabras)
                    print("Palabra con mayor cantidad de letras: ",palabra_cl)
                    lista_palabras = []

                    

        






    '''
    Tome el ejercicio:
    <condicionales_python / ejercicios_practica / ej4>,
    copielo a este ejercicio y modifíquelo para cumplir
    el siguiente requerimiento

    Realize un programa que corra indefinidamente en un bucle, al comienzo de la
    iteración del bucle el programa consultará al usuario con el siguiente menú:
    1 - Ordenar por orden alfabético (usando el operador ">")
    2 - Ordenar por cantidad de letras (longitud de la palabra)
    3 - Salir del programa

    En caso de presionar "3" el programa debe terminar e informar por
    pantalla de que ha acabado,
    en caso contrario si se presionar "1" o "2" debe continuar con la siguiente tarea

    NOTA: Si se ingresa otro valor que no sea 1, 2 o 3 se debe enviar
    un mensaje de error y volver a comenzar el bucle
    (vea en el apunte "Bucles - Sentencias" para encontrar
    la sentencia que lo ayude a cumplir esa tarea)

    Si el bucle continua (se presionó "1" o "2") se debe ingresar a otro bucle
    en donde en cada iteración se pedirá una palabra. La cantidad de iteración
    (cantidad de palabras a solicitar) lo dejamos a gusto del alumno, intente que esa
    condición esté dada por una variable (ej: palabras_deseadas = 4)
    Cada palabra ingresada se debe ir almacenando en una lista de palabras, dicha
    lista la debe inicializar vacia y agregar cada nuevo valor con el método "append".
    Luego de tener las palabras deseadas almacenadas en una lista de palabras
    se debe proceder a realizar las siguientes tareas:

    Si se ingresa "1" por consola se debe obtener la palabra
    más grande por orden alfabético
    Luego de terminar de recorrer toda la lista (utilizar un bucle "for")
    se debe imprimir en pantalla cual era la palabra
    más grande alfabeticamente.
    Recuerde que debe inicializar primero su variable
    donde irá almacenando la palabra que cumpla dicha condición.
    ¿Con qué valor debería ser inicializada dicha variable?

    Si se ingresa "2" por consola se debe obtener la palabra
    con mayor cantidad de letras
    Luego de terminar de recorrer toda la lista (utilizar un bucle "for")
    se debe imprimir en pantalla cual era la palabra con
    mayor cantidad de letras.
    Recuerde que debe inicializar primero su variable
    donde irá almacenando la palabra que cumpla dicha condición.
    ¿Con qué valor debería ser inicializada dicha variable?

    NOTA: Es recomendable que se organice con lápiz y papel para
    hacer un bosquejo del sistema ya que deberá utilizar 3 bucles en total,
    1 - El bucle principal que hace que el programa corra hasta ingresar un "3"
    2 - Un bucle interno que corre hasta socilitar todas las palabras deseadas
        que se deben ir guardando en una lista
    3- Otro bucle interno que corre luego de que termine el bucle "2" que
       recorre la lista de palabras y busca la mayor según el motivo ingresado ("1" o "2")

  '''
    

   

if __name__ == '__main__':
    print("Ejercicios de práctica")
    ej1()
    #ej2()
    #ej3()
    #ej4()
    #ej5()
