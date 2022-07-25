CREATE DATABASE tp;
USE tp;
CREATE TABLE plantel (
id int auto_increment,
nombre varchar(255),
apellido varchar(255),
posicion varchar(3),
edad int,
altura int,
partidos int,
goles int,
cotizacion float,
primary key(id)
);
SELECT * FROM plantel;