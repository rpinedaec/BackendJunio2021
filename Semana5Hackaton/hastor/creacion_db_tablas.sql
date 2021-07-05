/*creacion de base de datos*/
create database colegio;

use colegio;
/*creacion de tablas*/
create table cursos(
id_curso serial not null,
codigo_curso char(3) not null,
nombre varchar(50) not null,
id_profesor int not null,
activo bool not null,
constraint pk_cursos primary key(id_curso),
constraint fk_cursos_codigo_profesor foreign key (id_profesor) references profesores(id_profesor)
);


create table profesores(
id_profesor serial not null,
codigo_profesor varchar(30) not null,
nombres varchar(30) not null,
apellido_paterno varchar(50) not null,
apellido_materno varchar(50) not null,
edad int not null,
telefono int null,
direccion varchar(50) null,
email varchar(50) not null,
profesion varchar(50) null,
CONSTRAINT pk_profesor primary key (id_profesor)
);


create table alumnos(
id_alumno serial not null,
codigo_alumno varchar(30) not null,
nombres varchar(50) not null,
apellido_paterno varchar(50) not null,
apellido_materno varchar(50) not null,
edad int not null,
correo varchar(30) not null, 
direccion varchar(50) null,
id_salon int not null,
CONSTRAINT pk_alumnos primary key (id_alumno),
CONSTRAINT pk_alumnos_id_salon foreign key (id_salon) references salon(id_salon)
);


create table salon(
id_salon serial not null,
codigo_salon varchar(30) not null,
nombre varchar(30) not null, 
anio_escolar int not null,
id_curso int not null,
constraint pk_salon primary key (id_salon),
constraint uq_salon_id_cursos unique (id_curso),
constraint pk_salon_id_cursos foreign key (id_curso) references cursos(id_curso)
);

create table notas(
id_alumno int not null,
id_curso int not null,
bimestre1_nota int not null,
bimestre2_nota int not null,
bimestre3_nota int not null,
bimestre4_nota int not null
);

