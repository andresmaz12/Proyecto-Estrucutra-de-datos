class nodoFlota():
    def __init__(self, placa, marca, modelo, anno, kilometraje):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.anno = anno
        self.kilometraje = kilometraje
        self.siguiente = None