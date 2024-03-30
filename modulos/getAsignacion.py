import requests
import os
import modulos.getAllData as data
from tabulate import tabulate
import json


def getAsignacionID():
    os.system("clear")
    while True:
        id = input("   Ingrese ID del activo al que desea listar las asignaciones: ")
        if id in data.ListID_Activos():
            break
        else:
            print("Este ID de activo no existe !")
            
    peticion = requests.get(f"http://154.38.171.54:5502/activos/{id}")
    info = peticion.json()
    
    x = [info.get("asignaciones")]
    
    print(tabulate(x, headers=["NroAsignacion", "FechaAsignacion", "TipoAsignacion", "AsignadoA"], tablefmt="github"))
    
    input("   Presione ENTER para continuar...")