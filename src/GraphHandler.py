import xml.sax
from Node import Node
from Edge import Edge
from Graph import Graph

class GraphHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.type = None
        self.id = None
        self.key = None
        self.source = None
        self.target = None
        self.osmid_original = None
        self.lon = None
        self.lat = None
        self.osmid = None
        self.length = None
        self.x = None
        self.y = None
        self.node = None
        self.edge = None 
        self.graph = Graph()

    def startElement(self, tag, attributes):
        self.type = tag

        if tag == 'node': 
            self.type = tag
            self.id = int(attributes['id'])

        if tag == 'edge': 
            self.type = tag
            self.id = int(attributes['id'])
            self.target = int(attributes['target'])
            self.source = int(attributes['source'])

        if tag =='data':
            self.key = attributes['key'] 
        
    def characters(self, content):
        if content!= "\n" and content!="  " and content!='\t':
            if self.key == 'd4':
                self.osmid_original = content
                
            elif self.key == 'd8':       
                self.lon =float(content)
                
            elif self.key == 'd9':  
                self.lat = float(content)
                
            elif self.key == 'd12':
                self.osmid = content

            elif self.key == 'd17':
                self.length = float(content)

            elif self.key == 'd6':
                self.x = float(content)

            elif self.key == 'd5':
                self.y = float(content)
                
    def endElement(self, tag):
        if(tag == 'node'):
            self.node = Node(self.id, self.osmid_original, self.lon, self.lat,self.x,self.y)
            self.graph.addNode(self.node)
            
        if(tag == 'edge'):
            self.edge = Edge(self.id, self.source, self.target, self.osmid, self.length)
            self.graph.addEdge(self.edge)
            if self.graph.minEdge == None:
                self.graph.minEdge = self.edge.length
            elif self.edge.length < self.graph.minEdge:
                self.graph.minEdge = self.edge.length
           
            
        

    