create database hackaton5;

use hackaton5;
/*tablas*/

create table cursos(
id_curso serial not null,
codigo_curso char(6) not null,
nombre varchar(60) not null,
id_profesor int not null,
activo bool not null,
constraint pk_cursos primary key(id_curso),
constraint fk_cursos_codigo_profesor foreign key (id_profesor) references profesores(id_profesor)
);


create table profesores(
id_profesor serial not null,
codigo_profesor varchar(6) not null,
nombres varchar(50) not null,
apellido_paterno varchar(30) not null,
apellido_materno varchar(30) not null,
edad int not null,
telefono int null,
direccion varchar(60) null,
email varchar(60) not null,
profesion varchar(60) null,
CONSTRAINT pk_profesor primary key (id_profesor)
);


create table alumnos(
id_alumno serial not null,
codigo_alumno varchar(6) not null,
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
codigo_salon varchar(6) not null,
nombre varchar(6) not null, 
anio_escolar int not null,
id_curso int not null,
constraint pk_salon primary key (id_salon),
constraint uq_salon_id_cursos unique (id_curso),
constraint pk_salon_id_cursos foreign key (id_curso) references cursos(id_curso)
);

create table notas(
id_alumno int not null,
id_curso int not null,
nota_bimestre1 int not null,
nota_bimestre2 int not null,
nota_bimestre3 int not null,
nota_bimestre4 int not null
);
