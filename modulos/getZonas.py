import requests
import os
import modulos.getAllData as data
from tabulate import tabulate
import json


def getZonaID():
    os.system("clear")
    while True:
        id = input("   Ingrese ID a buscar: ")
        if id in data.ListID_Zonas():
            break
        else:
            print("Este ID de Zona no existe !")
    
    peticion = requests.get(f"http://154.38.171.54:5502/zonas/{id}")
    info = peticion.json()
    
    result = []
    for (key, value) in info.items():
        if isinstance(value, dict):
            value_str = json.dumps(value)
        else:
            value_str = str(value)
        result.append([
            key,
            value_str
        ])
    
    os.system("clear")
    print(tabulate(result, headers=["Key", "Contenido"], tablefmt="github"))
    input("\n   Presione ENTER para continuar...")
    
def getZonasCapacidadMin():
    os.system("clear")
    while True:
        try:
            capacidad = int(input("   Ingrese Capacidad Minima a filtrar: "))
            break
        except ValueError:
            print("Error, solo valores enteros !")
    
    peticion = requests.get(f"http://154.38.171.54:5502/zonas")
    info = peticion.json()
    
    result = []
    for zona in info:
        if int(zona.get("totalCapacidad")) >= capacidad:
            result.append([
                zona["id"],
                zona["nombreZona"],
                zona["totalCapacidad"]
            ])
    
    os.system("clear")
    print(tabulate(result, headers=["ID", "Nombre", "Capacidad"], tablefmt="github"))
    input("\nPresione ENTER para continuar...")