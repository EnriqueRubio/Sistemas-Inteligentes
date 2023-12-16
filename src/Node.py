class Node:
    def __init__(self, id, osmid_original, lon, lat,x,y):
        self.id = id
        self.osmid_original = osmid_original
        self.lon = lon
        self.lat = lat
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return "ID: " + str(self.id) + ", OSMID: " + str(self.osmid_original) + ", LON: " + str(self.lon) + ", LAT: " + str(self.lat)