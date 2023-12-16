#! usr/bin/python
import xml.sax
from Estado import Estado
from NodeTree import NodeTree
from Problema import Problema
from GraphHandler import GraphHandler
from queue import PriorityQueue

def algoritmoBusqueda(problema,estrategia,profundidad_max):
    
    solucion = False
    frontera = PriorityQueue()
    visitados = {}

    id = 0
    padre = None
    estadoInicial = problema.estadoInicial
    valor = 0.00
    profundidad = 0
    coste = 0.00
    heuristica = 0
    accion = None
    nt = NodeTree(id, padre, estadoInicial, valor, profundidad, coste, heuristica,accion)
    frontera.put(nt)
    
    while((not frontera.empty()) and (not solucion)):
        
        nt = frontera.get()
        
        if(problema.objetivo(nt.estado.nodosDestino)):   
            solucion = True
        elif ((nt.estado.id not in visitados.keys()) and (nt.profundidad < profundidad_max)):
            
            visitados[nt.estado.id]= nt.estado.id
            sucesores = Estado.getSucesor(g,nt.estado.origen,nt.estado.nodosDestino)
            nodosArbol= nt.expandirNodo(nt,sucesores,estrategia,g)
            
            for n in nodosArbol:
                frontera.put(n)

    camino = []            
    if (solucion):
        camino = NodeTree.camino(nt)
        return camino
    else:
        print("NO HAY CAMINO")
        return camino
    

if (__name__ == "__main__"):

    #(71,[2, 112, 287, 561, 660] -> examen
    #Creacion del problema
    nodoOrigen = 1221
    destinos =[249, 441, 528]
    profundidad_max = 600
    fichero = 'CR_Capital.graphXML'
    problema = Problema(fichero,Estado(nodoOrigen,destinos))
    estrategia = "Anchura" # "Anchura" "Profundidad" "Coste Uniforme" "A-Euclidea" "A-Arco" "Voraz"

    #Creacion del Grafo
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    Handler = GraphHandler()
    parser.setContentHandler(Handler)
    parser.parse(problema.fichero)
    g = Handler.graph
    g.createAdjacents()
    
    camino = algoritmoBusqueda(problema,estrategia,profundidad_max)
    
    #Imprimimos camino
    for i in camino:
        print(str(i))
    
        