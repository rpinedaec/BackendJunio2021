use hackaton5;

insert into profesores (codigo_profesor,nombres,apellido_paterno,apellido_materno,edad,email) 
values ('PF0001','Martin','Amaya','Ruiz',24,'profesor1@prueba.com');

insert into profesores (codigo_profesor,nombres,apellido_paterno,apellido_materno,edad,email) 
values ('PF0001','Juan','Melendez','Duarte',23,'profesor2@prueba.com');

insert into profesores (codigo_profesor,nombres,apellido_paterno,apellido_materno,edad,email) 
values ('PF0001','Diego','Monteza','Durand',28,'profesor3@prueba.com');

insert into profesores (codigo_profesor,nombres,apellido_paterno,apellido_materno,edad,email) 
values ('PF0001','Cynthia','Flores','Diaz',27,'profesor4@prueba.com');

insert into profesores (codigo_profesor,nombres,apellido_paterno,apellido_materno,edad,email) 
values ('PF0001','Rosa','Pezo','Rojas',29,'profesor5@prueba.com');


insert into cursos (codigo_curso,nombre,id_profesor,activo) 
values ('CUR001','Microcontroladores',4,true);

insert into cursos (codigo_curso,nombre,id_profesor,activo) 
values ('CUR002','Física 1',5,true);

insert into cursos (codigo_curso,nombre,id_profesor,activo) 
values ('CUR003','Física 2',5,true);

insert into cursos (codigo_curso,nombre,id_profesor,activo) 
values ('CUR004','Seguridad de la información',1,true);

insert into cursos (codigo_curso,nombre,id_profesor,activo) 
values ('CUR005','Programación 1',2,true);

insert into cursos (codigo_curso,nombre,id_profesor,activo) 
values ('CUR006','Programación 2',3,true);



insert into salon (codigo_salon,nombre,anio_escolar,id_curso) 
values('SAL001','A101',2021,1);

insert into salon (codigo_salon,nombre,anio_escolar,id_curso) 
values('SAL002','A102',2021,2);

insert into salon (codigo_salon,nombre,anio_escolar,id_curso) 
values('SAL003','A103',2021,3);

insert into salon (codigo_salon,nombre,anio_escolar,id_curso) 
values('SAL004','A104',2021,4);

insert into salon (codigo_salon,nombre,anio_escolar,id_curso) 
values('SAL005','A105',2021,5);

insert into salon (codigo_salon,nombre,anio_escolar,id_curso) 
values('SAL006','A106',2021,6);



insert into alumnos(codigo_alumno, nombres, apellido_paterno,apellido_materno,edad,correo,id_salon)
values('AL0001','Jorge','Montal','Diaz',16,'alummno1@prueba.com',2);

insert into alumnos(codigo_alumno, nombres, apellido_paterno,apellido_materno,edad,correo,id_salon)
values('AL0005','Roberto','Ruiz','Diaz',16,'alummno1@prueba.com',1);

insert into alumnos(codigo_alumno, nombres, apellido_paterno,apellido_materno,edad,correo,id_salon)
values('AL0003','Diana','Saavedra','Moriano',16,'alummno1@prueba.com',1);

insert into alumnos(codigo_alumno, nombres, apellido_paterno,apellido_materno,edad,correo,id_salon)
values('AL0004','Marina','Abad','Arce',16,'alummno1@prueba.com',3);

insert into alumnos(codigo_alumno, nombres, apellido_paterno,apellido_materno,edad,correo,id_salon)
values('AL0005','Angel','Alcala','Teran',16,'alummno1@prueba.com',4);

insert into alumnos(codigo_alumno, nombres, apellido_paterno,apellido_materno,edad,correo,id_salon)
values('AL0006','Carlos','Montal','Sanchez',16,'alummno1@prueba.com',6);

insert into alumnos(codigo_alumno, nombres, apellido_paterno,apellido_materno,edad,correo,id_salon)
values('AL0007','Eduardo','Torres','Cruz',16,'alummno1@prueba.com',6);

insert into alumnos(codigo_alumno, nombres, apellido_paterno,apellido_materno,edad,correo,id_salon)
values('AL0008','Enzo','Vigil','Suarez',16,'alummno1@prueba.com',5);



insert into notas (id_alumno,id_curso,nota_bimestre1,nota_bimestre2,nota_bimestre3,nota_bimestre4)
values(1,2,19,14,15,10);

insert into notas (id_alumno,id_curso,nota_bimestre1,nota_bimestre2,nota_bimestre3,nota_bimestre4)
values(2,1,12,20,15,11);

insert into notas (id_alumno,id_curso,nota_bimestre1,nota_bimestre2,nota_bimestre3,nota_bimestre4)
values(3,1,19,14,15,15);

insert into notas (id_alumno,id_curso,nota_bimestre1,nota_bimestre2,nota_bimestre3,nota_bimestre4)
values(4,3,12,14,17,13);

insert into notas (id_alumno,id_curso,nota_bimestre1,nota_bimestre2,nota_bimestre3,nota_bimestre4)
values(5,4,11,18,15,11);

insert into notas (id_alumno,id_curso,nota_bimestre1,nota_bimestre2,nota_bimestre3,nota_bimestre4)
values(6,6,20,16,15,13);

insert into notas (id_alumno,id_curso,nota_bimestre1,nota_bimestre2,nota_bimestre3,nota_bimestre4)
values(7,6,09,19,18,12);

insert into notas (id_alumno,id_curso,nota_bimestre1,nota_bimestre2,nota_bimestre3,nota_bimestre4)
values(8,5,14,20,17,11);