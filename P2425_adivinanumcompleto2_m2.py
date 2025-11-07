# Taller Programación y Robótica CMM BML – 2024 -2025 - Clase 4
# Nombre de programa : P_adivinanumerocompleto2_0.py
# Topicos nuevos: importar libreria, bloques, bucle while , flujo condicional if,
# ... cambiar tipos, tipado dinamico, operadores de comparacion
# Creditos : adaptacion de JCSP basado en "Invent with python" ed4 - cap. 3
# https://inventwithpython.com/invent4thed/chapter3.html
# Fecha JCSP 2023 02 09
# Licencia : CC BY-NC-SA 4.0
# https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es
# version 2.0 for -> while
# version 2.0 + Mejora 2 : condición de salida si se introduce 0 + condicion while mejorada

# 0 - BLOQUE PRESENTACION E INCIALIZACION DE JUEGO
import random # incorpora funciones adicionales, en este caso de numero aleatorios
# esta forma de importar mantiene los nuevos elementos seprados en una 'habitacion'
# llamda random, para usarlos priemro tenemso que 'ir' a la hanitacion 'random'

MAXINTENTOS = 6 # Las constantes se nombran en mayusculas por convencion (PEP 8)
print('¡Bienvenido el Juego de Adivina Numero - Completo v2.1 mejora 2')
tuNombre = input('Hola! ¿Cuál es tu nombre?')

numero = random.randint(1, 20) # funcion randint escoge un numero entero del 1 al 20
print('Vale, ' + tuNombre + ', he pensado un numero del 1 al 20.')

intentos = 0
numeroSupuesto = -1 # hay que dar un valor inicial para l priemr avez que entra en el while

# 1- BLOQUE JUEGO 2 de 3: Bucle de juego
while intentos < MAXINTENTOS and numeroSupuesto != numero and numeroSupuesto != 0:
# Formulacion logica alternativa
# while not(apuestas == MAXAPUESTAS or numeroSupuesto == numero or numeroSupuesto == 0):    
    
    numeroSupuesto = int(input('¡Intenta adivinarlo! Di un número ')) #cambio de tipo de cadena a entero
    intentos = intentos + 1 # actualizo el numero de apuestas hechas
    # intentos += 1 # esta forma es mas 'pitonica'
    if numeroSupuesto == 0:
        break # Sale del bucle
    
    if numeroSupuesto < numero:
        print('Tu número esta demasiado bajo.') # 8 espacios antes de "print"

    if numeroSupuesto > numero:
        print('Tu número esta demasiado alto.')

    if numeroSupuesto == numero:
        break # Sale de bucle

# 2- BLOQUE JUEGO 3 de 3: Final Ganas / Pierdes / Decides Salir
if numeroSupuesto == 0 :
    print('¡Decidiste salir del juego!')
elif numeroSupuesto == numero:
    print('Bien hecho, ' + tuNombre + ' adivinaste mi mumero en ', intentos, ' intentos')
    print('El numero que habia pensado era ', numero)
else:
    print('No adivinaste mi numero en ', MAXINTENTOS, ' intentos')
    print('El numero que habia pensado era ', numero)
    
