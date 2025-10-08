-- Crear la tabla catalogo de puestos
CREATE TABLE puestos (
 id_puesto SERIAL PRIMARY KEY,  
 nombre_puesto VARCHAR(50) UNIQUE NOT NULL, 
 descripcion VARCHAR(255) NOT NULL 
);
-- Crear la tabla para almacenar usuarios 
CREATE TABLE usuarios (
 id_usuario SERIAL PRIMARY KEY,
 nombre VARCHAR(100) NOT NULL,
 correo VARCHAR(255) UNIQUE,
 telefono VARCHAR(15),
 fecha_nacimiento DATE,
 fecha_alta Date DEFAULT CURRENT_DATE,
 activo BOOLEAN DEFAULT TRUE,
 id_puesto INT NOT NULL,
 FOREIGN KEY (id_puesto) REFERENCES puestos (id_puesto)
);
-- Crear la tabla para almacenar contraseñas
CREATE TABLE credenciales (
 id_credencial SERIAL PRIMARY KEY,
 id_usuario INT NOT NULL,
 username VARCHAR(50) UNIQUE NOT NULL, 
 password_hash VARCHAR(255) NOT NULL,
 FOREIGN KEY (id_usuario) REFERENCES usuarios (id_usuario)
);

