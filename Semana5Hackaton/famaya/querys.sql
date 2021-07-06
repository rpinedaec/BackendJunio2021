use colegio;
/*Listado de alumnos por salon*/

select al.codigo_alumno,concat(al.nombres,' ',al.apellido_paterno,' ',al.apellido_materno) as alumno,
s.nombre as salon
from alumnos al
inner join salon s on al.id_salon = s.id_salon

/*Alumnos por salon*/

select s.codigo_salon, s.nombre, count(al.id_alumno)
from alumnos al
inner join salon s on al.id_salon = s.id_salon
group by s.codigo_salon,s.nombre 

/*Cursos - Profesores*/

select cu.codigo_curso,cu.nombre as curso, 
concat(pf.nombres,' ',pf.apellido_paterno,' ',pf.apellido_materno ) as profesor
from cursos cu
inner join profesores pf on cu.id_profesor = pf.id_profesor

/*profesores - Curso - Salon*/

select  
concat(pf.nombres,' ',pf.apellido_paterno,' ',pf.apellido_materno ) as profesor, cu.nombre as curso,
s.nombre as salon, s.anio_escolar
from salon s 
inner join cursos cu on s.id_curso = cu.id_curso
inner join profesores pf on pf.id_profesor = cu.id_profesor

/*Alumnos - Proferores - Cursos*/

select  
s.nombre as salon, 
concat(pf.nombres,' ',pf.apellido_paterno,' ',pf.apellido_materno ) as profesor, 
cu.nombre as curso,
concat(al.nombres,' ',al.apellido_paterno,' ',al.apellido_materno) as alumno,
s.anio_escolar
from salon s 
inner join cursos cu on s.id_curso = cu.id_curso
inner join profesores pf on pf.id_profesor = cu.id_profesor
inner join alumnos al on al.id_salon = s.id_salon

/*Alumnos - Cursos*/

select 
concat(al.nombres,' ',al.apellido_paterno,' ',al.apellido_materno) as alumno,
cu.nombre as curso
from alumnos al
inner join salon sa on al.id_salon = sa.id_salon
inner join cursos cu on cu.id_curso = sa.id_curso