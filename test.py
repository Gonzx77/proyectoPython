import requests
import json
import re
import os

from tabulate import tabulate
import modulos.getAllData as data

patronCodCampus = re.compile(r"^[A-Z]{3}\d{3}$")
patronFecha = re.compile(r"^\d{4}-\d{2}-\d{2}$")

def crearAsignacion():
    os.system("clear")
    
    tipos = [{"1", "Personal"}, {"2", "Zona"}]
    opciones = ["1", "2"]
    c = 0
    
    while True:
        id = input("   Ingrese ID del Activo al que desea mover: ")
        if id in data.ListID_Activos():
            break
        else:
            print("Este ID de activo no existe !")
    while True:
        try:
            NroAsignacion = int(input("   Ingrese NroAsignacion: "))
            break
        except ValueError:
            print("Error, solo valores enteros !")
    while True:
        try:
            FechaAsignacion = input(" Ingrese FechaAsignacion (YYYY-MM-DD):")
            if patronFecha.match(FechaAsignacion):
                break
            else:
                print("Error, debe seguir el formato !")
        except ValueError:
            print("Error, caracteres invalidos !")
        
        
    print(tabulate(tipos, headers=["Opciones", "Tipo"], tablefmt="github"))
    
    while True:
        if c == 1:
            break
        try:
            a = input("\n   Seleccione tipo de asignacion: ")
            if a in opciones:
                if a == "1":
                    while True:
                        b = input("   Ingrese ID a la persona que decea asignar el Activo: ")
                        if b in data.ListID_Activos():
                            TipoAsignacion = "Personal"
                            AsignadoA = b
                            c = 1
                            break
                        else:
                            print("Este ID de Activo no existe !")
                elif a == "2":
                    while True:
                        b = input("   Ingrese ID a la Zona que decea asignar el Activo: ")
                        if b in data.ListID_Zonas():
                            TipoAsignacion = "Zona"
                            AsignadoA = b
                            c = 1
                            break
                        else:
                            print("Este ID de Zona no existe !")
            else:
                print("Esta opcion no esta en la lista de opciones !")
        except ValueError:
            print("Error, caracteres invalidos !")
            
            
            
    activo = requests.get(f"http://154.38.171.54:5502/activos/{id}")
    activo = activo.json()
    activoAsig = activo.get("asignaciones")
    
    activoAsig.append({
        "NroAsignacion": NroAsignacion,
        "FechaAsignacion": FechaAsignacion,
        "TipoAsignacion": TipoAsignacion,
        "AsignadoA": AsignadoA
    })