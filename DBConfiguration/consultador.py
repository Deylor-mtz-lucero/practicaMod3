import psycopg2
#Conexion a la base de datos

conexion = psycopg2.connect(
    host="localhost",
    port="5432", # Puerto por defecto de PostgreSQL
    database="credenciales",
    user="Admin",
    password="p4ssw0rdDB"
)

#cursor crear cursor
cursor = conexion.cursor()

#Ejecutar consulta
cursor.execute("SELECT * FROM usuarios")

#Obtener resultados
registros = cursor.fetchall()   #fetchall recupera todas la filas devueltas
                                # fetchone recupera una fila
                                # fetchmany(n) recupera n filas
#registros almacena en tuplas
for fila in registros:
    print(fila)
    # Hacer algo con cada fila  
#Cerrar cursor y conexion
cursor.close()
conexion.close()    
