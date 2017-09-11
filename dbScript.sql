DROP DATABASE AsistenciaDB;

CREATE DATABASE AsistenciaDB;

USE AsistenciaDB;

CREATE TABLE Admin (
	id int,
    Username varchar(50),
    Passwrd varchar(50)
);

CREATE TABLE Operador (
	id int,
    Nombre varchar(50),
    Apellido varchar(50),
    Cedula varchar(10),
    Telefono varchar(10),
    FaceData varchar(50)
);
        
CREATE TABLE Asistencia (
	id int,
    idOperador int,
    Latitud float,
    Longitud float,
    Fecha date,
    Hora time,
    IsEntrada boolean
);

