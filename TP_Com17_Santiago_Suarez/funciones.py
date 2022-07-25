#==========================FUNCIONES 1 (CARGAR DATOS)===============================================

#Funcion para eliminar tildes, se usará cada vez que se ingrese un nombre y apellido para evitar problemas de comparación.
def sin_tildes(palabra):
  reemplazar = (("á", "a"),("é", "e"),("í", "i"),("ó", "o"),("ú", "u"))

  for i, j in reemplazar:
    palabra = palabra.replace(i, j).replace(i.upper(), j.upper())

  return palabra

#Función que permite ingresar datos a la lista previamente cargada
def agrega_dato(lista):
  jugadores = len(lista)

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

      #se convierte cada variable al formato deseado antes de agregar a la lista
      nombre = nombre.title()
      apellido = sin_tildes(apellido.title())
      posicion = sin_tildes(posicion.upper())
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

#=================================FUNCIONES 2 (VER PLANTEL)=================================================

#Función que recorre la lista principal y devuelve otra con los mismos datos, pero ordenados por posición
def ordenar_lista(lista):
  lista2 = []

  for arquero in lista:
    if arquero[2] == "ARQ":
      lista2.append(arquero)

  for defensor in lista:
    if defensor[2] == "DEF":
      lista2.append(defensor)

  for medio in lista:
    if medio[2] == "MED":
      lista2.append(medio)

  for delantero in lista:
    if delantero[2] == "DEL":
      lista2.append(delantero)

  return lista2

#Función para imprimir la lista previamente ordenada
def imprimir_plantel_ordenado(lista):
  for jugador in lista:
    texto = str(
      jugador[2] + ": " + jugador[0] + " " + jugador[1] +
      "    EDAD:" + str(jugador[3]) +
      "   ALTURA(CM):" + str(jugador[4]) +
      "   PARTIDOS:" + str(jugador[5]) +
      "   GOLES:" + str(jugador[6]) +
      "   VALOR:" + str(jugador[7]) + "M US$"
      )
    print(texto)

#Opcion para filtrar por posicion (Elegí no utlizarla para no sobrecargar el menú, sin embargo, allí también se encuentra la opción comentada en caso de querer probarla)
# def ver_datos(lista):
#   salir_sub_menu = False
#   while not salir_sub_menu:
#     print("------------ VER PLANTEL ---------------")
#     print("1 - Ver plantel completo.")
#     print("2 - Filtrar por posición.")
#     print("0 - Atrás.")
#     op = input("Selecciona una opción: ")
#     print("-------------------------------------")

#     if op == "1":
#       plantel_completo = ordenar_lista(lista)
#       return plantel_completo

#     elif op == "2":
#       salir_sub_menu2 = False
#       while not salir_sub_menu2:
#         lista_pos = []
#         print("Posición a filtrar (ARQ/DEF/MED/DEL):")
#         op2 = input("")
#         if op2.upper() == "ARQ":
#           for i in lista:
#             if i[2] == "ARQ":
#               dato = i
#               lista_pos.append(dato)
#           return lista_pos
#         elif op2.upper() == "DEF":
#           for i in lista:
#             if i[2] == "DEF":
#               dato = i
#               lista_pos.append(dato)
#           return lista_pos
#         elif op2.upper() == "MED":
#           for i in lista:
#             if i[2] == "MED":
#               dato = i
#               lista_pos.append(dato)
#           return lista_pos
#         elif op2.upper() == "DEL":
#           for i in lista:
#             if i[2] == "DEL":
#               dato = i
#               lista_pos.append(dato)
#           return lista_pos
#         elif op2 == "0":
#           salir_sub_menu = True
#         else:
#           print("Selecciona una opción válida.")

#==========================FUNCIONES 3 (ACTUALIZAR DATOS)===============================================

#Función para mostrar los datos de un solo jugador (será utilizada en la próxima función)
def imprimir_jugador(lista,nombre,apellido):
  nombre1 = sin_tildes(nombre.title())
  apellido1 = sin_tildes(apellido.title())

  for jugador in lista:
    if jugador[0] == nombre1 and jugador[1] == apellido1:
      jugador_datos = str(
      jugador[2] + ": " + jugador[0] + " " + jugador[1] +
      "    EDAD:" + str(jugador[3]) +
      "   ALTURA(CM):" + str(jugador[4]) +
      "   PARTIDOS:" + str(jugador[5]) +
      "   GOLES:" + str(jugador[6]) +
      "   VALOR:" + str(jugador[7]) + "M US$"
      )
      print(jugador_datos)


def actualizar_datos(lista):
  print("\nIngrese los datos del jugador a actualizar:")
  nombre_actualizar = sin_tildes(input("Nombre: ").title())
  apellido_actualizar = sin_tildes(input("Apellido: ").title())
  existe = False

  #primero recorrer lista para verificar que el jugador exista
  for i in lista:
    if i[0] == nombre_actualizar and i[1] == apellido_actualizar:
      existe = True
    
  #si existe volver a recorrer la lista para borrarlo
  while existe:

    imprimir_jugador(lista,nombre_actualizar,apellido_actualizar)

    for i in lista:
      if i[0] == nombre_actualizar and i[1] == apellido_actualizar:
        lista.remove(i)
        print("\nDatos nuevos:")
        #actualizar jugador nuevo
        #ingreso de datos
        nombre = input("Nombre: ")
          
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

        nombre = sin_tildes(nombre.title())
        apellido = sin_tildes(apellido.title())
        posicion = posicion.upper()
        edad = int(edad)
        altura = int(altura)
        partidos = int(partidos)
        goles = int(goles)
        cotizacion = cotizacion
      
        datos = [nombre,apellido,posicion,edad,altura,partidos,goles,cotizacion]
        lista.append(datos)
        print(f"\n{nombre} {apellido} actualizó a {nombre_actualizar} {apellido_actualizar} exitosamente!" )
        return lista

  else:
    print("El jugador no está en el plantel.")
    
  return lista

#==========================FUNCIONES 4 (ELIMINAR JUGADOR)===============================================

def eliminar_dato(lista):
  print("\nIngrese los datos del jugador a eliminar:")
  nombre_borrar = sin_tildes(input("Nombre: ").title())
  apellido_borrar = sin_tildes(input("Apellido: ").title())
  existe = False

  #primero recorrer lista para verificar que el jugador exista
  for i in lista:
    if i[0] == nombre_borrar and i[1] == apellido_borrar:
      existe = True
      
  #si existe volver a recorrer la lista para borrarlo
  if existe:
    for i in lista:
      if i[0] == nombre_borrar and i[1] == apellido_borrar:
        lista.remove(i)
        print(f"\n{nombre_borrar} {apellido_borrar} fue eliminado con éxito.")
  else:
    print("\nEl jugador no está en el plantel.")

  return lista

#==========================FUNCIONES 5 (OBTENER PROMEDIOS)===============================================

#Función que permite obtener el promedio de un elemento dentro de una lista brindado por parametro
def promedio(lista,indice_a_promediar):
  suma = 0
  cant = 0
  promedio = 0
  for i in lista:
    suma += i[indice_a_promediar]
    cant += 1
  promedio = int(suma/cant)
  return promedio

#Obtener promedio por posición indicada por parametro
def promedio_posicion(lista,indice_promediar,posicion):
  lista2 = []

  for i in lista:
    if i[2] == posicion:
      lista2.append(i)

  return promedio(lista2,indice_promediar)



#La función de arriba se utilizará dentro del sub menú cambiando el parametro dependiendo del elemento a promediar
def elegir_promedio(lista):
  salir_sub_menu = False
  while not salir_sub_menu:
    print("------------ PROMEDIOS ---------------")
    print("1 - Ver promedio de edad del plantel.")
    print("2 - Ver altura promedio en defensa.")
    print("3 - Ver altura promedio en ataque.")
    print("4 - Ver altura promedio del plantel.")
    print("5 - Ver valor promedio del plantel.")
    print("0 - Atrás.")
    op = input("Selecciona una opción: ")
    print("--------------------------------------")

    if op == "1":
      edad = promedio(lista,3)
      print(f"La edad promedio del plantel es de {edad} años.")

    elif op == "2":
      altura = promedio_posicion(lista,4,"DEF")
      print(f"La altura promedio en defensa de {altura} cm.")

    elif op == "3":
      altura = promedio_posicion(lista,4,"DEL")
      print(f"La altura promedio en ataque es de {altura} cm.")

    elif op == "4":
      altura = promedio(lista,4)
      print(f"La altura promedio del plantel es de {altura} cm.")

    elif op == "5":
      valor = promedio(lista,7)
      print(f"El valor promedio del plantel es de {valor}M US$.")

    elif op == "0":
      salir_sub_menu = True

    else:
      print("La opción ingresada es inválida.")

#==========================FUNCIONES 6 (FILTRAR ESTADISTICAS)===============================================

#Funcion que ordena la lista completa de mayor a menor(y viceversa) utilizando el metodo sort. Elegí no incluirla en el menú y mostrar sólo los tres datos mayores o menores.
# def ordenar_plantel(lista,indice_a_ordenar,mayor_o_menor): #mayor_o_menor es un booleano (True=mayor a menor, False=menor a mayor)
#   lista2 = []
#   lista3= []

#   for i in lista:
#     lista2.append(i[indice_a_ordenar])
#   lista2.sort(reverse=mayor_o_menor)

#   for j in lista2:
#     for i in lista:
#       if i[indice_a_ordenar] == j:
#         lista3.append(i)
  
#   return lista3

#Al igual que la función promedio, esta función que permite obtener la suma de un elemento dentro de una lista brindado por parametro
def obtener_suma(lista,indice_a_sumar):
  suma = 0
  for i in lista:
    suma += i[indice_a_sumar]
  return suma

#Imprime de forma ordenada una lista dentro de otra lista
def imprimir_listas_en_lista(lista):
  for i in lista:
    for j in i:
      print(j)

#Función que obtiene los valores más grandes de un elemento en una lista brindado por parametro. Además permite ingresar el nombre del elemento que se va a sumar ("goles", "altura", "edad", etc)
def obtener_tres_mayores(lista,indice_a_comparar,valor_comparado):
  lista2 = []
  maximo = 0
  maximo2 = 0
  maximo3 = 0

  for i in lista:
    if i[indice_a_comparar] > maximo:
      maximo = i[indice_a_comparar]
      nombre = i[0]
      apellido = i[1]
      valor = i[indice_a_comparar]
      dato = [f"{nombre} {apellido}", f"{valor_comparado}: {valor}"]
  lista2.append(dato)

  for i in lista:
    if i[indice_a_comparar] > maximo2 and i[indice_a_comparar] <= maximo:
      jugador = i[0] + " " + i[1]
      #nos aseguramos que el jugador a ingresar en la lista no sea el mismo que ya se igreso
      if jugador != lista2[0][0]:
        maximo2 = i[indice_a_comparar]
        valor = i[indice_a_comparar]
        dato = [f"{jugador}", f"{valor_comparado}: {valor}"]
  lista2.append(dato)

  for i in lista:
    if i[indice_a_comparar] > maximo3 and i[indice_a_comparar] <= maximo2:
      jugador = i[0] + " " + i[1]
      #nos aseguramos que el jugador a ingresar en la lista no sea el mismo que ya se igreso
      if jugador != lista2[0][0] and jugador != lista2[1][0]:
        maximo3 = i[indice_a_comparar]
        valor = i[indice_a_comparar]
        dato = [f"{jugador}", f"{valor_comparado}: {valor}"]
  lista2.append(dato)

  return lista2

#Sub-menú
def elegir_estadistica(lista):
  salir_sub_menu = False
  while not salir_sub_menu:
    print("---------- ESTADISTICAS -------------")
    print("1 - Ver goleadores.")
    print("2 - Ver jugadores más altos.")
    print("3 - Ver jugadores con más presencias.")
    print("4 - Ver jugadores más valiosos.")
    print("5 - Ver valor total del plantel.")
    print("0 - Atrás.")
    op = input("Selecciona una opción: ")
    print("-------------------------------------")

    if op == "1":
      print("Goleadores:\n")
      goleadores = obtener_tres_mayores(lista,6,"Goles")
      imprimir_listas_en_lista(goleadores)

    elif op == "2":
      print("Más altos:\n")
      altos = obtener_tres_mayores(lista,4,"Altura (cm)")
      imprimir_listas_en_lista(altos)

    elif op == "3":
      print("Más presencias:\n")
      presencias = obtener_tres_mayores(lista,5,"Partidos")
      imprimir_listas_en_lista(presencias)

    elif op == "4":
      print("Más valiosos:\n")
      valiosos = obtener_tres_mayores(lista,7,"Valor (M US$)")
      imprimir_listas_en_lista(valiosos)

    elif op == "5":
      valor_total = obtener_suma(lista,7)
      print(f"El valor total del plantel es de {valor_total} M US$.")

    elif op == "0":
      salir_sub_menu = True

    else:
      print("La opción ingresada es inválida.")

#============================FUNCIONES 7 (ACTUALIZAR ESTADISTICAS)==========================================

def actualizar_estadisticas(lista):
  lista2 = []
  jugadores = 0
  #suma de partidos a quienes jugaron
  print("Ingrese nombre y apellido de los futbolistas que jugaron: ")
  print("--------------------------------")
  jug_nombre = input("Nombre ('000' para finalizar): ")

  #se ingresan datos hasta introducir "000" o 16 jugadores, porque está es la cantidad maxima de futbolistas que pueden participar en un partido.
  while jug_nombre != "000" and jugadores < 17:
    jug_apellido = input("Apellido: ")
    print("----------------")

    jug_nombre = jug_nombre.title()
    jug_apellido = jug_apellido.title()

    for i in lista:
      if i[0] == jug_nombre and i[1] == jug_apellido:
        dato = [jug_nombre, jug_apellido]
        lista2.append(dato)
        i[5] += 1
        jugadores += 1

    jug_nombre = input("Nombre: ")

  #suma de goles a quienes marcaron
  print("\nIngrese el/los jugador/es que marcaron goles: ")
  print("--------------------------------")
  gol_nombre = input("Nombre ('000' para finalizar): ")

  while gol_nombre != "000":
    gol_apellido = input("Apellido: ")
    goles = input("Goles: ")
    #chequeo goles sea un numero
    while not goles.isdigit():
      goles = input("Por favor ingrese una cantidad válida: ")
    print("----------------")

    gol_nombre = gol_nombre.title()
    gol_apellido = gol_apellido.title()
    goles = int(goles)

    for i in lista2:
      if i[0] == gol_nombre and i[1] == gol_apellido:
        for j in lista:
          if j[0] == gol_nombre and j[1] == gol_apellido:
            j[6] += goles

    gol_nombre = input("Nombre: ")

  return lista