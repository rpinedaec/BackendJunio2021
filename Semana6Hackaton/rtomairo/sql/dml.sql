Insert into Alumno(nombre,dni,edad,correo)
values('Roberto Pineda', '001575291', 37, 'rp@x-codec.net');
Update Alumno
set nombre = 'David Lopez',
dni = '00175292',
edad = 32,
correo = 'dl@x-codec.net'
where id = 1;
--Delete from Alumno where id = 1;
Select * from Alumno;

Insert into Profesor(nombre,dni,edad,correo)
values('Karen Lam', '001575291', 37, 'rp@x-codec.net');
Update Profesor
set nombre = 'Liseth Serquen',
dni = '00175292',
edad = 32,
correo = 'dl@x-codec.net'
where id = 1;
--Delete from Profesor where id = 1;
Select * from Profesor;

Insert into Bimestre(nombre) values('I Bimestre');
Insert into Bimestre(nombre) values('II Bimestre');
Update Bimestre set nombre = '1 Bimestre' where id = 1;
--Delete Bimestre where id = 1;
Select * from Bimestre;

Insert into Curso(nombre) values('I Curso');
Insert into Curso(nombre) values('II Curso');
Update Curso set nombre = '1 Curso' where id = 1;
--Delete Curso where id = 1;
Select * from Curso;

insert into Periodo( nombre, año, bimestre_id)
values('Periodo1', 2021, 1);

Update Periodo 
set nombre = 'Periodo 1',
año = 2021,
bimestre_id = 1
where id = 1;
select * from Periodo;
--delete from Periodo where id = 1;

insert into CursoProfesor (curso_id, profesor_id)
values(1,1);
Update CursoProfesor set curso_id = 2, profesor_id = 2 where id = 1;
select * from CursoProfesor;
--delete from CursoProfesor where id = 1;

insert into Salon(nombre, periodo_id, profesor_id, alumno_id)
values ('Salon 1',1,1,1);
Update Salon set nombre = 'Salon I', periodo_id=1, profesor_id=1, alumno_id=1 where id = 1;
select * from Salon;
--delete Salon where id = 1;


