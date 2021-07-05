import time


class Persona:
    def __init__(self, dni, nombre, apellido):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
    
        
    
                
class Usuario(Persona):
    def __init__(self,codUsuario, dni, nombre, apellido):
        Persona.__init__(dni, nombre, apellido)
        self.dni = "C"+ codUsuario  
        
    
       
class Asistencia(Usuario):
    def __init__(self, nombre, apellido, codUsuario, fechaHora):
        Usuario.__init__(nombre, apellido, codUsuario)
        self.fechaHora = time.strftime("%c")
        return (time.strftime("%c"))
        
  
print("MENÚ REGISTROS\n\n1)-Nuevo Usuario\n2)-Mostrar\n3)-Eliminar Registros")

opc = input("Elige una opción: ")
if opc == "1":
    print("Nuevo Registro\n")
    registro = open("registro.csv" , "a")
    
    dni = input("Ingrese número de dni: ")
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    print("Registro exitoso: "+ nombre + " " + apellido + " " + dni) 
      
    registro.write(dni)
    registro.write(",")
    registro.write(nombre)
    registro.write(",")
    registro.write(apellido)
    registro.write("\n")
    
    registro.close()
    
elif opc == "2":
    print("Mostrar Registros\n")
    registro = open("registro.csv")
    
    print(registro.read())
    
    registro.close()    

elif opc == "3":
    registro = open("registro.csv", "a")
    registro.truncate()
    
    print("Registros eliminados")
    
    registro.close()
    
else:
    print("Debes ingresar al menos un registro")   