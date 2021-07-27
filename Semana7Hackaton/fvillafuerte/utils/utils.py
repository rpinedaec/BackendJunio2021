import logging
import os

class log:
    def __init__(self, nombreLogger):
        # create logger
        self.logger = logging.getLogger(nombreLogger)
        self.logger.filename = 'app.log'
        self.logger.setLevel(logging.DEBUG)
        # create console handler and set level to debug
        ch = logging.FileHandler("app.log", mode='a')
        ch.setLevel(logging.DEBUG)
        # create formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # add formatter to ch
        ch.setFormatter(formatter)
        # add ch to logger
        self.logger.addHandler(ch)

    def debug(self, mensaje):
        self.logger.debug(mensaje)

    def info(self, mensaje):
        self.logger.info(mensaje)

    def warning(self, mensaje):
        self.logger.warning(mensaje)

    def error(self, mensaje):
        self.logger.error(mensaje)

    def critical(self, mensaje):
        self.logger.critical(mensaje)


class fileManager:
    logD = log("fileManager")

    def __init__(self, nombreArchivo):
        self.nombreArchivo = nombreArchivo

    def leerArchivo(self):
        try:
            file = open(self.nombreArchivo,'r')
            return file.read()
        except Exception as e:
            return e
        

    def borrarArchivo(self):
        directorioActual = os.getcwd()
        path = directorioActual+"\\"+self.nombreArchivo
        self.logD.debug(path)
        if(os.path.isfile(path)):
            try:
                os.remove(path)
                self.logD.debug("removiendo archivo")

            except Exception as error:
                self.logD.error(error)

    def escribirArchivo(self, linea):
        try:
            directorioActual = os.getcwd()
            path = directorioActual+"\\"+self.nombreArchivo
            self.logD.debug(path)
            if(os.path.isfile(path)):
                try:
                    #escribir el archiv
                    file = open(self.nombreArchivo, 'a')
                    file.write(linea + "\n")
                except Exception as e:
                    self.logD.error(e)
                finally:
                    file.close()
            else:
                file = open(self.nombreArchivo, 'w')
                file.close()
                file = open(self.nombreArchivo, 'a')
                file.write(linea + "\n")
        except Exception as error:
            self.logD.error(error)

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