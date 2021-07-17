Insert into Alumno(nombre,dni,edad,correo) values('Roberto Pineda', '001575291', 37, 'rp@x-codec.net');
Insert into Alumno(nombre,dni,edad,correo) values('Diego Pacheco', '015412741', 17, 'dp@x-codec.net');
Insert into Alumno(nombre,dni,edad,correo) values('Mathias Bautista', '09851010', 25, 'mb@x-codec.net');
Insert into Alumno(nombre,dni,edad,correo) values('Evelin Bustamante', '374514111', 21, 'eb@x-codec.net');
Insert into Alumno(nombre,dni,edad,correo) values('Bruce Yamashiro', '66616661', 28, 'by@x-codec.net');
Update Alumno
set nombre = 'David Lopez',
dni = '00175292',
edad = 32,
correo = 'dl@x-codec.net'
where id = 1;
Delete from Alumno where id = 1;
Select * from Alumno;

Insert into Profesor(nombre,dni,edad,correo) values('Karen Lam', '001575291', 37, 'kl@x-codec.net');
Insert into Profesor(nombre,dni,edad,correo) values('Rocio Lopez', '291370111', 26, 'rl@x-codec.net');
Insert into Profesor(nombre,dni,edad,correo) values('Joel Zegarra', '57005291', 41, 'jz@x-codec.net');
Insert into Profesor(nombre,dni,edad,correo) values('Rudi Barranca', '91917451', 29, 'rb@x-codec.net');
Insert into Profesor(nombre,dni,edad,correo) values('Cesar Rios', '91128577', 35, 'cr@x-codec.net');
Update Profesor
set nombre = 'Liseth Serquen',
dni = '00175292',
edad = 32,
correo = 'dl@x-codec.net'
where id = 1;
Delete from Profesor where id = 1;
Select * from Profesor;

Insert into Bimestre(nombre) values('I Bimestre');
Insert into Bimestre(nombre) values('II Bimestre');
Insert into Bimestre(nombre) values('III Bimestre');
Insert into Bimestre(nombre) values('IV Bimestre');
Update Bimestre set nombre = '1 Bimestre' where id = 1;
Delete Bimestre where id = 1;
Select * from Bimestre;

Insert into Curso(nombre) values('I Curso');
Insert into Curso(nombre) values('II Curso');
Insert into Curso(nombre) values('III Curso');
Insert into Curso(nombre) values('IV Curso');
Insert into Curso(nombre) values('V Curso');
Update Curso set nombre = '1 Curso' where id = 1;
Delete Curso where id = 1;
Select * from Curso;

insert into Periodo( nombre, año, bimestre_id) values('Periodo1', 2021, 1);
insert into Periodo( nombre, año, bimestre_id) values('Periodo1', 2021, 2);
insert into Periodo( nombre, año, bimestre_id) values('Periodo1', 2021, 3);
insert into Periodo( nombre, año, bimestre_id) values('Periodo1', 2021, 1);
Update Periodo 
set nombre = 'Periodo 1',
año = 2021,
bimestre_id = 1
where id = 1;
select * from Periodo;
delete from Periodo where id = 1;

insert into CursoProfesor (curso_id, profesor_id) values(1,1);
insert into CursoProfesor (curso_id, profesor_id) values(1,1);
insert into CursoProfesor (curso_id, profesor_id) values(1,1);
insert into CursoProfesor (curso_id, profesor_id) values(1,1);
insert into CursoProfesor (curso_id, profesor_id) values(1,1);
Update CursoProfesor set curso_id = 2, profesor_id = 2 where id = 1;
select * from CursoProfesor;
delete from CursoProfesor where id = 1;

insert into Salon(nombre, periodo_id, profesor_id, alumno_id) values ('Salon 1',1,1,1);
insert into Salon(nombre, periodo_id, profesor_id, alumno_id) values ('Salon 1',1,1,1);
insert into Salon(nombre, periodo_id, profesor_id, alumno_id) values ('Salon 1',1,1,1);
insert into Salon(nombre, periodo_id, profesor_id, alumno_id) values ('Salon 1',1,1,1);
insert into Salon(nombre, periodo_id, profesor_id, alumno_id) values ('Salon 1',1,1,1);
Update Salon set nombre = 'Salon I', periodo_id=1, profesor_id=1, alumno_id=1 where id = 1;
select * from Salon;
delete Salon where id = 1;


