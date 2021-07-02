create table pais(
    id serial,
    nombre varchar(45) not null,
    primary key(id)
);

create table curso(
    id serial,
    nombre varchar(45) not null,
    primary key(id)
);

create table alumno(
    id serial,
    nombre varchar(45) not null,
    apellido_paterno  varchar(80) not null,
    apellido_materno varchar(80) not null,
    edad int,
    pais_id int not null,
    primary key(id),
    CONSTRAINT fk_alumno_pais
        FOREIGN KEY(pais_id) 
            REFERENCES pais(id)
);

 create table matricula(
    alumno_id int not null,
    curso_id int not null,
    CONSTRAINT fk_alumno_matricula
        FOREIGN KEY(alumno_id) 
            REFERENCES alumno(id),
    CONSTRAINT fk_curso_matricula
        FOREIGN KEY(curso_id) 
            REFERENCES curso(id)
 );

 -- CRUD
 -- Create

insert into pais(nombre) values('Peru');
insert into pais(nombre) values('Ecuador');
insert into pais(nombre) values('Bolivia');
insert into pais(nombre) values('Colombia');

insert into curso(nombre) values('PHP');
insert into curso(nombre) values('NODE');
insert into curso(nombre) values('PYTHON');
insert into curso(nombre) values('C#');

insert into alumno(nombre, apellido_paterno,apellido_materno, edad, pais_id)
values('Karen', 'Lam', 'Serquen', 26, 1);
insert into alumno(nombre, apellido_paterno,apellido_materno, edad, pais_id)
values('Roberto', 'Pineda', 'Lopez', 37, 2);
insert into alumno(nombre, apellido_paterno,apellido_materno, edad, pais_id)
values('David', 'Lopez', 'Serquen', 8, 3);

insert into alumno(nombre, apellido_paterno,apellido_materno, edad, pais_id)
values('Juan', 'Perez', 'Serquen', 33, 5);

-- READ
select nombre from pais;
select * from curso;
select * from alumno;

---UPDATE

update alumno
set nombre = 'Juan'
where nombre = 'David';

--DELETE

delete from alumno where nombre = 'Juan';

Select * from alumno al inner join pais ps on al.pais_id = ps.id;