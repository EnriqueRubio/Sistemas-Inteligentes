class Problema:
    def __init__(self, fichero, estadoInicial):
        self.fichero = fichero
        self.estadoInicial = estadoInicial

    def objetivo(self,nodeList):
        if len(nodeList) == 0:
            return True
    
    def __str__(self) -> str:
        return "FICHERO: " + self.fichero + ", ESTADO: " + self.estado + ", ¿FIN? " + self.fin