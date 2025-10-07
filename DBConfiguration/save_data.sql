--Insertar datos en catalogo de puestos
INSERT INTO puestos (nombre_puesto,descripcion) VALUES
('Operativo eventual', 'Cargo referente a un nivel salarial 8'),
('Supervisor', 'Cargo referente a un nivel salarial 7'),
('Jefe de departamento', 'Cargo referente a un nivel salarial 6'),
('Sugerente', 'Cargo referente a un nivel salarial 5'),
('Gerente', 'Cargo referente a un nivel salarial 4'),
('Subdirector de área', 'Cargo referente a un nivel salarial 3'),
('Director de área', 'Cargo referente a un nivel salarial 2'),
('Director General', 'Cargo referente a un nivel salarial 1');


-- Insertar datos en la tabla usuarios
INSERT INTO usuarios (nombre, correo, telefono, fecha_nacimiento,id_puesto) VALUES
('Juan Pérez', 'juan.perez1@example.com', '1234567890', '1985-01-15',1),
('Ana Gómez', 'ana.gomez2@example.com', '1234567891', '1990-03-22',2),
('Luis Martínez', 'luis.martinez3@example.com', '1234567892', '1988-07-10',3),
('María López', 'maria.lopez4@example.com', '1234567893', '1992-11-05',4),
('Carlos Ruiz', 'carlos.ruiz5@example.com', '1234567894', '1980-06-25',5),
('Sofía Castro', 'sofia.castro6@example.com', '1234567895', '1995-02-18',6),
('David Ramírez', 'david.ramirez7@example.com', '1234567896', '1983-09-09',7),
('Elena Ortega', 'elena.ortega8@example.com', '1234567897', '1991-05-03',7),
('Miguel Torres', 'miguel.torres9@example.com', '1234567898', '1993-12-14',7),
('Laura Sánchez', 'laura.sanchez10@example.com', '1234567899', '1987-08-01',7),
('Pedro Morales', 'pedro.morales11@example.com', '1234567800', '1986-04-17',7),
('Clara Hernández', 'clara.hernandez12@example.com', '1234567801', '1994-06-30',4),
('Jorge Rojas', 'jorge.rojas13@example.com', '1234567802', '1981-03-25',4),
('Valeria Peña', 'valeria.pena14@example.com', '1234567803', '1992-01-09',4),
('Andrés Romero', 'andres.romero15@example.com', '1234567804', '1989-10-12',4),
('Camila Paredes', 'camila.paredes16@example.com', '1234567805', '1997-11-19',4),
('Ricardo Vargas', 'ricardo.vargas17@example.com', '1234567806', '1984-07-23',5),
('Daniela Flores', 'daniela.flores18@example.com', '1234567807', '1996-03-01',5),
('Héctor Serrano', 'hector.serrano19@example.com', '1234567808', '1982-02-11',5),
('Patricia Vega', 'patricia.vega20@example.com', '1234567809', '1990-09-05',5),
('Deyanira Martinez', 'deyaniramartinez@example.com', '1234567811', '1990-09-06',3),
('Leticia Fernandez', 'letyfe@example.com', '1234567881', '1990-09-07',2);


-- Insertar datos en la tabla credenciales
INSERT INTO credenciales (id_usuario, username, password_hash) VALUES
(1, 'juan.perez1', 'hash_juan_perez'),
(2, 'ana.gomez2', 'hash_ana_gomez'),
(3, 'luis.martinez3', 'hash_luis_martinez'),
(4, 'maria.lopez4', 'hash_maria_lopez'),
(5, 'carlos.ruiz5', 'hash_carlos_ruiz'),
(6, 'sofia.castro6', 'hash_sofia_castro'),
(7, 'david.ramirez7', 'hash_david_ramirez'),
(8, 'elena.ortega8', 'hash_elena_ortega'),
(9, 'miguel.torres9', 'hash_miguel_torres'),
(10, 'laura.sanchez10', 'hash_laura_sanchez'),
(11, 'pedro.morales11', 'hash_pedro_morales'),
(12, 'clara.hernandez12', 'hash_clara_hernandez'),
(13, 'jorge.rojas13', 'hash_jorge_rojas'),
(14, 'valeria.pena14', 'hash_valeria_pena'),
(15, 'andres.romero15', 'hash_andres_romero'),
(16, 'camila.paredes16', 'hash_camila_paredes'),
(17, 'ricardo.vargas17', 'hash_ricardo_vargas'),
(18, 'daniela.flores18', 'hash_daniela_flores'),
(19, 'hector.serrano19', 'hash_hector_serrano'),
(20, 'patricia.vega20', 'hash_patricia_vega'),
(21, 'deyanira.mtz21', 'hash_deyanira_mtz'),
(22, 'lety.mtz21', 'hash_lety_mtz');
