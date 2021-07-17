
--datos bimestre
insert into bimestre(nombre) values('1er.Bimestre');
insert into bimestre(nombre) values('2do.Bimestre');
insert into bimestre(nombre) values('3er.Bimestre');
insert into bimestre(nombre) values('4to.Bimestre');

--datos salon
select fn_salon('N',0,'PRIMERO A',2021);
select fn_salon('N',0,'PRIMERO B',2021);
select fn_salon('N',0,'SEGUNDO A',2021);
select fn_salon('N',0,'SEGUNDO B',2021);
--datos profesor
select fn_profesor('N',0,'PEREZ GAMARRA ELIAS',38,'elias@gmail.com');
select fn_profesor('N',0,'CASAS VIVAS ROXANA',32,'roxi@gmail.com');
select fn_profesor('N',0,'CARRASCO VILA GUILLERMO',41,'carrasco@gmail.com');
--datos alumno
select fn_alumno('N',0,'JUAREZ HINOSTROZA IRMA',12,'jhinostroza@gmail.com');
select fn_alumno('N',0,'AGUILAR MEJICO JUAN',12,'aguilar25@gmail.com');
select fn_alumno('N',0,'GARCIA PORRAS PRCY',11,'garciap@gmail.com');
select fn_alumno('N',0,'BRAVO MARTINEZ MARTIN',13,'bravom@gmail.com');
select fn_alumno('N',0,'ROSALES MEZA ELIZABETH',13,'rosalesmeza@gmail.com');
--datos curso
select fn_curso('N',0,'MATEMATICAS 1',1);
select fn_curso('N',0,'COMUNICACION 1',2);
select fn_curso('N',0,'MATEMATICAS 2',3);
select fn_curso('N',0,'COMUNICACION 2',2);

--datos salon cursos
insert into salon_cursos values(1,1,'A');
insert into salon_cursos values(1,2,'A');
insert into salon_cursos values(2,1,'A');
insert into salon_cursos values(2,2,'A');
insert into salon_cursos values(3,3,'A');
insert into salon_cursos values(3,4,'A');
insert into salon_cursos values(4,3,'A');
insert into salon_cursos values(4,4,'A');

--datos matricula
select fn_matricula('N',0,1,1,'A');
select fn_matricula('N',0,2,1,'A');
select fn_matricula('N',0,3,1,'A');

--datos notas alumnos
insert into notas_alumno values(1,1,1,12);
insert into notas_alumno values(1,2,1,14);
insert into notas_alumno values(2,1,1,16);
insert into notas_alumno values(2,2,1,15);
