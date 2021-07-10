-- DDL --

CREATE DATABASE colegio;

CREATE TABLE profesor(
    idprofesor SERIAL,
    nombre VARCHAR(45) NOT NULL,
    codprofesor VARCHAR(8) NOT NULL,
    edad INT NOT NULL,
    correo VARCHAR(45) NOT NULL,
    CONSTRAINT pk_profesor PRIMARY KEY(idprofesor)
);

CREATE TABLE horarioprofesor(
    idhorario SERIAL,
    horainicio TIME NOT NULL,
    horafin TIME NOT NULL,
    dia DATE NOT NULL,
    CONSTRAINT pk_horarioprofesor PRIMARY KEY(idhorario)
);

CREATE TABLE profesor_has_horarioprofesor(
    idprofesor_profesor INT,
    idhorario_horarioprofesor INT,
    CONSTRAINT fk_profesor FOREIGN KEY(idprofesor_profesor) REFERENCES profesor(idprofesor),
    CONSTRAINT fk_horarioprofesor FOREIGN KEY(idhorario_horarioprofesor) REFERENCES horarioprofesor(idhorario)
);
CREATE TABLE alumno(
    idalumno SERIAL,
    nombre VARCHAR(45) NOT NULL,
    codalumno VARCHAR(8) NOT NULL,
    edad INT NOT NULL, 
    correo VARCHAR(45) NOT NULL,
    CONSTRAINT pk_alumno PRIMARY KEY(idalumno)
);

CREATE TABLE salon(
    idsalon SERIAL,
    nombre VARCHAR(45) NOT NULL,
    anoescolar DATE NOT NULL,
    codsalon VARCHAR(8) NOT NULL,
    idprofesor_profesor INT,
    idalumno_alumno INT,
    CONSTRAINT pk_salon PRIMARY KEY(idsalon),
    CONSTRAINT fk_profesor FOREIGN KEY(idprofesor_profesor) REFERENCES profesor(idprofesor),
    CONSTRAINT fk_alumno FOREIGN KEY(idalumno_alumno) REFERENCES alumno(idalumno)
);

CREATE TABLE curso(
    idcurso SERIAL,
    nombre VARCHAR(45) NOT NULL,
    codcurso VARCHAR(8) NOT NULL,
    CONSTRAINT pk_curso PRIMARY KEY(idcurso)
);

CREATE TABLE bimestre(
    idbimestre SERIAL,
    nombre VARCHAR(45) NOT NULL,
    codbimestre VARCHAR(8) NOT NULL,
    CONSTRAINT pk_bimestre PRIMARY KEY(idbimestre)
);

CREATE TABLE curso_has_bimestre(
    idcurso_curso INT,
    idbimestre_bimestre INT,
    CONSTRAINT fk_curso FOREIGN KEY(idcurso_curso) REFERENCES curso(idcurso),
    CONSTRAINT fk_bimestre FOREIGN KEY(idbimestre_bimestre) REFERENCES bimestre(idbimestre)
);
                --- CRUD ---

-- DML --

-- Create

INSERT INTO profesor VALUES ('01', 'Juan Diego Gomez', 'prf01', '28', 'juangomez@san-jose.edu');
INSERT INTO profesor VALUES ('02', 'Maria Teresa Bautista', 'prf02', '41', 'mariabautista@san-jose.edu');
INSERT INTO profesor VALUES ('03', 'Julia Salcedo', 'prf03', '45', 'juliasalcedo@san-jose.edu');
INSERT INTO profesor VALUES ('04', 'Carlos Leon', 'prf04', '39', 'carlosleon@san-jose.edu');
INSERT INTO profesor VALUES ('05', 'Alexander Guillermo', 'prf05', '39', 'alexanderguillermo@san-jose.edu');

INSERT INTO horarioprofesor VALUES ('01','08:00', '09:00', '05/07/2021');
INSERT INTO horarioprofesor VALUES ('02','09:00', '10:00', '05/07/2021');
INSERT INTO horarioprofesor VALUES ('03','11:00', '12:00', '05/07/2021');
INSERT INTO horarioprofesor VALUES ('04','12:00', '13:00', '05/07/2021');
INSERT INTO horarioprofesor VALUES ('05','13:00', '14:00', '05/07/2021');
INSERT INTO horarioprofesor VALUES ('06','08:00', '09:00', '06/07/2021');
INSERT INTO horarioprofesor VALUES ('07','09:00', '10:00', '06/07/2021');
INSERT INTO horarioprofesor VALUES ('08','11:00', '12:00', '06/07/2021');
INSERT INTO horarioprofesor VALUES ('09','12:00', '13:00', '06/07/2021');
INSERT INTO horarioprofesor VALUES ('10','13:00', '14:00', '06/07/2021');
INSERT INTO horarioprofesor VALUES ('11','08:00', '09:00', '07/07/2021');
INSERT INTO horarioprofesor VALUES ('12','09:00', '10:00', '07/07/2021');
INSERT INTO horarioprofesor VALUES ('13','11:00', '12:00', '07/07/2021');
INSERT INTO horarioprofesor VALUES ('14','12:00', '13:00', '07/07/2021');
INSERT INTO horarioprofesor VALUES ('15','13:00', '14:00', '07/07/2021');
INSERT INTO horarioprofesor VALUES ('16','08:00', '09:00', '08/07/2021');
INSERT INTO horarioprofesor VALUES ('17','09:00', '10:00', '08/07/2021');
INSERT INTO horarioprofesor VALUES ('18','11:00', '12:00', '08/07/2021');
INSERT INTO horarioprofesor VALUES ('19','12:00', '13:00', '08/07/2021');
INSERT INTO horarioprofesor VALUES ('20','13:00', '14:00', '08/07/2021');
INSERT INTO horarioprofesor VALUES ('21','08:00', '09:00', '09/07/2021');
INSERT INTO horarioprofesor VALUES ('22','09:00', '10:00', '09/07/2021');
INSERT INTO horarioprofesor VALUES ('23','11:00', '12:00', '09/07/2021');
INSERT INTO horarioprofesor VALUES ('24','12:00', '13:00', '09/07/2021');
INSERT INTO horarioprofesor VALUES ('25','13:00', '14:00', '09/07/2021');

INSERT INTO alumno VALUES ('01','Jose Rodriguez', 'alu01', '17', 'jose@gmail.com');
INSERT INTO alumno VALUES ('02','Christian Yuen', 'alu02', '19', 'christian@hotmail.com');
INSERT INTO alumno VALUES ('03','Antonio Morales', 'alu03', '18', 'antonio@yahoo.com');
INSERT INTO alumno VALUES ('04','Miriam Rodriguez', 'alu04', '17', 'jose@gmail.com');
INSERT INTO alumno VALUES ('05','Eduardo Floiras', 'alu05', '21', 'eduardo@gmail.com');
INSERT INTO alumno VALUES ('06','Lizbeth Rodriguez', 'alu06', '17', 'jose@gmail.com');
INSERT INTO alumno VALUES ('07','Justina Becker', 'alu07', '21', 'justina@yahoo.com');
INSERT INTO alumno VALUES ('08','Juan Quispe', 'alu08', '19', 'juanquispe@hotmail.com');
INSERT INTO alumno VALUES ('09','Maritza Rabi', 'alu09', '19', 'maritza@hotmail.com');
INSERT INTO alumno VALUES ('10','Kary Salinas', 'alu10', '21', 'jose@gmail.com');

INSERT INTO salon VALUES ('01','Aula de Computo', '2021', 'COM01');
INSERT INTO salon VALUES ('02','Aula de Laboratorio', '2021', 'LAB01');
INSERT INTO salon VALUES ('03','Aula de Musica', '2021', 'MUS01');
INSERT INTO salon VALUES ('04','Aula de Clases', '2021', 'CLA01');
INSERT INTO salon VALUES ('05','Aula de Fisica', '2021', 'FIS01');

INSERT INTO curso VALUES ('01','HTML', 'C01');
INSERT INTO curso VALUES ('02','Ofimatica', 'C02');
INSERT INTO curso VALUES ('03','Biologia', 'C03');
INSERT INTO curso VALUES ('04','Quimica Basica', 'C04');
INSERT INTO curso Values ('05','Musica Escolar', 'C05')
INSERT INTO curso VALUES ('06','Matematica', 'C07');
INSERT INTO curso VALUES ('07','Comunicacion', 'C08');
INSERT INTO curso VALUES ('08','Personal Sociales', 'C09');
INSERT INTO curso VALUES ('09','Ingles', 'C10');
INSERT INTO curso VALUES ('10','Ciencia y Tecnologia', 'C11');
INSERT INTO curso VALUES ('11','Fisica Ciencia Escolar', 'C12');

INSERT INTO bimestre VALUES ('01','Primner Bimestre', '1B');
INSERT INTO bimestre VALUES ('02','Segundo Bimestre', '2B');
INSERT INTO bimestre VALUES ('03','Tercer Bimestre', '3B');
INSERT INTO bimestre VALUES ('04','Cuarto Bimestre', '4B');

-- Read

SELECT * FROM alumno;
SELECT * FROM bimestre;
SELECT * FROM curso;
SELECT * FROM curso_has_bimestre;
SELECT * FROM horarioprofesor;
SELECT * FROM profesor;
SELECT * FROM profesor_has_horarioprofesor;
SELECT * FROM salon;

-- Update

UPDATE alumno
SET nombre = 'Jose de San Martin',
codalumno = 'alu001',
edad = 27,
correo = 'josedesanmartin@gmail.com'
WHERE idalumno = 1;

UPDATE profesor
SET nombre = 'Simon Bolivar',
codprofesor = 'pfr001',
edad = '37',
correo = 'simonbolivar@san-jose.edu'
WHERE idprofesor = 1;

-- Delete

DELETE FROM alumno 
WHERE nombre = 'Christian Yuen'

-- Inner Join

SELECT * FROM alumno
INNER JOIN curso
on alumno.idalumno = curso.idcurso

SELECT * FROM profesor
INNER JOIN curso
ON profesor.idprofesor = curso.idcurso

-- Alter 

ALTER TABLE salon ALTER COLUMN anoescolar TYPE VARCHAR(4)
