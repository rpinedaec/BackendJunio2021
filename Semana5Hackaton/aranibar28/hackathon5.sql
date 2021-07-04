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


create table profesor(
    id serial,
    nombres varchar(255) not null,
    identificador  varchar(80) not null,
    edad int,
    correo varchar(45) not null,
    primary key(id)
);

create table curso(
    id serial,
    nombre varchar(255) not null,
    profesor_id int not null,
    primary key(id),
    CONSTRAINT fk_curso_profesor
        FOREIGN KEY(profesor_id) 
            REFERENCES profesor(id)
);

create table salon(
    id serial,
    nombre varchar(255) not null,
    anio_escolar  varchar(80) not null,
    curso_id int not null,
    primary key(id),
    CONSTRAINT fk_salon_curso
        FOREIGN KEY(curso_id) 
            REFERENCES curso(id)
);

create table bimestre(
    id serial,
    notas int not null,
    alumno_id int not null,
    curso_id int not null,
    CONSTRAINT fk_bimestre_alumno
        FOREIGN KEY(alumno_id) 
            REFERENCES alumno(id),
    CONSTRAINT fk_bimestre_curso
        FOREIGN KEY(curso_id) 
            REFERENCES curso(id)
 );

insert into alumno(nombres, identificador, edad, correo)
values('Gerson Aranibar', '70800756', 25, 'aranibar28@gmail.com');
insert into alumno(nombres, identificador, edad, correo)
values('Gian Lapadula', '48671840', 24, 'lapadula@gmail.com');
insert into alumno(nombres, identificador, edad, correo)
values('Crhistian Cueva', '10162292', 27, 'cueva@gmail.com');
insert into alumno(nombres, identificador, edad, correo)
values('Andre Carrillo', '43474036', 22, 'carrillo@gmail.com');

insert into profesor(nombres, identificador, edad, correo)
values('Neymar Junior', '70800756', 25, 'neymar@gmail.com');
insert into profesor(nombres, identificador, edad, correo)
values('Leonel Messi', '48671840', 24, 'messi@gmail.com');
insert into profesor(nombres, identificador, edad, correo)
values('Kylian Mbappe', '10162292', 27, 'mbappe@gmail.com');
insert into profesor(nombres, identificador, edad, correo)
values('Cristiano Ronaldo', '43474036', 22, 'cr7@gmail.com');

insert into curso(nombre, profesor_id) values('Python', 1);
insert into curso(nombre, profesor_id) values('Java', 1);
insert into curso(nombre, profesor_id) values('PHP', 2);
insert into curso(nombre, profesor_id) values('SQL Server', 3);
insert into curso(nombre, profesor_id) values('PostgreSQL', 4);
insert into curso(nombre, profesor_id) values('MySQL', 4);

insert into salon(nombre, anio_escolar, curso_id) values('C203', '2021-1', 1);
insert into salon(nombre, anio_escolar, curso_id) values('C304', '2021-1', 2);
insert into salon(nombre, anio_escolar, curso_id) values('C301', '2021-2', 3);
insert into salon(nombre, anio_escolar, curso_id) values('C405', '2021-2', 4);
insert into salon(nombre, anio_escolar, curso_id) values('C501', '2021-3', 4);

insert into bimestre(notas, alumno_id, curso_id) values(20,1,1);
insert into bimestre(notas, alumno_id, curso_id) values(17,1,2);
insert into bimestre(notas, alumno_id, curso_id) values(15,2,3);
insert into bimestre(notas, alumno_id, curso_id) values(18,3,3);
insert into bimestre(notas, alumno_id, curso_id) values(12,4,4);

select * from alumno;
select * from alumno a inner join bimestre b on b.alumno_id = a.id;
select * from curso c inner join bimestre b on b.curso_id = c.id;
update curso set profesor_id = 3 where profesor_id = 2;