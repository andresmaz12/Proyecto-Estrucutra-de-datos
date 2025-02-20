from nodoFlota import nodoFlota

class linkedListFlota():
    def __init__(self):
        self.cabeza = None
        self.tamanio = 0
    
    def esta_vacia(self):
        return self.cabeza is None
    
    def agregarAuto(self, placa, marca, modelo, anno, kilometraje):
        nuevo_nodo = nodoFlota(placa, marca, modelo, anno, kilometraje)
        
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            nuevo_nodo.siguiente = self.cabeza  
            self.tamanio += 1
            print(f"Auto con placa {placa} agregado exitosamente!")
            return
        
        if self.buscar_placa(placa):
            print(f"Error: Ya existe un auto con la placa {placa}")
            return
        
        actual = self.cabeza
        while actual.siguiente != self.cabeza:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo
        nuevo_nodo.siguiente = self.cabeza
        self.tamanio += 1
        print(f"Auto con placa {placa} agregado exitosamente!")
    
    def buscar_placa(self, placa):
        if self.esta_vacia():
            return False
        
        actual = self.cabeza
        while True:
            if actual.placa == placa:
                return True
            actual = actual.siguiente
            if actual == self.cabeza:
                break
        return False
    
    def eliminarAuto(self, placa):
        if self.esta_vacia():
            print("La lista está vacía.")
            return
        
        if self.cabeza.siguiente == self.cabeza:
            if self.cabeza.placa == placa:
                self.cabeza = None
                self.tamanio = 0
                print(f"Auto con placa {placa} eliminado exitosamente!")
                return
            else:
                print(f"No se encontró un auto con la placa {placa}")
                return
        
        actual = self.cabeza
        anterior = None
        encontrado = False
        
        while True:
            if actual.placa == placa:
                encontrado = True
                break
            anterior = actual
            actual = actual.siguiente
            if actual == self.cabeza:
                break
        
        if not encontrado:
            print(f"No se encontró un auto con la placa {placa}")
            return
        
        if actual == self.cabeza:
            anterior = self.cabeza
            while anterior.siguiente != self.cabeza:
                anterior = anterior.siguiente
            self.cabeza = self.cabeza.siguiente
            anterior.siguiente = self.cabeza
        else:
            anterior.siguiente = actual.siguiente
        
        self.tamanio -= 1
        print(f"Auto con placa {placa} eliminado exitosamente!")
    
    def busquedaAuto(self, placa):
        if self.esta_vacia():
            print("La lista está vacía.")
            return
        
        actual = self.cabeza
        encontrado = False
        
        while True:
            if actual.placa == placa:
                print("\nAuto encontrado:")
                print(f"Placa: {actual.placa}")
                print(f"Marca: {actual.marca}")
                print(f"Modelo: {actual.modelo}")
                print(f"Año: {actual.anno}")
                print(f"Kilometraje: {actual.kilometraje}")
                encontrado = True
                break
            actual = actual.siguiente
            if actual == self.cabeza:
                break
        
        if not encontrado:
            print(f"No se encontró un auto con la placa {placa}")
    
    def listarAutos(self):
        if self.esta_vacia():
            print("La lista está vacía.")
            return
        
        print("\nListado de autos:")
        actual = self.cabeza
        while True:
            print(f"\nPlaca: {actual.placa}")
            print(f"Marca: {actual.marca}")
            print(f"Modelo: {actual.modelo}")
            print(f"Año: {actual.anno}")
            print(f"Kilometraje: {actual.kilometraje}")
            actual = actual.siguiente
            if actual == self.cabeza:
                break
        print(f"\nTotal de autos: {self.tamanio}")