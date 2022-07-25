import configuracion
import palabras
import funciones

#FEDERICO
def config():
    pass

def juego():
    cond = True
    bonus = True
    entrada = ""
    confNivel = 0
    palabraRespuesta = []
    nivel = funciones.verificarNivel()
    palabraAleatoria = funciones.obtenerPalabraRandom(nivel,palabras.list)
        
    for i in range(palabraAleatoria.getLongitud()):
        palabraRespuesta.append("*")
        
    confNivel = funciones.obtenerConfNivel(nivel)
    intentos = confNivel.getIntentos()
    puntos = confNivel.getPuntos()
    puntosBonus = confNivel.getBonus()
    
    while(intentos > 0):
        cond = True
        print("Intentos: ", intentos)
        print("Puntos: ", puntos+puntosBonus)
        print(*palabraRespuesta)
        entrada = input("Ingrese una letra o la palabra: ").lower()
        
        if (entrada == palabraAleatoria.getPalabra()) and bonus == True:
            print("acertaste a la primera!!")
            intentos=0
        else:
            puntosBonus = 0
            bonus = False
            for sal,busq in enumerate(palabraAleatoria.getPalabra()):
                if(busq == entrada):
                    palabraRespuesta[sal] = entrada
                    cond = False
            
        if("".join(map(str,palabraRespuesta)) == palabraAleatoria.getPalabra()):
            print("Adivinaste la palabra!!!",palabraAleatoria.getPalabra())
            #posible solucion a DESACTIVAR PALABRA SI SE ADIVINA
            #palabraAleatoria.setActivo(False)
            intentos = 0
                
        #SOLUCION DE ERROR DE INTENTOS (MERA BOBADA)
        if(cond !=False):
            intentos = intentos - 1

#FUNCIONES CONFIGURACION:
#   1.CAMBIAR PUNTOS
#   1.CAMBIAR BONUS
#   1.CAMBIAR INTENTOS
#   1.AGREGAR, QUITAR Y EDITAR PALABRAS


#FUNCIONES JUEGO:
#   2.ESCOGER UNA PALABRA RANDOM DEPENDE DE LA DIFICULTAD
#   3.PINTAR PALABRA Y SUS PISTAS
#   4.SI ACERTO LA PALABRA DESACTIVARLA
#   5.SELECCIONAR LA COMPLEJIDAD
#   6.RESTAR INTENTOS