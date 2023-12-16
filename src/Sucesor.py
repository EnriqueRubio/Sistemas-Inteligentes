class Sucesor:
    def __init__(self,estado,accion,coste):
        self.estado= estado
        self.accion = accion
        self.coste = coste

    def __lt__(self,other):
        if self.estado.origen < other.estado.origen:
            return   True
        else:
            return False
         
    def __str__(self) -> str:
        return "Estado:"+str(self.estado.id)+" Accion:"+str(self.accion)+" Coste:"+str(self.coste) 

