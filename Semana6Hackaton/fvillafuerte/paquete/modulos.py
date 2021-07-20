import os
from tabulate import tabulate

def pedirNumeroEntero(strMsg):
    correcto = False
    num = 0
    while(not correcto):
        try:
            num = int(input(strMsg))
            correcto = True
        except ValueError:
            print('Error, Ingrese número entero')
    return num

def pedirDNI():
    correcto = False
    while(not correcto):
        num = pedirNumeroEntero("N° DNI: ")
        if len(str(num)) == 8:
            correcto = True
        else:
            print("N° de dígitos incorrectos")
    return str(num)

def valOpc():
    correcto = False
    while(not correcto):
        opc = input("Está seguro de Elimar todos los datos de este registro? [S]i, [N]o : ")
        opc = opc.upper()
        if opc == 'S' or opc == 'N' :
            correcto = True
        else:
            print("Opción no válida, ...")
    return opc

### FUNCION ALIENAR TEXTO
def alinear_texto(strTexto,intAncho,strCad,strOPC):
    intLong = len(strTexto)
    if intLong <= intAncho:
        if strOPC == "I":
            strC1 = ""
            strC2 = strCad * (intAncho - intLong)        
        if strOPC == "C":
            intPos = int((intAncho - intLong) / 2)
            strC1 = strCad * intPos
            strC2 = strCad * (intAncho - (intPos + intLong))
        if strOPC == "D":
            strC1 = strCad * (intAncho - intLong)
            strC2 = ""        
        strTexto = strC1 + strTexto + strC2
    else:
        raise ValueError("Nro. caracteres superior al ancho de alineación")
    return strTexto


### FUNCIONES DE TABLA SALON
def InsertSalon(conn):
    os.system('clear')
    print(alinear_texto("REGISTRAR DATOS SALON",40," ","C"))
    print(alinear_texto("",40,"=","C"))
    nombre = input("Nombre de Salón: ")
    a_esco = pedirNumeroEntero("Año Escolar: ")
    query = f"""select fn_salon('N',0,'{nombre.upper()}',{a_esco});"""
    result = conn.ejecutarBDD(query)
    if(result):
        input("Se grabó correctamente.., presione una tecla para continuar")

def UpdateSalon(conn):
    os.system('clear')
    print(alinear_texto("MODIFICAR DATOS SALON",40," ","C"))
    print(alinear_texto("",40,"=","C"))
    id_reg = pedirNumeroEntero("ID Salón: ")
    query = f"""select * from salon where id_salon = {id_reg};"""
    result = conn.consultarBDD(query)
    if(len(result) == 0):
        input("No existe ID.., presione una tecla para continuar")
    if(len(result) == 1):
        print(tabulate(result, headers=['ID', 'SALON', 'AÑO ESCOLAR'], tablefmt='simple'))
        print("")
        nombre = input("Nombre de Salón: ")
        a_esco = pedirNumeroEntero("Año Escolar: ")
        query = f"""select fn_salon('M',{id_reg},'{nombre.upper()}',{a_esco});"""
        result = conn.ejecutarBDD(query)
        if(result):
            input("Se actualizó  correctamente.., presione una tecla para continuar")

def DeleteSalon(conn):
    os.system('clear')
    print(alinear_texto("ELIMINAR DATOS SALON",40," ","C"))
    print(alinear_texto("",40,"=","C"))
    id_reg = pedirNumeroEntero("ID Salón a Eliminar: ")
    query = f"""select * from salon where id_salon = {id_reg};"""
    result = conn.consultarBDD(query)
    if(len(result) == 0):
        input("No existe ID.., presione una tecla para continuar")
    if(len(result) == 1):
        print(tabulate(result, headers=['ID', 'SALON', 'AÑO ESCOLAR'], tablefmt='simple'))
        print("")
        opc = valOpc()
        if opc == "S":
            query = f"""select fn_salon('E',{id_reg},'',0);"""
            result = conn.ejecutarBDD(query)
            if(result):
                input("Se eliminó  correctamente.., presione una tecla para continuar")


### FUNCIONES DE TABLA PROFESOR
def InsertProfesor(conn):
    os.system('clear')
    print(alinear_texto("REGISTRAR DATOS PROFESOR",40," ","C"))
    print(alinear_texto("",40,"=","C"))
    nombre = input("Apellidos y Nombres: ")
    edad = pedirNumeroEntero("Edad: ")
    correo = input("Correo Electrónico: ")
    query = f"""select fn_profesor('N',0,'{nombre.upper()}',{edad},'{correo}');"""
    result = conn.ejecutarBDD(query)
    if(result):
        input("Se grabó correctamente.., presione una tecla para continuar")

def UpdateProfesor(conn):
    os.system('clear')
    print(alinear_texto("MODIFICAR DATOS PROFESOR",40," ","C"))
    print(alinear_texto("",40,"=","C"))
    id_reg = pedirNumeroEntero("ID Profesor: ")
    query = f"""select * from profesor where id_profesor = {id_reg};"""
    result = conn.consultarBDD(query)
    if(len(result) == 0):
        input("No existe ID.., presione una tecla para continuar")
    if(len(result) == 1):
        print(tabulate(result, headers=['ID', 'APELLIDOS Y NOMBRES', 'EDAD', 'CORREO'], tablefmt='simple'))
        print("")
        nombre = input("Apellidos y Nombres: ")
        edad = pedirNumeroEntero("Edad: ")
        correo = input("Correo Electrónico: ")
        query = f"""select fn_profesor('M',{id_reg},'{nombre.upper()}',{edad},'{correo}');"""
        result = conn.ejecutarBDD(query)
        if(result):
            input("Se actualizó  correctamente.., presione una tecla para continuar")

def DeleteProfesor(conn):
    os.system('clear')
    print(alinear_texto("ELIMINAR DATOS PROFESOR",40," ","C"))
    print(alinear_texto("",40,"=","C"))
    id_reg = input("ID Profesor a Eliminar: ")
    query = f"""select * from profesor where id_profesor = {id_reg};"""
    result = conn.consultarBDD(query)
    if(len(result) == 0):
        input("No existe ID.., presione una tecla para continuar")
    if(len(result) == 1):
        print(tabulate(result, headers=['ID', 'APELLIDOS Y NOMBRES', 'EDAD', 'CORREO'], tablefmt='simple'))
        print("")
        opc = valOpc()
        if opc == "S":
            query = f"""select fn_profesor('E',{id_reg},'',0,'');"""
            result = conn.ejecutarBDD(query)
            if(result):
                input("Se eliminó  correctamente.., presione una tecla para continuar")


### FUNCIONES DE TABLA ALUMNO
def InsertAlumno(conn):
    os.system('clear')
    print(alinear_texto("REGISTRAR DATOS ALUMNO",40," ","C"))
    print(alinear_texto("",40,"=","C"))
    nombre = input("Apellidos y Nombres: ")
    edad = pedirNumeroEntero("Edad: ")
    correo = input("Correo Electrónico: ")
    query = f"""select fn_alumno('N',0,'{nombre.upper()}',{edad},'{correo}');"""
    result = conn.ejecutarBDD(query)
    if(result):
        input("Se grabó correctamente.., presione una tecla para continuar")

def UpdateAlumno(conn):
    os.system('clear')
    print(alinear_texto("MODIFICAR DATOS ALUMNO",40," ","C"))
    print(alinear_texto("",40,"=","C"))
    id_reg = pedirNumeroEntero("ID Alumno: ")
    query = f"""select * from alumno where id_alumno = {id_reg};"""
    result = conn.consultarBDD(query)
    if(len(result) == 0):
        input("No existe ID.., presione una tecla para continuar")
    if(len(result) == 1):
        print(tabulate(result, headers=['ID', 'APELLIDOS Y NOMBRES', 'EDAD', 'CORREO'], tablefmt='simple'))
        print("")
        nombre = input("Apellidos y Nombres: ")
        edad = pedirNumeroEntero("Edad: ")
        correo = input("Correo Electrónico: ")
        query = f"""select fn_alumno('M',{id_reg},'{nombre.upper()}',{edad},'{correo}');"""
        result = conn.ejecutarBDD(query)
        if(result):
            input("Se actualizó  correctamente.., presione una tecla para continuar")

def DeleteAlumno(conn):
    os.system('clear')
    print(alinear_texto("ELIMINAR DATOS ALUMNO",40," ","C"))
    print(alinear_texto("",40,"=","C"))
    id_reg = input("ID Alumno a Eliminar: ")
    query = f"""select * from alumno where id_alumno = {id_reg};"""
    result = conn.consultarBDD(query)
    if(len(result) == 0):
        input("No existe ID.., presione una tecla para continuar")
    if(len(result) == 1):
        print(tabulate(result, headers=['ID', 'APELLIDOS Y NOMBRES', 'EDAD', 'CORREO'], tablefmt='simple'))
        print("")
        opc = valOpc()
        if opc == "S":
            query = f"""select fn_alumno('E',{id_reg},'',0,'');"""
            result = conn.ejecutarBDD(query)
            if(result):
                input("Se eliminó  correctamente.., presione una tecla para continuar")


### FUNCIONES DE TABLA CURSOS
def InsertCurso(conn):
    os.system('clear')
    print(alinear_texto("REGISTRAR CURSO",40," ","C"))
    print(alinear_texto("",40,"=","C"))
    nombre = input("NOMBRE DEL CURSO: ")
    id_prof = pedirNumeroEntero("ID Profesor: ")
    query = f"""select * from profesor where id_profesor = {id_prof};"""
    result = conn.consultarBDD(query)
    if(len(result) == 0):
        input("No existe ID del Profesor.., presione una tecla para continuar")
    if(len(result) == 1):
        query = f"""select fn_curso('N',0,'{nombre.upper()}',{id_prof});"""
        result = conn.ejecutarBDD(query)
        if(result):
            input("Se grabó correctamente.., presione una tecla para continuar")

def UpdateCurso(conn):
    os.system('clear')
    print(alinear_texto("MODIFICAR DATOS CURSO",40," ","C"))
    print(alinear_texto("",40,"=","C"))
    id_reg = pedirNumeroEntero("ID Curso: ")
    query = f"""select a.*,b.nombre as profesor from curso as a inner join profesor as b on a.id_profesor=b.id_profesor where a.id_curso = {id_reg};"""
    result = conn.consultarBDD(query)
    if(len(result) == 0):
        input("No existe ID.., presione una tecla para continuar")
    if(len(result) == 1):
        print(tabulate(result, headers=['ID CURSO', 'CURSO', 'ID PROF.', 'PROFESOR'], tablefmt='simple'))
        print("")
        nombre = input("NOMBRE DEL CURSO: ")
        id_prof = pedirNumeroEntero("ID Profesor: ")
        query = f"""select * from profesor where id_profesor = {id_prof};"""
        result = conn.consultarBDD(query)
        if(len(result) == 0):
            input("No existe ID del Profesor.., presione una tecla para continuar")
        if(len(result) == 1):
            query = f"""select fn_curso('M',{id_reg},'{nombre.upper()}',{id_prof});"""
            result = conn.ejecutarBDD(query)
            if(result):
                input("Se grabó correctamente.., presione una tecla para continuar")

def DeleteCurso(conn):
    os.system('clear')
    print(alinear_texto("ELIMINAR CURSOS",40," ","C"))
    print(alinear_texto("",40,"=","C"))
    id_reg = input("ID Curso a Eliminar: ")
    query = f"""select a.*,b.nombre as profesor from curso as a inner join profesor as b on a.id_profesor=b.id_profesor where a.id_curso = {id_reg};"""
    result = conn.consultarBDD(query)
    if(len(result) == 0):
        input("No existe ID.., presione una tecla para continuar")
    if(len(result) == 1):
        print(tabulate(result, headers=['ID CURSO', 'CURSO', 'ID PROF.', 'PROFESOR'], tablefmt='simple'))
        print("")
        opc = valOpc()
        if opc == "S":
            query = f"""select fn_curso('E',{id_reg},'',0');"""
            result = conn.ejecutarBDD(query)
            if(result):
                input("Se eliminó  correctamente.., presione una tecla para continuar")


### FUNCIONES DE TABLA CURSOS POR SALON
def InsertCursoSalon(conn):
    os.system('clear')
    print(alinear_texto("REGISTRAR CURSO X SALON",40," ","C"))
    print(alinear_texto("",40,"=","C"))
    id_salon = pedirNumeroEntero("ID Salón: ")
    query = f"""select * from salon where id_salon = {id_salon};"""
    result = conn.consultarBDD(query)
    if(len(result) == 0):
        input("No existe ID del salón.., presione una tecla para continuar")        
    if(len(result) == 1):
        print(result[0][1]) 
        id_curso = pedirNumeroEntero("ID Curso: ")
        query = f"""select * from curso where id_curso = {id_curso};"""
        result2 = conn.consultarBDD(query)
        if(len(result2) == 0):
            input("No existe ID del curso.., presione una tecla para continuar")
        if(len(result2) == 1):
            print(result2[0][1]) 
            estado = input("Estado [A]ctivo [I]nactivo: ")            
            query = f"""insert into salon_cursos values({id_salon},{id_curso},'{estado.upper()}');"""
            result2 = conn.ejecutarBDD(query)
            if(result2):
                input("Se grabó correctamente.., presione una tecla para continuar")


def DeleteCursoSalon(conn):
    os.system('clear')
    print(alinear_texto("ELIMINAR CURSOS X SALON",40," ","C"))
    print(alinear_texto("",40,"=","C"))
    id_salon = pedirNumeroEntero("ID Salón a Eliminar: ")
    query = f"""select distinct b.nombre from salon_cursos as a inner join salon as b on a.id_salon=b.id_salon where a.id_salon = {id_salon};"""
    result = conn.consultarBDD(query)
    if(len(result) == 0):
        input("No existe ID del salón.., presione una tecla para continuar")        
    if(len(result) == 1):
        print(result[0][0]) 
        id_curso = pedirNumeroEntero("ID Curso a Eliminar: ")
        query = f"""select a.id_salon,b.nombre as salon,a.id_curso,c.nombre as curso, case a.estado when 'A' then 'Activo' else 'Inactivo' end as cest from salon_cursos as a inner join salon as b on a.id_salon=b.id_salon inner join curso as c on a.id_curso=c.id_curso where a.id_salon = {id_salon} and a.id_curso = {id_curso};"""
        result2 = conn.consultarBDD(query)
        if(len(result2) == 0):
            input("No existe ID del curso.., presione una tecla para continuar")
        if(len(result2) == 1):
            print(tabulate(result2, headers=['ID SALON', 'SALON', 'ID CURSO.', 'CURSO', 'ESTADO'], tablefmt='simple'))
            print("")
            opc = valOpc()
            if opc == "S":
                query = f"""delete from salon_cursos where id_salon = {id_salon} and id_curso = {id_curso};"""
                result2 = conn.ejecutarBDD(query)
                if(result2):
                    input("Se eliminó  correctamente.., presione una tecla para continuar")


### FUNCIONES DE TABLA MATRICULA ALUMNOS
def InsertMatricula(conn):
    os.system('clear')
    print(alinear_texto("MATRICULAR ALUMNOS",40," ","C"))
    print(alinear_texto("",40,"=","C"))
    id_alumno = pedirNumeroEntero("ID Alumno: ")
    query = f"""select * from alumno where id_alumno = {id_alumno};"""
    result = conn.consultarBDD(query)
    if(len(result) == 0):
        input("No existe ID del alumno.., presione una tecla para continuar")        
    if(len(result) == 1):
        print(result[0][1]) 
        id_salon = pedirNumeroEntero("ID Salón: ")
        query = f"""select * from salon where id_salon = {id_salon};"""
        result2 = conn.consultarBDD(query)
        if(len(result2) == 0):
            input("No existe ID del salón.., presione una tecla para continuar")
        if(len(result2) == 1):
            print(result2[0][1])
            estado = input("Estado [A]ctivo [I]nactivo: ")
            query = f"""select fn_matricula('N',0,{id_alumno},{id_salon},'{estado.upper()}');"""
            result2 = conn.ejecutarBDD(query)
            if(result2):
                input("Se grabó correctamente.., presione una tecla para continuar")


def UpdateMatricula(conn):
    os.system('clear')
    print(alinear_texto("MODIFICAR MATRICULA",40," ","C"))
    print(alinear_texto("",40,"=","C"))
    id_reg = pedirNumeroEntero("ID Matricula: ")
    query = f"""select a.id_matricula,c.nombre as salon,a.id_salon,b.nombre as alumno,a.id_alumno,case a.estado when 'A' then 'Activo' else 'Inactivo' end as cest from matricula as a inner join alumno as b on a.id_alumno=b.id_alumno inner join salon as c on a.id_salon=c.id_salon where a.id_matricula = {id_reg};"""
    result = conn.consultarBDD(query)
    if(len(result) == 0):
        input("No existe ID de Matrícula.., presione una tecla para continuar")        
    if(len(result) == 1):
        print(tabulate(result, headers=['ID MATRICULA', 'SALON', 'ID_SALON', 'ALUMNO', 'ID_ALUMNO', 'ESTADO'], tablefmt='simple'))
        print("")
        id_alumno = pedirNumeroEntero("ID Alumno: ")
        query = f"""select * from alumno where id_alumno = {id_alumno};"""
        result = conn.consultarBDD(query)
        if(len(result) == 0):
            input("No existe ID del alumno.., presione una tecla para continuar")        
        if(len(result) == 1):
            print(result[0][1]) 
            id_salon = pedirNumeroEntero("ID Salón: ")
            query = f"""select * from salon where id_salon = {id_salon};"""
            result2 = conn.consultarBDD(query)
            if(len(result2) == 0):
                input("No existe ID del salón.., presione una tecla para continuar")
            if(len(result2) == 1):
                print(result2[0][1])
                estado = input("Estado [A]ctivo [I]nactivo: ")
                query = f"""select fn_matricula('M',{id_reg},{id_alumno},{id_salon},'{estado.upper()}');"""
                result2 = conn.ejecutarBDD(query)
                if(result2):
                    input("Se grabó correctamente.., presione una tecla para continuar")


def DeleteMatricula(conn):
    os.system('clear')
    print(alinear_texto("ELIMINAR MATRICULA",40," ","C"))
    print(alinear_texto("",40,"=","C"))
    id_reg = pedirNumeroEntero("ID Matricula: ")
    query = f"""select a.id_matricula,b.nombre as alumno,c.nombre as salon,case a.estado when 'A' then 'Activo' else 'Inactivo' end as cest from matricula as a inner join alumno as b on a.id_alumno=b.id_alumno inner join salon as c on a.id_salon=c.id_salon where a.id_matricula = {id_reg};"""
    result = conn.consultarBDD(query)
    if(len(result) == 0):
        input("No existe ID de Matrícula.., presione una tecla para continuar")        
    if(len(result) == 1):
        print(tabulate(result, headers=['ID MATRICULA', 'SALON', 'ALUMNO', 'ESTADO'], tablefmt='simple'))
        print("")
        opc = valOpc()
        if opc == "S":
            query = f"""select fn_matricula('E',{id_reg},0,0,'');"""
            result = conn.ejecutarBDD(query)
            if(result):
                input("Se eliminó  correctamente.., presione una tecla para continuar")


### FUNCIONES DE TABLA NOTAS DEL ALUMNO
def InsertRegNotas(conn):
    os.system('clear')
    print(alinear_texto("REGISTRAR NOTAS DEL ALUMNO",40," ","C"))
    print(alinear_texto("",40,"=","C"))
    id_salon = pedirNumeroEntero("ID Salon: ")
    query = f"""select * from salon where id_salon = {id_salon};"""
    result = conn.consultarBDD(query)
    if(len(result) == 0):
        input("No existe ID de salón.., presione una tecla para continuar")        
    if(len(result) == 1):
        print(result[0][1]) 
        id_curso = pedirNumeroEntero("ID Curso: ")
        query = f"""select b.nombre from salon_cursos as a inner join curso as b on a.id_curso=b.id_curso where a.id_salon = {id_salon} and a.id_curso = {id_curso};"""
        result2 = conn.consultarBDD(query)
        if(len(result2) == 0):
            input("No existe ID del curso.., presione una tecla para continuar")
        if(len(result2) == 1):
            print(result2[0][0]) 
            id_matricula = pedirNumeroEntero("ID Matricula: ")
            query = f"""select b.nombre from matricula as a inner join alumno as b on a.id_alumno=b.id_alumno where a.id_salon = {id_salon} and a.id_matricula = {id_matricula};"""
            result3 = conn.consultarBDD(query)
            if(len(result3) == 0):
                input("No existe ID matrícula.., presione una tecla para continuar")
            if(len(result3) == 1):
                print(result3[0][0]) 
                bimestre = pedirNumeroEntero("N° Bimestre: ")
                nota = pedirNumeroEntero("Nota: ")
                query = f"""insert into notas_alumno values({id_matricula},{id_curso},{bimestre},{nota});"""
                result3 = conn.ejecutarBDD(query)
                if(result3):
                    input("Se grabó correctamente.., presione una tecla para continuar")

def DeleteRegNotas(conn):
    os.system('clear')
    print(alinear_texto("ELIMINAR NOTAS ALUMNO",40," ","C"))
    print(alinear_texto("",40,"=","C"))
    id_salon = pedirNumeroEntero("ID Salon: ")
    query = f"""select * from salon where id_salon = {id_salon};"""
    result = conn.consultarBDD(query)
    if(len(result) == 0):
        input("No existe ID de salón.., presione una tecla para continuar")        
    if(len(result) == 1):
        print(result[0][1]) 
        id_curso = pedirNumeroEntero("ID Curso: ")
        query = f"""select b.nombre from salon_cursos as a inner join curso as b on a.id_curso=b.id_curso where a.id_salon = {id_salon} and a.id_curso = {id_curso};"""
        result2 = conn.consultarBDD(query)
        if(len(result2) == 0):
            input("No existe ID del curso.., presione una tecla para continuar")
        if(len(result2) == 1):
            print(result2[0][0]) 
            id_matricula = pedirNumeroEntero("ID Matricula: ")
            query = f"""select b.nombre from matricula as a inner join alumno as b on a.id_alumno=b.id_alumno where a.id_salon = {id_salon} and a.id_matricula = {id_matricula};"""
            result3 = conn.consultarBDD(query)
            if(len(result3) == 0):
                input("No existe ID matrícula.., presione una tecla para continuar")
            if(len(result3) == 1):
                print(result3[0][0]) 
                bimestre = pedirNumeroEntero("N° Bimestre: ")
                query = f"""select a.id_matricula,d.nombre as salon,c.nombre as alumno,f.nombre as profesor,e.nombre as curso,g.nombre as bimestre,a.nota from notas_alumno as a inner join matricula as b on a.id_matricula=b.id_matricula inner join alumno as c on b.id_alumno=c.id_alumno inner join salon as d on b.id_salon=d.id_salon inner join curso as e on a.id_curso=e.id_curso inner join profesor as f on e.id_profesor=f.id_profesor inner join bimestre as g on a.id_bimestre=g.id_bimestre where a.id_matricula={id_matricula} and a.id_curso={id_curso} and a.id_bimestre={bimestre};"""
                result4 = conn.consultarBDD(query)
                if(len(result4) == 0):
                    input("No existe notas del bimestre.., presione una tecla para continuar")
                if(len(result4) == 1):
                    print(tabulate(result4, headers=['ID MATRICULA', 'SALON', 'ALUMNO', 'PROFESOR', 'CURSO', 'BIMESTRE', 'NOTA'], tablefmt='simple'))
                    print("")
                    opc = valOpc()
                    if opc == "S":
                        query = f"""delete from notas_alumno where id_matricula = {id_matricula} and id_curso = {id_curso} and id_bimestre = {bimestre};"""
                        result4 = conn.ejecutarBDD(query)
                        if(result4):
                            input("Se eliminó  correctamente.., presione una tecla para continuar")


def ListarRegistro(conn,header,query,title):
    os.system('clear')
    print(alinear_texto(title.upper(),40," ","C"))
    print(alinear_texto("",40,"=","C"))
    result = conn.consultarBDD(query)
    print(tabulate(result, headers=header, tablefmt='fancy_grid'))
    input("Presione una tecla para continuar...")
