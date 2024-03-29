import requests
import os
import modulos.getAllData as data
from tabulate import tabulate
import json


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
    
getZonasCapacidadMin()