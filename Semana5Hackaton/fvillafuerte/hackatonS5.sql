--- base de datos colegio
CREATE DATABASE colegio
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Spanish_Spain.1252'
    LC_CTYPE = 'Spanish_Spain.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

--- tabla salon
DROP TABLE IF EXISTS salon;
Create Table salon(
	id_salon int not null,
	nombre varchar(30),
	ano_escolar smallint,
	Constraint pk_salon Primary Key (id_salon)
);

--- tabla profesor
DROP TABLE IF EXISTS profesor;
Create Table profesor(
	id_profesor int not null,
	nombre varchar(50),
	edad smallint,
	correo varchar(30),
	Constraint pk_profesor Primary Key (id_profesor)
);

--- tabla alumno
DROP TABLE IF EXISTS alumno;
Create Table alumno(
	id_alumno int not null,
	nombre varchar(50),
	edad smallint,
	correo varchar(30),
	Constraint pk_alumno Primary Key (id_alumno)
);

--- tabla curso
DROP TABLE IF EXISTS curso;
Create Table curso(
	id_curso int not null,
	nombre varchar(30),
	id_profesor int not null,
	Constraint pk_curso Primary Key (id_curso),
	Constraint fk_curso_id_profesor FOREIGN KEY (id_profesor) references profesor(id_profesor)
);

--- tabla bimestres
DROP TABLE IF EXISTS bimestre;
Create Table bimestre(
	id_bimestre serial,
	nombre varchar(15),
	Constraint pk_bimestre Primary Key (id_bimestre)
);

--- tabla maricula del alumno
DROP TABLE IF EXISTS matricula;
Create Table matricula(
	id_matricula int not null,
	id_alumno int not null,
	id_salon int not null,
	estado char(1) not null,
	Constraint pk_matricula Primary Key (id_matricula),
	Constraint fk_matricula_id_alumno FOREIGN KEY (id_alumno) references alumno(id_alumno),
	Constraint fk_matricula_id_salon FOREIGN KEY (id_salon) references salon(id_salon),
	Constraint chk_matricula_estado check (estado in('A','I'))
);

--- tabla cursos por salon
DROP TABLE IF EXISTS salon_cursos;
Create Table salon_cursos(
	id_salon int not null,
	id_curso int not null,
	estado char(1) not null,
	Constraint pk_salon_cursos Primary Key (id_salon,id_curso),
	Constraint fk_salon_cursos_id_salon FOREIGN KEY (id_salon) references salon(id_salon),
	Constraint fk_salon_cursos_id_curso FOREIGN KEY (id_curso) references curso(id_curso),
	Constraint chk_salon_cursos_estado check (estado in('A','I'))
);

--- tabla notas del alumno
DROP TABLE IF EXISTS notas_alumno;
Create Table notas_alumno(
	id_matricula int not null,
	id_curso int not null,
	id_bimestre int not null,
	nota int,
	Constraint pk_notas_alumno Primary Key (id_matricula,id_curso,id_bimestre),
	Constraint fk_notas_alumno_id_matricula FOREIGN KEY (id_matricula) references matricula(id_matricula),
	Constraint fk_notas_alumno_id_curso FOREIGN KEY (id_curso) references curso(id_curso),
	Constraint fk_notas_alumno_id_bimestre FOREIGN KEY (id_bimestre) references bimestre(id_bimestre)
);

--funciones
-- actualizar tabla salon
create or replace function fn_salon(char(1),int,varchar(30),int)
returns varchar(20)
as $$
declare
	opc char(1):= $1;
	id int:= $2;
	nom varchar(30):= $3;
	ano int:= $4;
	res varchar(20) := '';
	reg int:= 0;
begin
	if opc = 'N' then
	    select max(id_salon)+1 into reg from salon;
		if reg isnull then 
			reg :=1;
		end if;
		insert into salon values(reg,nom,ano);
		res := 'Registro Agregado';
	end if;
	if opc = 'M' then
		update salon set nombre=nom, ano_escolar=ano where id_salon=id;
		res := 'Registro Modificado';
	end if;
	if opc = 'E' then
		delete from salon where id_salon=id;
		res := 'Registro Eliminado';
	end if;	
	return res;
end;
$$
language plpgsql;

-- actualizar tabla profesor
create or replace function fn_profesor(char(1),int,varchar(50),int,varchar(30))
returns varchar(20)
as $$
declare
	opc char(1):= $1;
	id int:= $2;
	nom varchar(50):= $3;
	age int:= $4;
	mail varchar(30):= $5;
	res varchar(20) := '';
	reg int:= 0;
begin
	if opc = 'N' then
	    select max(id_profesor)+1 into reg from profesor;
		if reg isnull then 
			reg :=1;
		end if;
		insert into profesor values(reg,nom,age,mail);
		res := 'Registro Agregado';
	end if;
	if opc = 'M' then
		update profesor set nombre=nom, edad=age, correo=mail where id_profesor=id;
		res := 'Registro Modificado';
	end if;
	if opc = 'E' then
		delete from profesor where id_profesor=id;
		res := 'Registro Eliminado';
	end if;	
	return res;
end;
$$
language plpgsql;

-- actualizar tabla alumno
create or replace function fn_alumno(char(1),int,varchar(50),int,varchar(30))
returns varchar(20)
as $$
declare
	opc char(1):= $1;
	id int:= $2;
	nom varchar(50):= $3;
	age int:= $4;
	mail varchar(30):= $5;
	res varchar(20) := '';
	reg int:= 0;
begin
	if opc = 'N' then
	    select max(id_alumno)+1 into reg from alumno;
		if reg isnull then 
			reg :=1;
		end if;
		insert into alumno values(reg,nom,age,mail);
		res := 'Registro Agregado';
	end if;
	if opc = 'M' then
		update alumno set nombre=nom, edad=age, correo=mail where id_alumno=id;
		res := 'Registro Modificado';
	end if;
	if opc = 'E' then
		delete from alumno where id_alumno=id;
		res := 'Registro Eliminado';
	end if;	
	return res;
end;
$$
language plpgsql;

-- actualizar tabla curso
create or replace function fn_curso(char(1),int,varchar(30),int)
returns varchar(20)
as $$
declare
	opc char(1):= $1;
	id int:= $2;
	nom varchar(30):= $3;
	prof int:= $4;
	res varchar(20) := '';
	reg int:= 0;
begin
	if opc = 'N' then
	    select max(id_curso)+1 into reg from curso;
		if reg isnull then 
			reg :=1;
		end if;
		insert into curso values(reg,nom,prof);
		res := 'Registro Agregado';
	end if;
	if opc = 'M' then
		update curso set nombre=nom, id_profesor=prof where id_curso=id;
		res := 'Registro Modificado';
	end if;
	if opc = 'E' then
		delete from curso where id_curso=id;
		res := 'Registro Eliminado';
	end if;	
	return res;
end;
$$
language plpgsql;

-- actualizar tabla matricula
create or replace function fn_matricula(char(1),int,int,int,char(1))
returns varchar(20)
as $$
declare
	opc char(1):= $1;
	id int:= $2;
	alum int:= $3;
	aula int:= $4;
	est char(1):= $5;
	res varchar(20) := '';
	reg int:= 0;
begin
	if opc = 'N' then
	    select max(id_matricula)+1 into reg from matricula;
		if reg isnull then 
			reg :=1;
		end if;
		insert into matricula values(reg,alum,aula,est);
		res := 'Registro Agregado';
	end if;
	if opc = 'M' then
		update matricula set id_alumno=alum, id_salon=aula, estado=est where id_matricula=id;
		res := 'Registro Modificado';
	end if;
	if opc = 'E' then
		delete from matricula where id_matricula=id;
		res := 'Registro Eliminado';
	end if;	
	return res;
end;
$$
language plpgsql;


--CRUD
--Creación 
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
select fn_alumno('N',0,'BENDEZU JANAMPA LILIANA',14,'bendezu@gmail.com');
select fn_alumno('N',0,'PARA BORRADO',30,'borrado@gmail.com');
--datos curso
select fn_curso('N',0,'MATEMATICAS 1',1);
select fn_curso('N',0,'COMUNICACION 1',2);
select fn_curso('N',0,'MATEMATICAS 2',3);
select fn_curso('N',0,'COMUNICACION 2',2);
--datos bimestre
insert into bimestre(nombre) values('1er.Bimestre');
insert into bimestre(nombre) values('2do.Bimestre');
insert into bimestre(nombre) values('3er.Bimestre');
insert into bimestre(nombre) values('4to.Bimestre');

--datos matricula
select fn_matricula('N',0,1,1,'A');
select fn_matricula('N',0,2,1,'A');
select fn_matricula('N',0,3,1,'A');
select fn_matricula('N',0,4,2,'A');
select fn_matricula('N',0,5,2,'A');
select fn_matricula('N',0,6,2,'A');

--datos salon cursos
insert into salon_cursos values(1,1,'A');
insert into salon_cursos values(1,2,'A');
insert into salon_cursos values(2,1,'A');
insert into salon_cursos values(2,2,'A');
insert into salon_cursos values(3,3,'A');
insert into salon_cursos values(3,4,'A');
insert into salon_cursos values(4,3,'A');
insert into salon_cursos values(4,4,'A');

--datos notas alumnos
insert into notas_alumno values(1,1,1,12);
insert into notas_alumno values(1,2,1,14);
insert into notas_alumno values(1,1,2,15);
insert into notas_alumno values(1,2,2,13);
insert into notas_alumno values(2,1,1,16);
insert into notas_alumno values(2,2,1,15);
insert into notas_alumno values(2,1,2,17);
insert into notas_alumno values(2,2,2,16);
insert into notas_alumno values(3,1,1,15);
insert into notas_alumno values(3,2,1,16);
insert into notas_alumno values(4,1,1,18);
insert into notas_alumno values(4,2,1,14);
insert into notas_alumno values(4,1,2,12);
insert into notas_alumno values(4,2,2,13);

--Read
select * from salon;
select * from profesor;
select * from alumno;
select a.*,b.nombre as profesor from curso as a inner join profesor as b on a.id_profesor=b.id_profesor;
select * from bimestre;
select a.*,b.nombre as alumno,c.nombre as salon, case a.estado when 'A' then 'Activo' else 'Inactivo' end as cest
	from matricula as a inner join alumno as b on a.id_alumno=b.id_alumno inner join salon as c on a.id_salon=c.id_salon;

select a.*,b.nombre as salon,c.nombre as curso, case a.estado when 'A' then 'Activo' else 'Inactivo' end as cest
	from salon_cursos as a inner join salon as b on a.id_salon=b.id_salon inner join curso as c on a.id_curso=c.id_curso;

select a.id_matricula,c.nombre as alumno,d.nombre as salon,f.nombre as profesor,e.nombre as curso,g.nombre as bimestre,a.nota
from notas_alumno as a 
inner join matricula as b on a.id_matricula=b.id_matricula
inner join alumno as c on b.id_alumno=c.id_alumno
inner join salon as d on b.id_salon=d.id_salon
inner join curso as e on a.id_curso=e.id_curso
inner join profesor as f on e.id_profesor=f.id_profesor
inner join bimestre as g on a.id_bimestre=g.id_bimestre
;

--Update
--Cambiando datos el salon
select fn_salon('M',1,'PRIMERO C',2021);
select fn_salon('M',1,'PRIMERO A',2021);
--Cambiando datos del alumno
select fn_alumno('M',3,'GARCIA PORRRAS PERCY',11,'garciaporras@gmail.com');

--Delete
---borrado de un alumno
select fn_alumno('E',7,'',0,'');
---borrado de notas
delete from notas_alumno where id_matricula=4 and id_curso=2 and id_bimestre=2;
