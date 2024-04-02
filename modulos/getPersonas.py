import requests
import os
import modulos.getAllData as data
from tabulate import tabulate
import json

def getPersonaID():
    os.system("clear")
    while True:
        id = input("   Ingrese ID a buscar: ")
        if id in str(data.ListID_Personas()):
            break
        else:
            print("Este ID de Persona no existe !")
    
    peticion = requests.get(f"http://154.38.171.54:5502/personas/{id}")
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