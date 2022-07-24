from menus import menuConfig, menuJuego

def main():
    cond = True
    opc = 1
    
    while(opc != 0):
        print("Menú Principal")
        print("¿Qué desea hacer?\n\t1.Opciones del juego\n\t2.Jugar\n\t3.Salir")
        while(cond == True):
            try:
                opc = int(input("Opcion: "))
                cond = False
            except ValueError:
                print("Ingrese el número que acompaña a la opción")
        cond = True
        if(opc == 1):
            menuConfig()
        elif(opc == 2):
            menuJuego()
        elif(opc == 3):
            print("Adiós")
            opc = 0
        else:
            print("Ingrese una opción valida por favor")
    
if __name__ == "__main__":
    main()
