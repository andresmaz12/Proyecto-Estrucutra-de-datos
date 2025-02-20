import re
from datetime import datetime
from listaMantenimiento import linkedListMatenimiento
from linkedListFlota import linkedListFlota
mantenimiento = linkedListMatenimiento()
flota_vehiculos = linkedListFlota()
anno_actual = datetime.now().year

class Vehiculo:
    def __init__(self, placa, marca, modelo, anno, kilometraje):
        self._placa = placa
        self.marca = marca
        self.modelo = modelo
        self._anno = anno
        self._kilometraje = kilometraje

    @property
    def placa(self):
        return self._placa

    @placa.setter
    def placa(self, nuevo_placa):
        formato = r"^\d{3}[A-Z]{3}$"
        if re.match(formato, nuevo_placa):
            self._placa = nuevo_placa
        else:
            raise ValueError("La placa debe seguir el formato 123ABC")

    @property
    def anno(self):
        return self._anno

    @anno.setter
    def anno(self, nuevo_anno):
        if 1970 < nuevo_anno <= anno_actual:  
            self._anno = nuevo_anno
        else:
            raise ValueError("El año del vehículo debe ser mayor a 1970 y menor o igual al actual")

    @property
    def kilometraje(self):
        return self._kilometraje

    @kilometraje.setter
    def kilometraje(self, nuevo_kilometraje):
        if nuevo_kilometraje >= 0:
            self._kilometraje = nuevo_kilometraje
        else:
            raise ValueError("El kilometraje debe ser positivo")

    @staticmethod
    def agregarFlota(placa, marca, modelo, anno, kilometraje):
        flota_vehiculos.agregarAuto(placa, marca, modelo, anno, kilometraje)

    @staticmethod
    def agregarMantenimiento(placa):
        from main import flota_vehiculos  
        actual = flota_vehiculos.cabeza
        vehiculo_existe = False
        if actual:
            while True:
                if actual.placa == placa:
                    vehiculo_existe = True
                    break
                actual = actual.siguiente
                if actual == flota_vehiculos.cabeza:
                    break
        
        if not vehiculo_existe:
            print(f"No existe un vehículo con la placa {placa}")
            return
            
        mantenimiento = linkedListMatenimiento()
        mantenimiento.agregrarMantenimientos(placa)
        
    @staticmethod
    def listarMantenimientos(placa):
        linkedListMatenimiento.imprimir(placa)
