import os

def limpieza():
    if os.name == "posix":
        return os.system("clear")
    else:
        return os.system("cls")

def mensajeBienvenida():
    limpieza()
    print("╔═════════════════════════════════════════════════╗")
    print("║            Generador de Contraseñas             ║")
    print("╠═════════════════════════════════════════════════╣")
    print("║ Este programa genera contraseñas completamente  ║")
    print("║ aleatorias segun la cantidad de caracteres que  ║")
    print("║ escogas.                                        ║")
    print("║                                                 ║")
    print("║ ¡Las contraseñas mas seguras son de mas de 16   ║")
    print("║ caracteres y con variedad de simbolos!          ║")
    print("╠═════════════════════════════════════════════════╣")
    print("║ » Presione Ctrl + C para salir                  ║")
    print("╠═════════════════════════════════════════════════╝")
    print("║")

def mensajeDespedida():
    limpieza()
    print("╔═════════════════════════════════════════════════╗")
    print("║                   Cerrando...                   ║")
    print("╠═════════════════════════════════════════════════╝")
    enterContinuar()

def enterContinuar():
    print("║")
    print("╠═════════════════════════════════════════════════╗")
    print("║ » Presione Enter para continuar                 ║")
    input("╚═════════════════════════════════════════════════╝")
    limpieza()
