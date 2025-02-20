from nodoVehiculos import nodoVehiculos

class linkedListMatenimiento():
    def __init__(self):
        self.cabeza = None
    
    def agregrarMantenimientos(self, placa, fecha, descripcion, cosot):
        nuevoNodo = nodoVehiculos(placa, fecha, descripcion, cosot)
        if not self.cabeza:
            self.cabeza = nuevoNodo
        else:
            actual = self.cabeza
            while actual.siguiente: 
                actual = actual.siguiente
            actual.siguiente = nuevoNodo

    def imprimir(self):
        actual = self.cabeza
        while actual: 
            print(actual._fecha, actual.descripcion, actual._costo)
            self.cabeza = actual.siguiente
            actual = None
            return