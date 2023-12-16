import math

ID = 1

class NodeTree:
    def __init__(self, id, padre, estado, valor, profundidad, coste, heuristica, accion):
        self.id = id
        self.padre = padre
        self.estado = estado
        self.valor = valor
        self.profundidad = profundidad
        self.coste = coste
        self.heuristica = heuristica
        self.accion =  accion
    
    def camino(nt):
        camino=[]
        camino.append(nt)
        nt = nt.padre
        while nt is not None:
            camino.append(nt)
            nt = nt.padre
        return reversed(camino)

    def expandirNodo(self,nt,sucesores,estrategia,g):
        nodosHijos = []
        global ID
        
        for sucesor in sucesores:
            id = ID
            padre = nt
            estado = sucesor.estado
            profundidad = nt.profundidad+1  
            coste = nt.coste + sucesor.coste
            accion = sucesor.accion
            heuristica = 0
            
            if (estrategia == "Profundidad"):
                valor = 1/(profundidad+1)
            elif (estrategia == "Anchura"):
                valor = profundidad 
            elif (estrategia == "Coste Uniforme"):
                valor = coste
            elif (estrategia == "Voraz"):
                heuristica = self.hArco(g,estado)  
                valor = heuristica
            elif (estrategia == "A-Arco"):
                heuristica = self.hArco(g,estado)    
                valor = coste + heuristica
            elif (estrategia == "A-Euclidea"):
                heuristica = self.hEuclidea(g,estado)
                valor = coste + heuristica
            
            nodoHijo = NodeTree(id, padre, estado, valor, profundidad, coste, heuristica, accion)
            nodosHijos.append(nodoHijo)
            ID=ID+1
              
        return  nodosHijos
    
    def hEuclidea(self,g,estado):
        res = []
        nodos = estado.nodosDestino.copy()
        nodos.append(estado.origen)
        
        while(len(nodos)!=0):
            nodo_actual = nodos.pop(0)
            x1 = (g.getNode(nodo_actual)).x
            y1 = (g.getNode(nodo_actual)).y
            for j in nodos:     
                x2 = (g.getNode(j)).x
                y2 = (g.getNode(j)).y
                op=math.sqrt(abs((((x1-x2)**2) + ((y1-y2)**2))))
                res.append(op)
        if(len(res)==0):
            return 0.00
        dist=min(res) * len(estado.nodosDestino)
            
        return dist
        

    def hArco(self,g,estado):
        k = len(estado.nodosDestino)
        min = g.minEdge
        res = k*min

        return res

    def __str__(self) -> str:
        return "[" + str(self.id) + "][" + str(round(self.coste,3)) + "," + "[("+str(self.estado.origen)+","+str(self.estado.nodosDestino)+")|"+self.estado.id[-6:] + "]," + str(self.accion) + "," + str(self.profundidad) + "," + str(round(self.heuristica,2)) + "," + str(round(self.valor,3)) + "]"
    
    def __lt__(self,other):
        if ((self.valor < other.valor) or ((self.valor == other.valor) and (self.id < other.id))):
            return True
        else:
            return False
        


    