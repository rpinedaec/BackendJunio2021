create database hackaton;
\c hackaton;

create table alumnos(
    id serial,
    nombre varchar(45) not null,
    identificacion varchar(45) not null,
    edad int,
    correo varchar(80) not null,
    primary key(id)
);
create table profesores(
    id serial,
    nombre varchar(45) not null,
    identificador varchar(80) not null,
    edad int,
    correo varchar(80) not null,
    primary key(id)
);
create table cursos(
    id serial,
    nombre varchar(45) not null,
    idProfesor int not null,
    primary key(id),
CONSTRAINT fk_curso_profesor
FOREIGN KEY(idProfesor) 
REFERENCES profesores(id)
);

create table salon(
    id serial,
    nombre varchar(45) not null,
    añoEscolar int not null,
    idAlumno int not null,
    idProfesor int not null,
    primary key(id),
CONSTRAINT fk_salon_alumno
FOREIGN KEY(idAlumno) 
REFERENCES alumnos(id),
CONSTRAINT fk_profesor_curso
FOREIGN KEY(idProfesor) 
REFERENCES profesores(id)
);



create table notas(
    id serial,
    puntaje decimal(20,20),
    idAlumno int not null,
    idCurso int not null,
    bimestre int not null,
    primary key(id),
    CONSTRAINT fk_notas_alumno
    FOREIGN KEY(idAlumno) 
    REFERENCES alumnos(id),
    CONSTRAINT fk_notas_curso
    FOREIGN KEY(idCurso) 
    REFERENCES cursos(id)
);

-- Insertar datos en alumnos

insert into alumnos(nombre, identificacion, edad, correo)
values('Hector Rivera', '73533219', 24, 'correo@correo.com');

insert into alumnos(nombre, identificacion, edad, correo)
values('Jorge Sanchez', '442121010', 34, 'correo1@correo.com');

--buscar en alumnos
select nombre, identificacion, edad, correo from alumnos;

--modificar el identificador del alumno 2

update alumnos
set nombre = 'Jorge Sanchez', 
identificacion= '442121044', 
edad = 34, 
correo='correo1@correo.com'
where id = 2;

-- eliminar alumno 2

delete from alumnos where id = 2;

-- Insertar datos en Profesores

insert into profesores(nombre, identificador,edad, correo)
values('Roberto Pineda', '12345678', 29, 'correoDocente1@correo.com');

insert into profesores(nombre, identificador,edad, correo)
values('Marco Jimenez', '87654321', 45, 'correoDocente2@correo.com');

-- Insertar datos en Cursos

insert into cursos(nombre, idProfesor)
values('Python', 1);

insert into cursos(nombre, idProfesor)
values('Filosofia', 2);

-- Insertar datos en Salon

insert into salon(nombre, añoEscolar,idAlumno,idProfesor)
values('a101', 2022,1,2);
insert into salon(nombre, añoEscolar,idAlumno,idProfesor)
values('a102', 2022,2,1);

-- Insertar datos en Notas

insert into notas( puntaje,idAlumno,idCurso,bimestre)
values(18,1,1,1);
insert into notas( puntaje,idAlumno,idCurso,bimestre)
values(19,1,1,1);

--Para sacar el promedio de las notas 

select avg(puntaje) from notas;