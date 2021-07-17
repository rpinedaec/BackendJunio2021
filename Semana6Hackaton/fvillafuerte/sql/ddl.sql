--- base de datos colegio
CREATE DATABASE hackaton6
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Spanish_Spain.1252'
    LC_CTYPE = 'Spanish_Spain.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

\c hackaton6;

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
