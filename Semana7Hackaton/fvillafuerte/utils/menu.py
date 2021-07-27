import os
import time
from utils.utils import alinear_texto

#-----------------
### CLASE MENU ###
class Menu:
    def __init__(self, name, op_list, pre_menu=0):
        self.name = name
        self.op_list = op_list
        self.pre_menu = pre_menu

    def show(self):
        a = True
        while a:
            self.limpiarPantalla()
            print(alinear_texto("",40,"-","C"))
            print(alinear_texto(self.name.upper(),40,":","C"))
            print(alinear_texto("",40,"-","C"))
            print("")
            for (key, value) in self.op_list.items():
                print("[" + value + "] " + key)
            print("")
            ans = input("Opción: ")
            print("")
            if(ans.upper() == "0"):
                break
            b = 0
            for (key, value) in self.op_list.items():
                if (value == ans):
                    b = b+1
            if (b > 0):
                a = False
            else:
                print("Opción no valida, escoja una opción valida")
                time.sleep(2)
        return ans

    def limpiarPantalla(self):
        def clear():
            return os.system('clear')
        clear()