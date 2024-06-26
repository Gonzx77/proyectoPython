import requests
import os
import modulos.getAllData as data
from tabulate import tabulate
import json


def getAsignacionID():
    os.system("clear")
    while True:
        while True:
            try:
                id = input("   Ingrese ID del activo al que desea listar las asignaciones: ")
                break
            except ValueError:
                print("Solo valores enteros !")
        if id in str(data.ListID_Activos()):
            break
        else:
            print("Este ID de activo no existe !")
            
    peticion = requests.get(f"http://154.38.171.54:5502/activos/{id}")
    info = peticion.json()
    x = info.get("asignaciones")
    
    tabla = []
    for asignacion in x:
        fila = [asignacion.get("NroAsignacion", ""), asignacion.get("FechaAsignacion", ""), asignacion.get("TipoAsignacion", ""), asignacion.get("AsignadoA", "")]
        tabla.append(fila)
        
    print(tabulate(tabla, headers=["NroAsignacion", "FechaAsignacion", "TipoAsignacion", "AsignadoA"], tablefmt="github"))
    
    input("   Presione ENTER para continuar...")