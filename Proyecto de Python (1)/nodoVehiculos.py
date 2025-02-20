from datetime import datetime

class nodoVehiculos:
    def __init__(self,placa, fechaMantenimiento, descripcionMantenimiento, costoMantenimiento):
        self._fecha = fechaMantenimiento
        self.descripcion = descripcionMantenimiento
        self._costo = costoMantenimiento
        self.siguiente = None

        @property
        def fechaMantenimiento(self):
            return self._fecha
        
        @fechaMantenimiento.setter
        def fechaMantenimiento(self, nuevaFecha):
            if  datetime.strptime(nuevaFecha, "%d/%m/%Y"):
                self._fecha = nuevaFecha
            else:
                raise ValueError("La fecha debe mantener cierto formato DD/MM/AA o no es una fecha valida")

        @property
        def costoMantenimiento(self):
            return self._costo

        @costoMantenimiento.setter
        def costoMantenimiento(self, nuevoCosto):
            if (nuevoCosto >= 0):
                self._costo = nuevoCosto
            else: 
                raise ValueError("El costo de un mantenimiento no uede ser menor a Q 0.00")