# Taller Programación y Robótica CMM BML – 2024 -2025 - Clase 4
# Nombre de programa : P_adivinanumsimple.py
# Topicos nuevos: importar libreria, bloques, flujo condicional if,
# ... cambiar tipos, tipado dinamico, operadores de comparacion
# Creditos : adaptacion simplificada de JCSP basado en "Invent with python" ed4 - cap. 3
# https://inventwithpython.com/invent4thed/chapter3.html
# Fecha JCSP 2023 02 09
# Licencia : CC BY-NC-SA 4.0
# https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es
# v 2.0 ligeras mejoras y comentarios

import random # incorpora funciones adicionales, en este caso de numero aleatorios
# esta forma de importar mantiene los nuevos elementos seprados en una 'habitacion'
# llamda random, para usarlos priemro tenemso que 'ir' a al hanitacion 'random'

# 0 - FASE PRESENTACION E INCIALIZACION DE JUEGO
print('¡Bienvenido el Juego de Adivina Numero - Simple v2')
tuNombre = input('Hola! ¿Cuál es tu nombre?')

numero = random.randint(1, 20) # funcion randint escoge un numero entero del 1 al 20
print('Vale, ' + tuNombre + ', he pensado un numero del 1 al 20.')

#1- FASE DE JUEGO EN SI (sin bucle en este caso) 
numeroSupuesto = int(input('¡Intenta adivinarlo! Di un número ')) #cambio de tipo de cadena a entero

if numeroSupuesto < numero:
    print('Tu numero esta demasiado bajo.') # 4 espacios antes de "print"
    print('Lo siento no lo adivinaste')

if numeroSupuesto > numero:
    print('Tu numero esta demasiado alto.')
    print('Lo siento no lo adivinaste')

if numeroSupuesto == numero:
    print('Bien hecho, ' + tuNombre + ' adivinaste mi mumero')

#2- FIN DEL JUEGO
print('El numero que habia pensado era ', numero)
