import mysql.connector

def cargar_database(lista):
  #establecer conexion con mi base de datos
  print("Estableciendo conexión con la base de datos...")
  
  conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="tp"
  )

  #ejecutar cursor para hacer consultas
  mycursor = conexion.cursor()

  #eliminar tabla y volverla a crear
  sql = "TRUNCATE TABLE plantel"
  mycursor.execute(sql)
  #insertar los datos nuevos en la tabla
  sql = "INSERT INTO plantel (nombre,apellido,posicion,edad,altura,partidos,goles,cotizacion) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
  mycursor.executemany(sql, lista)

  #guardar cambios
  conexion.commit()
  print("Carga en base de datos exitosa!")