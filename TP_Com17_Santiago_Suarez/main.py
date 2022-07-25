import mysql.connector
from funciones import *
from conexion_base_datos import *

#=============================FUNCIÓN CARGA DATOS========================================

def carga_datos():
  lista = []
  jugadores = 0

  #ingreso de datos
  nombre = input("\nNombre ('000' para finalizar): ")

  while nombre.upper() != "000" and jugadores < 27:

      apellido = input("Apellido: ")
    
      posicion = input("Posición (ARQ/DEF/MED/DEL): ")
      #chequeo posicion correcta
      while not posicion.upper() in ("ARQ","DEF","MED","DEL"):
        posicion = input("Por favor ingrese una posición válida (ARQ/DEF/MED/DEL): ")
        
      edad = input("Edad: ")
      #chequeo edad sea un numero de dos digitos
      while not edad.isdigit() or len(edad) != 2:
         edad = input("Por favor ingrese una edad válida: ")
        
      altura = input("Altura en centimetros: ")
      #chequeo altura sea un numero de tres digitos
      while not altura.isdigit() or len(altura) != 3:
         altura = input("Por favor ingrese una altura válida: ")
        
      partidos = input("Cantidad de partidos jugados: ")
      #chequeo partidos sea un numero
      while not partidos.isdigit():
        partidos = input("Por favor ingrese una cantidad válida: ")
        
      goles = input("Goles: ")
      #chequeo goles sea un numero
      while not goles.isdigit():
        goles = input("Por favor ingrese una cantidad válida: ")
      
      #chequeo cotizacion sea float
      while True:
        try:
          cotizacion = float(input("Cotización en millones US$: "))
          break
        except ValueError:
          print("Por favor ingresa un dato válido.")

      nombre = nombre.title()
      apellido = apellido.title()
      posicion = posicion.upper()
      edad = int(edad)
      altura = int(altura)
      partidos = int(partidos)
      goles = int(goles)
      cotizacion = cotizacion
    
      datos = [nombre,apellido,posicion,edad,altura,partidos,goles,cotizacion]
      lista.append(datos)
      jugadores = len(lista)

      #si se alcanzo el limite la carga finaliza sin volver a pedir el nombre
      if jugadores < 27:
        nombre = input("\nNombre: ")
      else:
        print("Limite de jugadores en el plantel alcanzado.")
  
  print("Carga finalizada.")
  return lista

#=============================DATOS CARGADOS============================================

#Lista generada con la función carga_datos
lista_datos = [['Lionel', 'Messi', 'DEL', 35, 169, 188, 86, 150.0], ['Lautaro', 'Martinez', 'DEL', 24, 174, 38, 20, 85.0], ['Franco', 'Armani', 'ARQ', 35, 188, 32, 0, 5.0], ['Emiliano', 'Martinez', 'ARQ', 30, 195, 31, 0, 65.5], ['Cristian', 'Romero', 'DEF', 24, 188, 19, 2, 80.0], ['Nicolas', 'Otamendi', 'DEF', 33, 181, 61, 4, 12.5], ['Rodrigo', 'De Paul', 'MED', 27, 181, 42, 6, 55.0], ['Julian', 'Alvarez', 'DEL', 22, 177, 9, 1, 50.0], ['Angel', 'Di Maria', 'DEL', 34, 181, 123, 22, 55.0], ['Gonzalo', 'Montiel', 'DEF', 24, 175, 15, 0, 25.0], ['Nahuel', 'Molina', 'DEF', 23, 177, 23, 0, 45.0], ['Marcos', 'Acuña', 'DEF', 31, 168, 55, 2, 30.9], ['Nicolas', 'Tagliafico', 'DEF', 29, 167, 56, 3, 20.0], ['German', 'Pezzella', 'DEF', 31, 186, 29, 1, 15.0], ['Paulo', 'Dybala', 'DEL', 28, 175, 23, 2, 85.5], ['Leandro', 'Paredes', 'MED', 28, 179, 38, 2, 40.0], ['Giovanni', 'Lo Celso', 'MED', 25, 177, 35, 1, 55.0]]

#=============================FUNCIÓN MENÚ========================================

def menu(lista):
  salir = False

  while not salir:
    print("============= MENÚ PRINCIPAL ==============")
    print("1 - Cargar datos.")
    print("2 - Ver plantel.")
    print("3 - Actualizar datos.")
    print("4 - Eliminar jugador.")
    print("5 - Obtener promedios.")
    print("6 - Filtrar estadisticas.")
    print("7 - Actualizar estadisticas.")
    print("8 - Exportar a base de datos MySQL.")
    print("0 - Salir.")
    op = input("Seleccionar una opción: ")
    print("===========================================")

    if op == "1":
      agrega_dato(lista_datos)

    elif op == "2":
      #opcion para filtrar por posicion
      # datos = ver_datos(lista_datos)
      # imprimir_plantel_ordenado(datos)

      #opcion sin filtrado
      lista2 = ordenar_lista(lista)
      imprimir_plantel_ordenado(lista2)

    elif op == "3":
      actualizar_datos(lista)

    elif op == "4":
      eliminar_dato(lista)

    elif op == "5":
      elegir_promedio(lista)

    elif op == "6":
      elegir_estadistica(lista)

    elif op == "7":
      actualizar_estadisticas(lista)

    elif op == "8":
      cargar_database(lista)

    elif op == "0":
      print("Saliendo del menú principal...")
      salir = True
      print("Hasta luego!")

    else:
      print("La opción ingresada no es válida.")

menu(lista_datos)