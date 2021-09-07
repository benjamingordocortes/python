import random
import os
import time
repeat = True
partida = 1

while repeat == True:
    lista = ["hola","prueba","ahorcado","python","cuerda"] #añadir palabras aqui
    ahorcado = ["      _____",
                "     |    |",
                "   (0<0)  |",
                "     |    |",
                "   \/|\/  |",
                "     |    |",
                "    / \   |",
                "__________|"]
    vida = 6
    eleccion = list(random.choice(lista))
    letrasUsadas = []
    resultado = []

    for i in range(len(eleccion)):
        resultado.append("_ ")

    while vida > 0:
        os.system("clear") and os.system("cls")
        print("\n".join(ahorcado))
        print("".join(resultado))
        print(f"letras usadas: "+", ".join(letrasUsadas))
        usuario = input("letra: ")
        
        if len(usuario) == 1:
            if usuario in letrasUsadas:
                print("ya esta dicha")
                time.sleep(1)
            else:
                letrasUsadas.append(usuario)
            for i in range(len(eleccion)):
                if usuario == eleccion[i]:
                    resultado[i] = usuario
                    
                    
            if usuario not in eleccion:
                vida = vida - 1
                print(f"nº intentos: {vida}") 
                ahorcado.pop(-1)
        else:
            print("solo una letra")
        if eleccion==resultado:
                    os.system("clear") and os.system("cls")
                    print("\n".join(ahorcado))
                    print("el resultado es: "+"".join(resultado))
                    print("Ganastee")
                    partida = partida + 1
                    user = input("si quieres jugar otra escriba 'y':")
                    break
                    
        if vida == 0:
            print("Perdiste")
            user = input("quieres otra (escriba y para si):")
        
    if user == "y":
        repeat = True
        partida = partida + 1
    else:
        repeat = False
        break
