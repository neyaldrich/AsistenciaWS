USE AsistenciaDB;

INSERT INTO restApi_admin (username, password)
VALUES ("admin1", "1111");

INSERT INTO restApi_admin (username, password)
VALUES ("admin2", "2222");

INSERT INTO restApi_admin (username, password)
VALUES ("admin3", "3333");

-- Insercion de Operadores

INSERT INTO restApi_operador (nombre, apellido, cedula, telefono, encodedFaceData)
VALUES ("Fernando", "Mejía", "0952417854", "0980504030", "none");

INSERT INTO restApi_operador (nombre, apellido, cedula, telefono)
VALUES ("Enrique", "Torres", "1247836214", "0981514131");

INSERT INTO restApi_operador (nombre, apellido, cedula, telefono)
VALUES ("Sara", "Flores", "1547836214", "0982524232");

INSERT INTO restApi_operador (nombre, apellido, cedula, telefono)
VALUES ("Jessica", "Donoso", "1547836214", "0983534333");

INSERT INTO restApi_operador (nombre, apellido, cedula, telefono)
VALUES ("Hector", "Andrade", "1547833214", "0984544434");

-- Ingresos y salidas del Operador 1, en la semana del 4 al 8 de Septiembre

INSERT INTO restApi_asistencia (operador_id, latitud, longitud, fecha, hora, isEntrada)
VALUES (1, -2.2058400, -79.9079500, '2017-09-04', '08:30:00', true);

INSERT INTO restApi_asistencia (operador_id, latitud, longitud, fecha, hora, isEntrada)
VALUES (1, -2.2058400, -79.9079500, '2017-09-04', '17:30:00', false);  


INSERT INTO restApi_asistencia (operador_id, latitud, longitud, fecha, hora, isEntrada)
VALUES (1, -2.2058400, -79.9079500, '2017-09-05', '08:30:00', true);

INSERT INTO restApi_asistencia (operador_id, latitud, longitud, fecha, hora, isEntrada)
VALUES (1, -2.2058400, -79.9079500, '2017-09-05', '17:30:00', false);  


INSERT INTO restApi_asistencia (operador_id, latitud, longitud, fecha, hora, isEntrada)
VALUES (1, -2.2058400, -79.9079500, '2017-09-06', '08:30:00', true);

INSERT INTO restApi_asistencia (operador_id, latitud, longitud, fecha, hora, isEntrada)
VALUES (1, -2.2058400, -79.9079500, '2017-09-06', '17:30:00', false);  


INSERT INTO restApi_asistencia (operador_id, latitud, longitud, fecha, hora, isEntrada)
VALUES (1, -2.2058400, -79.9079500, '2017-09-07', '08:30:00', true);

INSERT INTO restApi_asistencia (operador_id, latitud, longitud, fecha, hora, isEntrada)
VALUES (1, -2.2058400, -79.9079500, '2017-09-07', '17:30:00', false);


INSERT INTO restApi_asistencia (operador_id, latitud, longitud, fecha, hora, isEntrada)
VALUES (1, -2.2058400, -79.9079500, '2017-09-08', '08:30:00', true);

INSERT INTO restApi_asistencia (operador_id, latitud, longitud, fecha, hora, isEntrada)
VALUES (1, -2.2058400, -79.9079500, '2017-09-08', '17:30:00', false); 

-- End Operador 1


-- Ingresos y salidas del Operador 2, en la semana del 4 al 8 de Septiembre

INSERT INTO restApi_asistencia (operador_id, latitud, longitud, fecha, hora, isEntrada)
VALUES (2, -2.2058400, -79.9079500, '2017-09-04', '09:00:00', true);

INSERT INTO restApi_asistencia (operador_id, latitud, longitud, fecha, hora, isEntrada)
VALUES (2, -2.2058400, -79.9079500, '2017-09-04', '18:00:00', false);  


INSERT INTO restApi_asistencia (operador_id, latitud, longitud, fecha, hora, isEntrada)
VALUES (2, -2.2058400, -79.9079500, '2017-09-05', '09:00:00', true);

INSERT INTO restApi_asistencia (operador_id, latitud, longitud, fecha, hora, isEntrada)
VALUES (2, -2.2058400, -79.9079500, '2017-09-05', '18:00:00', false); 


INSERT INTO restApi_asistencia (operador_id, latitud, longitud, fecha, hora, isEntrada)
VALUES (2, -2.2058400, -79.9079500, '2017-09-06', '09:00:00', true);

INSERT INTO restApi_asistencia (operador_id, latitud, longitud, fecha, hora, isEntrada)
VALUES (2, -2.2058400, -79.9079500, '2017-09-06', '18:00:00', false); 


INSERT INTO restApi_asistencia (operador_id, latitud, longitud, fecha, hora, isEntrada)
VALUES (2, -2.2058400, -79.9079500, '2017-09-07', '09:00:00', true);

INSERT INTO restApi_asistencia (operador_id, latitud, longitud, fecha, hora, isEntrada)
VALUES (2, -2.2058400, -79.9079500, '2017-09-07', '18:00:00', false); 


INSERT INTO restApi_asistencia (operador_id, latitud, longitud, fecha, hora, isEntrada)
VALUES (2, -2.2058400, -79.9079500, '2017-09-08', '09:00:00', true);

INSERT INTO restApi_asistencia (operador_id, latitud, longitud, fecha, hora, isEntrada)
VALUES (2, -2.2058400, -79.9079500, '2017-09-08', '18:00:00', false); 

-- End Operador 2