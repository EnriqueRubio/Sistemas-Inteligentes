class Edge:
    def __init__(self, id, source, target, osmid, length):
        self.id = id
        self.source = source
        self.target = target
        self.osmid = osmid
        self.length = length

    def __str__(self) -> str:
        return "ID: " + str(self.id) + ", SOURCE: " + str(self.source) + ", TARGET: " + str(self.target) + ", OSMID: " + str(self.osmid) + ", LENGTH: " + str(self.length)