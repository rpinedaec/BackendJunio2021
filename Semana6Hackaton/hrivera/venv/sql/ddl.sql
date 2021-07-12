create database hackaton6;

\c hackaton6;

create table Alumno(
    id serial,
    nombre varchar(255) not null,
    dni varchar(255) not null,
    edad int not null,
    correo varchar(255) not null,
    primary key(id)
);

create table Profesor(
    id serial,
    nombre varchar(255) not null,
    dni varchar(255) not null,
    edad int not null,
    correo varchar(255) not null,
    primary key(id)
);

create table Bimestre(
    id serial,
    nombre varchar(255) not null,
    primary key(id)
);

create table Curso(
    id serial,
    nombre varchar(255) not null,
    primary key(id)
);

create table Periodo(
    id serial,
    nombre varchar(255) not null,
    año int not null,
    bimestre_id int not null,
    primary key(id),
    CONSTRAINT fk_periodo_bimestre
        FOREIGN KEY(bimestre_id) 
            REFERENCES Bimestre(id)
);

create table CursoProfesor(
    id serial,
    curso_id int not null,
    profesor_id int not null,
    primary key(id),
    CONSTRAINT fk_curso_prefesor
        FOREIGN KEY(curso_id) 
            REFERENCES Curso(id),
    CONSTRAINT fk_profesor_curso
        FOREIGN KEY(profesor_id) 
            REFERENCES Profesor(id)
);

create table Salon(
    id serial,
    nombre varchar(255) not null,
    periodo_id int not null,
    profesor_id int not null,
    alumno_id int not null,
    primary key(id),
    CONSTRAINT fk_salon_periodo
        FOREIGN KEY(periodo_id) 
            REFERENCES Periodo(id),
    CONSTRAINT fk_profesor_salon
        FOREIGN KEY(profesor_id) 
            REFERENCES Profesor(id),
    CONSTRAINT fk_alumno_salon
        FOREIGN KEY(alumno_id) 
            REFERENCES Alumno(id)
);