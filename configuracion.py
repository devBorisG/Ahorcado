class Configuracion:
    def __init__(self,puntos,bonus,intentos):
        self.__puntos = puntos
        self.__bonus = bonus
        self.__intentos = intentos
        
    #Getters
    def getPuntos(self):
        return self.__puntos
    
    def getBonus(self):
        return self.__bonus
    
    def getIntentos(self):
        return self.__intentos
    
    #Setters
    def setPuntos(self,puntos):
        self.__puntos = puntos
        
    def setBonus(self,bonus):
        self.__bonus = bonus
        
    def setIntentos(self,intentos):
        self.__bonus = intentos
