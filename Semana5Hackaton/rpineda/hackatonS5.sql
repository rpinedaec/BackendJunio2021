-- DDL 
create database colegio;

create table alumno(
    id serial,
    nombres varchar(255) not null,
    identificador  varchar(80) not null,
    edad int,
    correo varchar(45) not null,
    primary key(id)
);

-- DML

insert into alumno(nombres, identificador, edad, correo)
values('Karen Lam', '0987654', 26, 'karen@x-codec.net');

select nombres, identificador, edad, correo from alumno;

update alumno
set nombres = 'Liset Sequen', 
identificador = '8989898', 
edad = 27, 
correo='liset@x-codec.net'
where id = 1;

delete from alumno where id = 1;