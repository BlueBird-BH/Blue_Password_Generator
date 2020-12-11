from random import SystemRandom
import menu

caracteresNumericos = "1234567890"
caracteresLetras_mayusculas = "QWERTYUIOPASDFGHJKLZXCVBNM"
caracteresLetras_minusculas = "qwertyuiopasdfghjklzxcvbnm"
caracteresSimbolos = "!#$%&/()=?¿¡-_<>+*}{[]@"

valoresClave = caracteresNumericos + caracteresLetras_mayusculas + caracteresLetras_minusculas + caracteresSimbolos

def generadorClaves():
    longitudClave = input("╚═─[Ingrese la longitud que deseas]→ ")
    caracteresRestantes = int(longitudClave)
    claveGenerada = ""

    while caracteresRestantes > 0:
        claveGenerada = claveGenerada + SystemRandom().choice(valoresClave)
        caracteresRestantes -= 1

    menu.mensajeBienvenida()
    print("╠═→ Esta es la contraseña generada")
    print(f"║   con una longitud de {longitudClave} caracteres → {claveGenerada}\n")

if __name__ == "__main__":
    try:
        menu.mensajeBienvenida()
        generadorClaves()
        menu.enterContinuar()
    except KeyboardInterrupt:
        menu.mensajeDespedida()
