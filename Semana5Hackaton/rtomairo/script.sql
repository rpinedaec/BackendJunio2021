CREATE DATABASE colegio;


drop table if exists profesor;
create table profesor(
    idProfesor serial,
    nombre VARCHAR(70),
    apellido_paterno varchar(40) not null,
    apellido_materno VARCHAR(40) not null,
    edad SMALLINT not null,
    correo varchar(50) not null,
    CONSTRAINT pk_profesor PRIMARY KEY(idProfesor)
);


drop table if exists salon;
create table salon(
    idSalon serial,
    nombreSeccion VARCHAR(10) not null,
    CONSTRAINT pk_salon PRIMARY KEY(idSalon)
);

drop table if exists curso;
create table curso(
    idCurso serial, 
    profesorId SMALLINT not null,
    salonId SMALLINT not null,
    nombre VARCHAR(20) not null,
    CONSTRAINT pk_curso PRIMARY KEY(idCurso),
    CONSTRAINT fk_curso_profesor 
        FOREIGN KEY(profesorId)
            REFERENCES profesor(idProfesor),
    CONSTRAINT fk_salon
        FOREIGN KEY(salonId)
            REFERENCES salon(idSalon)
);


drop table if exists bimestre;
create table bimestre(
    idBimestre serial,
    nombre varchar(15) not null,
    CONSTRAINT pk_bimestre PRIMARY KEY(idBimestre)
);

drop table if exists alumno;
create table alumno(
    idAlumno serial,
    nombre VARCHAR(70),
    apellido_paterno varchar(40) not null,
    apellido_materno VARCHAR(40) not null,
    edad SMALLINT not null,
    correo varchar(50) not null,
    CONSTRAINT pk_alumno PRIMARY KEY(idAlumno)
);


drop table if exists registro_notas;
create table registro_notas(
    idNotas serial,
    alumnoId SMALLINT not null,
    bimestreId SMALLINT not null,
    cursoId SMALLINT not null,
    nota SMALLINT not null,
    CONSTRAINT pk_notas PRIMARY KEY(idNotas),
    CONSTRAINT fk_alumno 
        FOREIGN KEY(alumnoId)
            REFERENCES alumno(idAlumno),
    CONSTRAINT fk_bimestre
        FOREIGN KEY(bimestreId)
            REFERENCES bimestre(idBimestre),
    CONSTRAINT fk_curso
        FOREIGN KEY(cursoId)
            REFERENCES curso(idCurso)
    
);
-------------------------CRUD----------------------------------------------------------------


-------------------INSERTANDO VALORES ----------------------------------------

------INSERTAR Profesor
insert into profesor values(DEFAULT,'Luisa','Bravo','Poma',34,'luisabpoma@gmail.com');
insert into profesor values(DEFAULT,'Raul','Poma','Castro',47,'Raulpoma@gmail.com');
insert into profesor values(DEFAULT,'Cristina','siguas','Musto',54,'cristinasiguas@gmail.com');
insert into profesor values(DEFAULT,'Samuel','Contreras','Castro',47,'samulcon@gmail.com');

------INSERTAR Salon
insert into salon values(DEFAULT,'Sección A'),
						(DEFAULT,'Sección B'),
						(DEFAULT,'Sección C'),
						(DEFAULT,'Sección D');


-----INSERTAR Cursos
insert into curso values(DEFAULT,1,1,'Historia'),
						(DEFAULT,2,1,'Matematica'),
						(DEFAULT,3,1,'Lenguaje'),
						(DEFAULT,4,1,'Computación');

---INSERTAR ALUMNOS

insert into alumno values(DEFAULT,'Luis','Quispe','Poma',18,'luis@gmail.com');
insert into alumno values(DEFAULT,'Jose','Torres','Castro',17,'joseT@gmail.com');
insert into alumno values(DEFAULT,'Roger','Velazques','Musto',19,'rvm@gmail.com');
insert into alumno values(DEFAULT,'Liz','Valencia','Castro',20,'lizval@gmail.com');
insert into alumno values(DEFAULT,'88888','Valecscscsncia','Cascscsctro',2330,'lizvalccc@gmail.cccom');
insert into alumno values(DEFAULT,'swww','dd','tro',30,'lizvalccc@gmail.cccom');
insert into alumno values(DEFAULT,'ll','ramdwd','ectro',40,'lizvalgmail.cccom');
insert into alumno values(DEFAULT,'77csz','cdc','decsctro',54,'888ccc@gmail.cccom');


--INSERTAR BIMESTRE
insert into bimestre values(DEFAULT, '1° Bimestre'),
							(DEFAULT, '2° Bimestre'),
							(DEFAULT, '3° Bimestre'),
							(DEFAULT, '4° Bimestre');

--INSERTAR REGISTRO NOTAS
insert into registro_notas values(DEFAULT,1,1,1,15),
								(DEFAULT,2,2,2,15),
								(DEFAULT,2,3,3,15),
								(DEFAULT,3,4,1,15),
								(DEFAULT,4,1,1,15);

---------------------------- UPDATE -----------------------------------------------------------------------------
select *from alumno
UPDATE alumno 
set apellido_materno='Contreras' 
WHERE idalumno=1; 

Update alumno
set nombre='carlos',
apellido_paterno = 'Ramirez',
apellido_materno = 'Peña',
edad = 17,
correo = 'carpeña@gmail.com'
where idalumno=6;

Update alumno
set nombre='Emily',
apellido_paterno = 'Chavez',
apellido_materno = 'Ortiz',
edad = 18,
correo = 'Emi@gmail.com'
where idalumno=7;

Update alumno
set nombre='Ricardo',
apellido_paterno = 'Albertis',
apellido_materno = 'Peña',
edad = 17,
correo = 'ricda@gmail.com'
where idalumno=8;





----------------------------- DELETE -----------------------------------------------------------------------------
DELETE from alumno WHERE idalumno =5
DELETE from alumno WHERE idalumno =9

---------------------------------- READ ------------------------------------------------------

---Alumnos
select a.nombre, a.apellido_paterno, a.apellido_materno, r.nota,
b.nombre as Bimestre
from registro_notas as r
inner join alumno as a
on r.alumnoid = a.idalumno
join bimestre as b
on r.bimestreid = b.idbimestre


---Profesor
select c.nombre,
p.nombre, p.apellido_paterno, p.apellido_materno,
s.nombreseccion
from curso as c
inner join profesor as p
on c.profesorid = p.idprofesor
join salon as s
on c.salonid = s.idsalon

----

select a.nombre, a.apellido_paterno, a.apellido_materno, 
r.nota,
b.nombre as Bimestre,
s.nombre
from registro_notas as r
inner join alumno as a
on r.alumnoid = a.idalumno
join bimestre as b
on r.bimestreid = b.idbimestre
join curso as s
on r.cursoid = r.cursoid




