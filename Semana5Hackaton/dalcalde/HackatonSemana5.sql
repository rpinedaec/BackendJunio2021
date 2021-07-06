--HACKATON SEMANA 5
--  "BASE DE DATOS COLEGIO"

create database COLEGIO;
-- Creando Tablas
create Table Alumno(
    idAlumno serial,
    nombre varchar(80) not null,
    apellido_mat varchar(20) not null,
    apellido_pat varchar(20) not null,
    edad int,
    correo varchar(30) not null,
    primary key(idAlumno)
);

create Table Docente(
    idDocente serial,
    nombre varchar(80) not null,
    apellido_mat varchar(20) not null,
    apellido_pat varchar(20) not null,
    edad int,
    correo varchar(30) not null,
    primary key(idDocente)
);

create Table Aula(
    idAula serial,
    seccion varchar(10) not null,
    Curso_id int not null,
    primary key (idAula)
);

create Table Curso(
    idCurso serial,
    nombre varchar(60)null,
    Docente_id int not null,
    Aula_id int not null,
    Matricula_id int not null,
    Alumno_id int not null,
    primary key (idCurso),
    CONSTRAINT fk_Docente_Curso
        FOREIGN key (Docente_id)
            REFERENCES Docente(idDocente),
    CONSTRAINT fk_Aula_Curso
        FOREIGN key (Aula_id)
            REFERENCES Aula(idAula)
);

create Table Matricula(
    idMatricula serial,
    Alumno_id int not null,
    Docente_id int not null,
    Aula_id int not null,
    primary key(idMatricula),
    CONSTRAINT fk_Alumno_Matricula
        FOREIGN key (Alumno_id)
            REFERENCES Alumno(idAlumno),
    CONSTRAINT fk_Docente_Matricula
        FOREIGN key (Docente_id)
            REFERENCES Docente(idDocente),
    CONSTRAINT fk_Aula_Matricula
        FOREIGN key (Aula_id)
            REFERENCES Aula(idAula)
);

create Table Bimestre(
    idBimestre serial,
    nombre varchar(45) not null,
    fecha_ini date not null,
    fecha_fin date not null,
    primary key (idBimestre)
);

create table RegistroNotas(
    idRegistro serial,
    Alumno_id int not null,
    Bimestre_id int not null,
    Docente_id int not null,
    Aula_id int not null,
    primary key (idRegistro)
    CONSTRAINT fk_Alumno_RegistroNotas
        FOREIGN key (Alumno_id)
            REFERENCES Alumno(idAlumno)
    CONSTRAINT fk_Bimestre_RegistroNotas
        FOREIGN key (Bimestre_id)
            REFERENCES Bimestre(idBimestre),
    CONSTRAINT fk_Docente_RegistroNotas
        FOREIGN key (Docente_id)
            REFERENCES Docente(idDocente),
    CONSTRAINT fk_Aula_RegistroNotas
        FOREIGN key (Aula_id)
            REFERENCES Aula(idAula)
);

--DML (CRUD)
insert into Alumno(nombre, apellido_pat, apellido_mat, edad, correo)
values('Juan', 'Perez', 'De las Rocas', 26, 'Juanpdr@colegio.com');

insert into Docente(nombre, apellido_pat, apellido_mat, edad, correo)
values('Jose', 'De La Torre', 'Ugarte', 35, 'Jdelatorre12@colegio.com');

insert into Aula(seccion)
values('A');

insert into Curso(nombre)
values('Lenguaje y Literatura');

insert into Bimestre(nombre, fecha_ini, fecha_fin)
values('I',2021-03-01,2021-05-30 );


select id, nombre, apellido_mat,apellido_pat, edad, correo from Alumno;
select id, nombre, apellido_mat,apellido_pat, edad, correo from Docente;
select seccion from Aula;
select nombre from Curso;
select nombre, fecha_ini, fecha_fin from Bimestre;

update Alumno
set nombre = 'Panfleto', 
apellido_mat = 'Lizarazu',
apellido_pat = 'Rodriguez',
edad = 29, 
correo='plizarazur@colegio.com'
where id = 1;

update Docente
set nombre = 'Vespucio', 
apellido_mat = 'Amestazaga',
apellido_pat = 'Rumaldo',
edad = 67, 
correo='vamestazagar@colegio.com'
where id = 1;

update Aula
set seccion = 'B', 
where id = 1;

update Curso
set nombre = 'Razonamiento Matematico', 
where id = 1;

update Bimestre
set nombre = 'II',
fecha_ini = 2021-03-02,
fecha_fin =2021-05-29,
where id = 1;

delete from Alumno where id = 1;
delete from Docente where id = 1;
delete from Aula where id = 1;
delete from Curso where id = 1;
delete from alumno where id = 1;