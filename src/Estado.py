import hashlib
from Sucesor import Sucesor

class Estado:

    def __init__(self,origen, nodosDest):
        self.id = self.calcularId(origen,nodosDest)
        self.origen = origen
        self.nodosDestino = nodosDest

    def calcularId(self,origen, nodeList):
        cadenastr = str(nodeList).replace("'","")
        cadenastr = str(cadenastr).replace(" ","")
        cadena = "(" + str(origen) + "," + cadenastr + ")"
        id = hashlib.md5(cadena.encode())
        subcadena = id.hexdigest()
        return subcadena
    
    def getSucesor(g, origen, nodosDestino):
        sucesores = []
        ady = g.getAdjacents(origen)
        
        if (ady is not None):
            ady.sort()
            for nodo in ady:
                    nodosDestinocp = nodosDestino.copy()
                    if(nodo in nodosDestinocp):
                        nodosDestinocp.remove(nodo)
                        coste = g.getEdge(origen,nodo).length
                        estado = Estado(nodo,nodosDestinocp)     
                        accion = str(origen)+"->"+str(nodo)
                    else:
                        coste = g.getEdge(origen,nodo).length
                        estado =Estado(nodo,nodosDestinocp)
                        accion = str(origen)+"->"+str(nodo)
                            
                    sucesor = Sucesor(estado,accion,coste)
                    sucesores.append(sucesor)
                
        return sucesores
           
        