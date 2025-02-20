import os
import sys
from linkedListFlota import linkedListFlota
from claseVehciulo import Vehiculo

flota_vehiculos = linkedListFlota()

def limpiarConsola():
    from os import system
    system("cls")
    
def agregarAuto():
    placa = input("Ingrese el número de placa: ")
    marca = input("Ingrese la marca de su carro: ")
    modelo = input("Ingrese el modelo de su carro: ")
    anno = int(input("Ingrese el año de su vehiculo (no menor a 1970): "))
    kilometraje = int(input("Ingrese el kilometraje de su carro: "))
    flota_vehiculos.agregarAuto(placa, marca, modelo, anno, kilometraje)

def eliminarAuto():
    placa = input("Ingrese la placa del auto que desea eliminar: ")
    flota_vehiculos.eliminarAuto(placa)
    
def listarAuto():
    print("Se imprimiran todos los autos disponibles en caso de haber")
    flota_vehiculos.listarAutos()
    
def busquedaAuto():
    placa = input("Ingrese la placa del auto que desea buscar: ")
    flota_vehiculos.busquedaAuto(placa)

def menu(opcion):
    if(opcion == "1"):
        limpiarConsola()
        agregarAuto()
    elif(opcion == "2"):
        limpiarConsola()
        eliminarAuto()
    elif(opcion == "3"):
        limpiarConsola()
        busquedaAuto()
    elif(opcion == "4"):
        limpiarConsola()
        listarAuto()
    elif(opcion == "5"):
        limpiarConsola()
        placa = input("Ingrese la placa de su vehiculo: ")
        Vehiculo.agregarMantenimiento(placa)
    elif(opcion == "6"):
        limpiarConsola()
        print("Gracias por usar el sistema!")
        return True
    else:
        print("Ingrese una opcion valida")
        return False

def main():
    while True:
        print("\nBienvenido")
        print("1.) Agregar vehiculos")
        print("2.) Eliminar vehiculo")
        print("3.) Buscar vehiculos por placa y mostrar informacion")
        print("4.) Listar todos los vehiculos")
        print("5.) Agregar mantenimientos")
        print("6.) Salir")
        opcion = input("Que desea hacer: ")
        if menu(opcion):
            break

if __name__ == '__main__':
    main()