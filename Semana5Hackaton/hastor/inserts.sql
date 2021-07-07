use colegio;
/*insertando datos a tabla profesores*/
insert into profesores (codigo_profesor,nombres,apellido_paterno,apellido_materno,edad,email) 
values ('P0001','Renato','Valdez','Vega',35,'rvaldez@colegio.com');

insert into profesores (codigo_profesor,nombres,apellido_paterno,apellido_materno,edad,email) 
values ('P0002','Andres','Alcantara','Flores',34,'aalcantara@colegio.com');

insert into profesores (codigo_profesor,nombres,apellido_paterno,apellido_materno,edad,email) 
values ('P0003','Paul','Vega','Espinoza',35,'pvega@colegio.com');

insert into profesores (codigo_profesor,nombres,apellido_paterno,apellido_materno,edad,email) 
values ('P0004','Juan','Vallejo','Rojas',35,'jvallejo@colegio.com');

insert into profesores (codigo_profesor,nombres,apellido_paterno,apellido_materno,edad,email) 
values ('P0005','Ricardo','Mata','Matias',37,'rmata@colegio.com');

/*insertando datos tabla */

insert into cursos (codigo_curso,nombre,id_profesor,activo) 
values ('ALG','Algebra',2,true);

insert into cursos (codigo_curso,nombre,id_profesor,activo) 
values ('LIT','Literatura',3,true);

insert into cursos (codigo_curso,nombre,id_profesor,activo) 
values ('FIS','Fisica',1,true);

insert into cursos (codigo_curso,nombre,id_profesor,activo) 
values ('QUI','Quimica',1,true);

insert into cursos (codigo_curso,nombre,id_profesor,activo) 
values ('TRG','Trigonometria',4,true);

insert into cursos (codigo_curso,nombre,id_profesor,activo) 
values ('GEO','Geometria',5,true);

/*insertando data en la tabla salon*/

insert into salon (codigo_salon,nombre,anio_escolar,id_curso) 
values('S0001','Salon Rojo',2021,1);

insert into salon (codigo_salon,nombre,anio_escolar,id_curso) 
values('S0002','Salon Celeste',2021,6);

insert into salon (codigo_salon,nombre,anio_escolar,id_curso) 
values('S0003','Salon Azul',2021,2);

insert into salon (codigo_salon,nombre,anio_escolar,id_curso) 
values('S0004','Salon Verde',2021,3);

insert into salon (codigo_salon,nombre,anio_escolar,id_curso) 
values('S0005','Salon Amarillo',2021,4);

insert into salon (codigo_salon,nombre,anio_escolar,id_curso) 
values('S0006','Salon Morado',2021,5);

/*insertando data en la tabla alumnos*/

insert into alumnos(codigo_alumno, nombres, apellido_paterno,apellido_materno,edad,correo,id_salon)
values('A0001','Haroun','Asto','Rojas',16,'hasto@colegio.com',2);

insert into alumnos(codigo_alumno, nombres, apellido_paterno,apellido_materno,edad,correo,id_salon)
values('A0002','Betsy','Rojas','Laura',16,'brojas@colegio.com',2);

insert into alumnos(codigo_alumno, nombres, apellido_paterno,apellido_materno,edad,correo,id_salon)
values('A0003','Frida','Rojas','Salas',16,'frojas@colegio.com',1);

insert into alumnos(codigo_alumno, nombres, apellido_paterno,apellido_materno,edad,correo,id_salon)
values('A0004','Zoe','Asto','Rojas',16,'zasto@colegio.com',1);

insert into alumnos(codigo_alumno, nombres, apellido_paterno,apellido_materno,edad,correo,id_salon)
values('A0005','Maria','Espinoza','Gomez',16,'mespinoza@colegio.com',3);

insert into alumnos(codigo_alumno, nombres, apellido_paterno,apellido_materno,edad,correo,id_salon)
values('A0006','Juan','Villalobos','Cotrina',16,'jvillalobos@colegio.com',4);

insert into alumnos(codigo_alumno, nombres, apellido_paterno,apellido_materno,edad,correo,id_salon)
values('A0007','Kevin','Ricaldi','Vidal',16,'kricaldi@colegio.com',5);

insert into alumnos(codigo_alumno, nombres, apellido_paterno,apellido_materno,edad,correo,id_salon)
values('A0008','Jover','Camayo','Velarde',16,'jcamayo@colegio.com',1);

insert into alumnos(codigo_alumno, nombres, apellido_paterno,apellido_materno,edad,correo,id_salon)
values('A0009','Mayra','Pachecho','Gomez',16,'mpacheco@colegio.com',6);

insert into alumnos(codigo_alumno, nombres, apellido_paterno,apellido_materno,edad,correo,id_salon)
values('A0010','Carlos','Villagran','Romeo',16,'cvillagran@colegio.com',7);

/*insertando data en la tabla notas*/


insert into notas (id_alumno,id_curso,bimestre1_nota,bimestre2_nota,bimestre3_nota,bimestre4_nota)
values(1,1,12,14,15,11);

insert into notas (id_alumno,id_curso,bimestre1_nota,bimestre2_nota,bimestre3_nota,bimestre4_nota)
values(1,2,11,14,15,11);

insert into notas (id_alumno,id_curso,bimestre1_nota,bimestre2_nota,bimestre3_nota,bimestre4_nota)
values(1,3,09,14,12,11);

insert into notas (id_alumno,id_curso,bimestre1_nota,bimestre2_nota,bimestre3_nota,bimestre4_nota)
values(2,3,09,05,13,12);

insert into notas (id_alumno,id_curso,bimestre1_nota,bimestre2_nota,bimestre3_nota,bimestre4_nota)
values(2,4,20,18,17,16);

insert into notas (id_alumno,id_curso,bimestre1_nota,bimestre2_nota,bimestre3_nota,bimestre4_nota)
values(2,5,11,10,11,11);


insert into profesores (codigo_profesor,nombres,apellido_paterno,apellido_materno,edad,email) 
values ('P0005','Ricardo','Mata','Matias',37,'rmata@colegio.com');

update profesores
set codigo_profesor = '',
nombres = '',
apellido_paterno = '',
apellido_materno = '',
edad = 22,
email = ''
where id_profesor = 22
