import sys, os

menu_options  = {}

def return_to_menu():
    input()
    menu_options['main_menu']()

def calculate_verification_digit():
    
    print("Ingrese DNI a verificar")
    dni = input("> ")
    try:
        int(dni)
    except ValueError as e:
        print("DNI inválido")
        return
    else:
        if len(dni)>8 or len(dni)<8:
            print("DNI inválido")            
            return
    
    print("Ingrese digito verificador")
    input_verify_digit = input("> ")
    
    verify_digits = [6, 7, 8, 9, 0, 1, 1, 2, 3, 4, 5]
    verify_words = ["K", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    default_list_1 = [3, 2, 7, 6, 5, 4, 3, 2]

    splitted = list(dni)
    suma_1 = 0
    for i, digit in enumerate(splitted):
        suma_1 += int(digit)*default_list_1[i]
    default_divisor = 11
    module_1 = suma_1 % default_divisor
    subtract_1 = default_divisor - module_1 if module_1 else 0
    default_plus = 1
    plus_1 = subtract_1 + default_plus
    result_verify_digit = verify_digits[plus_1-1]
    result_verify_word = verify_words[plus_1-1]

    message = "DATOS INVALIDOS"
    if (input_verify_digit == result_verify_word) or (int(input_verify_digit) == result_verify_digit):
        message = "DATOS VALIDOS"
    
    print(message)


def exec_menu(choice):
    os.system('clear')
    choice = choice.lower()
    if choice == '':
        menu_options['main_menu']()
    else:
        try:
            menu_options[choice]()
        except KeyError:
            print("Opcion invalida, intente de nuevo.\n")
            menu_options['main_menu']()
    return


def main_menu():
    os.system('clear')
    
    print("Bienvenido,"
    "\nElija una opcion:"
    "\n1. Validar DNI"
    "\n0. Salir")
    choice = input("> ")
    exec_menu(choice)

    return


def exit():
    sys.exit()


menu_options = {
    'main_menu': main_menu,
    '1': calculate_verification_digit,
    '0': exit,
}


if __name__ == "__main__":
    main_menu()