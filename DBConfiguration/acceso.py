import psycopg2
import getpass # Para ocultar la entrada de la contraseña. (un input)

# Configuración de conexión a la base de datos en Docker
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "RecursosHumanos"
DB_USER = 'Admin'
DB_PASSWORD = "p4ssw0rdDB"

def conectar_db():
    """Conecta a la base de datos PostgreSQL y retorna la conexión."""
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        return conn
    except Exception as e:
        print("Error de conexión:", e)
        return None


def obtener_datos_usuario(username, password):
    #Consulta la base de datos para obtener los datos de un usuario a partir de sus credenciales.
    conn = conectar_db()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        # Verificar si el usuario y contraseña existen en la tabla credenciales
        # tres comillas es para trabajar en párrafos
        query = """
        SELECT u.id_usuario, u.nombre, u.correo, u.telefono, u.fecha_nacimiento,p.nombre_puesto 
        FROM usuarios u, puestos p, credenciales c WHERE 
        c.id_usuario = u.id_usuario AND u.id_puesto=p.id_puesto
        WHERE c.username = %s AND c.password_hash = %s;
        """
        cursor.execute(query, (username, password))
        usuario = cursor.fetchone()

        if usuario:
            print("\nDatos del usuario encontrado:")
            print(f"ID: {usuario[0]}")
            print(f"Nombre: {usuario[1]}")
            print(f"Correo: {usuario[2]}")
            print(f"Teléfono: {usuario[3]}")
            print(f"Fecha de Nacimiento: {usuario[4]}")
            print(f"Puesto: {usuario[5]}")
        else:
            print("\nUsuario o contraseña incorrectos.")
        cursor.close()
        conn.close()
    except Exception as e:
        print("Error al consultar la base de datos:", e)

def insertar_usuario(nombre, correo, telefono, fecha_nacimiento, username, password,idPuesto):
    #Inserta un nuevo usuario y sus credenciales en la base de datos.
    conn = conectar_db()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        # Insertar en la tabla usuarios
        insert_usuario_query = """
        INSERT INTO usuarios (nombre, correo, telefono, fecha_nacimiento,id_puesto)
        VALUES (%s, %s, %s, %s,%s) RETURNING id_usuario;
        """
        cursor.execute(insert_usuario_query, (nombre, correo, telefono, fecha_nacimiento,idPuesto))
        #Obtener el id_usuario generado
        id_usuario = cursor.fetchone()[0]  #con el puro parentesis se obtiene una tupla, y ya con [0] se obtiene el valor

        # Insertar en la tabla credenciales
        insert_credenciales_query = """
        INSERT INTO credenciales (id_usuario, username, password_hash)
        VALUES (%s, %s, %s);
        """
        cursor.execute(insert_credenciales_query, (id_usuario, username, password))
        # Confirmar los cambios en la base de datos
        conn.commit()
        print("\nEl usuario y credenciales insertados correctamente.")
        cursor.close()
        conn.close()
    #Cachar cualquier error y cerrar la conexión
    except Exception as e:
        # Si hay un error, deshacer los cambios
        #Realmente no es necesario porque al cerrar la conexión sin commit, se deshacen los cambios
        conn.rollback()
        conn.close()
        print("Error al insertar en la base de datos:", e)
    finally:
        if conn:
            cursor.close()
            conn.close()
        

def actualizar_correo(id_usuario, nuevo_correo):
    #Actualiza el correo de un usuario en la base de datos.
    conn = conectar_db()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        #Query de actualización
        update_query = """
        UPDATE usuarios
        SET correo = %s
        WHERE id_usuario = %s;
        """
        cursor.execute(update_query, (nuevo_correo, id_usuario))
        conn.commit()
        if cursor.rowcount > 0:
            print("\nCorreo actualizado correctamente.")
        else:
            print("\nNo se encontró el usuario con el ID proporcionado.")
        cursor.close()
        conn.close()
    except Exception as e:
        conn.rollback()
        conn.close()
        print("Error al actualizar el correo:", e)
    finally:
        if conn:
            cursor.close()
            conn.close()

def eliminar_usuario_logico(id_usuario):
    #pone como inactivo a un usuario, para esto ocupamos UPDATE
    conn = conectar_db()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        #Query de actualización
        update_query = "UPDATE usuarios SET activo = false WHERE id_usuario = %s";    
        cursor.execute(update_query, (id_usuario))
        conn.commit()
        if cursor.rowcount > 0:
            print("\nUsuario dado de baja correctamente.")
        else:
            print("\nNo se encontró el usuario con el ID proporcionado.")
        cursor.close()
        conn.close()
    except Exception as e:
        conn.rollback()
        conn.close()
        print("Error al actualizar el estado del usuario:", e)
    finally:
        if conn:
            cursor.close()
            conn.close()

def eliminar_usuario(id_usuario):
    #Elimina un usuario y sus credenciales de la base de datos.
    conn = conectar_db()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        #Eliminar credenciales primero por la clave foránea
        delete_credenciales_query = """
        DELETE FROM credenciales
        WHERE id_usuario = %s;
        """
        cursor.execute(delete_credenciales_query, (id_usuario,))
        #Eliminar usuario
        delete_usuario_query = """
        DELETE FROM usuarios
        WHERE id_usuario = %s;
        """
        cursor.execute(delete_usuario_query, (id_usuario,))
        conn.commit()
        if cursor.rowcount > 0:
            print("\nUsuario eliminado correctamente.")
        else:
            print("\nNo se encontró el usuario con el ID proporcionado.")
        cursor.close()
        conn.close()
    except Exception as e:
        conn.rollback()
        conn.close()
        print("Error al eliminar el usuario:", e)
    finally:
        if conn:
            cursor.close()
            conn.close()
def muestra_puestos():
     #La finalidad de esta funcion es desplagar los datos de los usuarios ordenados por ID
     #Ademas, el usuario puede elegir si despliega todos, solo los activos o solo los dados de baja

    conn = conectar_db()     
    if not conn:
        return
    try:        
        cursor = conn.cursor()
        # Verificar si el usuario y contraseña existen en la tabla credenciales
        # tres comillas es para trabajar en párrafos
        query = "SELECT id_puesto,nombre_puesto,descripcion FROM puestos ORDER BY id_puesto"        
        cursor.execute(query)
        print ("ID_PUESTO |    NOMBRE DEL PUESTO (DESCRIPCION)")
        for fila in cursor:
            print("    " + str(fila[0]) + "     | " + fila[1] + " (" + fila[2]+")")
    except Exception as e:
        conn.rollback()
        conn.close()
        print("Error al eliminar el usuario:", e)
    finally:
        if conn:
            cursor.close()
            conn.close()


def menu():
    while True:
        print(" ----   SELECCIÓN DE EJECUCIÓN   ---- ")
        print("\n")
        print("1. Iniciar sesión")
        print("2. Insertar nuevo usuario")
        print("3. Actualizar correo de usuario")
        print("4. Eliminar usuario")
        print("5. Eliminar usuario logico(baja)")
        print("6. Consultar catalogo de puestos")
        print("0. Salir")
        opcion = input("\nIngrese el número de la opción deseada ( del 0 al 6): ")
        if opcion in ['0','1', '2', '3', '4', '5','6']:
            if opcion == '1':
                user = input("Ingrese su usuario: ")
                pwd = getpass.getpass("Ingrese su contraseña: ")#No muestra la contraseña a escribir
                obtener_datos_usuario(user, pwd)
            elif opcion == '2':
                nombreNuevo = input("Ingrese su nombre: ")
                correoNuevo = input("Ingrese su correo: ")
                telefonoNuevo = input("Ingrese su teléfono: ")
                fechaNacimientoNuevo = input("Ingrese su fecha de nacimiento (YYYY-MM-DD): ")
                idPuesto=input("Ingrese el ID del puesto (sino lo conoce, consulte la opción 6): ")
                userNuevo = input("Ingrese su usuario: ")
                pwdNuevo = getpass.getpass("Ingrese su contraseña: ")#No muestra la contraseña a escribir
                insertar_usuario(nombreNuevo, correoNuevo, telefonoNuevo, fechaNacimientoNuevo, userNuevo, pwdNuevo,idPuesto)
            elif opcion == '3':
                id_usuario = input("Ingrese el ID de usuario que deseas modificar el correo: ")
                nuevoCorreo = input("Ingrese su nuevo correo: ")
                actualizar_correo(id_usuario, nuevoCorreo)
            elif opcion == '4':
                id_usuario_eliminar = input("Ingrese el ID de usuario que deseas eliminar: ")
                eliminar_usuario(id_usuario_eliminar)
            elif opcion == '5':
                id_usuario_baja = input("Ingrese el ID de usuario que deseas dar de baja: ")
                eliminar_usuario_logico(id_usuario_baja)
            elif opcion=='6':
                muestra_puestos()
                break
            elif opcion == '0':
                print("Saliendo del programa.")             
                break
                           
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    menu()
    #print("Inicio de sesión en la base de datos")    
    # Solicitar credenciales al usuario
    #user = input("Ingrese su usuario: ")
    #pwd = getpass.getpass("Ingrese su contraseña: ")#No muestra la contraseña a escribir
    #Consultar base de datos
    #obtener_datos_usuario(user, pwd)
    #-----------------------
    #print("Insertar datos en la base de datos")    
    #nombreNuevo = input("Ingrese su nombre: ")
    #correoNuevo = input("Ingrese su correo: ")
    #telefonoNuevo = input("Ingrese su teléfono: ")
    #fechaNacimientoNuevo = input("Ingrese su fecha de nacimiento (YYYY-MM-DD): ")
    #userNuevo = input("Ingrese su usuario: ")
    #pwdNuevo = getpass.getpass("Ingrese su contraseña: ")#No muestra la contraseña a escribir
    #Insertar datos en la base de datos
    #insertar_usuario(nombreNuevo, correoNuevo, telefonoNuevo, fechaNacimientoNuevo, userNuevo, pwdNuevo)
    #print("Actualizar correo")
    #id_usuario = input("Ingrese el ID de usuario que deseas modificar el correo: ")
    #nuevoCorreo = input("Ingrese su nuevo correo: ")
    #actualizar_correo(id_usuario, nuevoCorreo)

    #print("Eliminar usuario")
    #id_usuario_eliminar = input("Ingrese el ID de usuario que deseas eliminar: ")
    #eliminar_usuario(id_usuario_eliminar)