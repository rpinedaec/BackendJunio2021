from models.alumno import Alumno
from utils.utils import log

log = log("Inicio")
log.info("Inicio de la aplicacion")
try:
    nroAlumnos = int(input("Ingrese el numero de Alumnos: "))
    i = 1
    listaAlumnos = []
    while True:
        if i > nroAlumnos: break
        estudiante = input(f"Ingrese el nombre del Estudiante {i}: ")
        nroNotas = int(input("Ingrese el numero de notas para el estudiante: "))
        listaNotas = []
        log.debug("ingreso a nroNotas "+str(nroNotas))
        n = 1
        while True:
            try:
                if n > nroNotas: break
                nota = int(input(f"ingrese la nota {n}: "))
                listaNotas.append(nota)
                n += 1
            except ValueError as error:
                log.error(error)
        alumno = Alumno(estudiante,listaNotas)
        listaAlumnos.append(alumno)
        i += 1
    res = Alumno.ingresarAlumno(listaAlumnos)
    print (res)
except Exception as err:
    log.error(err)
