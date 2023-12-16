class Graph():
    def __init__(self):
        self.nodes = {}
        self.edges = {}
        self.adjacents = {}
        self.minEdge = None
           
    def addNode(self, node):
        if node.id not in self.nodes.keys():
            self.nodes[node.id] = node
   
    def addEdge(self, edge):           
        source = edge.source
        target = edge.target
        key = str(source)+"->"+str(target)
        
        if(key not in self.edges.keys()):
            self.edges[key]=edge
    
    def createAdjacents(self):   
        for node in self.nodes:
            aux = []
            for key in self.edges:
                edge=self.edges[key]
                if(edge.source == node):
                    aux.append(edge.target)
            self.adjacents[node]=aux
            
    def getEdge(self, source, target):
        key = str(source)+"->"+str(target)
        return self.edges.get(key)
    
    def getNode(self,id):   
        return self.nodes.get(id)
              
    def getAdjacents(self, node):
        return self.adjacents.get(node)
    