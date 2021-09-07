import random

player = True
partida = 0
usuario = 0
maquina = 0
while True:

    element = ["piedra","papel","tijera"]
    maq = random.choice(element)
    eleccion = input("selecciona tu elemento (tijera, piedra y papel): ").lower()
   
    if eleccion=="tijera" or eleccion=="papel" or eleccion=="piedra":
        print(f"usuario saca {eleccion.upper()} y maquina saca {maq.upper()}")
        if maq == eleccion :
            print("empate")

        elif maq=="tijera" and eleccion=="piedra":
            print("gana usuario")
            usuario = usuario + 1
        
        elif maq=="tijera" and eleccion=="papel":
            print("gana maquina")
            maquina = maquina + 1

        elif maq=="papel" and eleccion=="piedra":
            print("gana maquina")
            maquina = maquina + 1

        elif maq=="papel" and eleccion=="tijera":
            print("gana usuario")
            usuario = usuario + 1

        elif maq=="piedra" and eleccion=="tijera":
            print("gana maquina")
            maquina = maquina + 1

        elif maq=="piedra" and eleccion=="papel":
            print("gana usuario")
            usuario = usuario + 1
    else:
        print("no valido")
    
    print(f"marcado: maquina {maquina} - {usuario} usuario")

    if maquina==3 or usuario==3:
        if usuario==3:
            print("ganaste")
            break
        else:
            print("perdiste")
            break