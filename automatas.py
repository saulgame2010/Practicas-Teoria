class estado:
    def __init__(self, lis, nombre):
        self.lis = lis
        self.nombre = nombre


class automata:
    def __init__(self, estados):
        self.nomEstado = estados[0].nombre
        self.lisEstados = estados
        self.estado=estados[0]
    def transicion(self, numero):
        estadoActual = None
        for x in range(0,len(self.lisEstados)):
            if self.lisEstados[x].nombre == self.nomEstado:
                estadoActual = self.lisEstados[x]
                break
        if estadoActual != None:
            
            for camino in estadoActual.lis:
                if camino[0]==numero:
                    self.nomEstado=camino[1]
                    print(self.nomEstado,end="-->")