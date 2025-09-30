import pyscopg2
#Conexion a la base de datos

conexion = psycopg2.connect(
    host="localhost",
    database="nombre_base_datos",
    user="usuario",
    password="contraseña"
)
