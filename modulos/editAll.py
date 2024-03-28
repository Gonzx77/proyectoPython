import requests
import json
import re
import os

from tabulate import tabulate
import modulos.getAllData as data

def Activo():
    while True:
        id = input("   Ingrese ID del activo a editar: ")
        if id in data.ListID_Activos():
            break
        else:
            print("Error, este ID de activo no existe !")
        
        
    activo = requests.get(f"http://154.38.171.54:5502/activos/{id}")
    activo = activo.json()
    result = []
    for (key, value) in activo.items():
        if isinstance(value, dict):
            value_str = json.dumps(value)
        else:
            value_str = str(value)
        result.append([
            key,
            value_str
        ])
    
    print(tabulate(result, headers=["Key", "Contenido"], tablefmt="github"))
    print("EDITANDO ACTIVO (deje en blanco para mantener) \n")
    
    while True:
        try:
            r = input("   Ingrese nuevo NroItem: ").strip()
            if r:
                r = int(r)
                activo["NroItem"] = str(r)
                print("-Modificado")
                break
            else:
                print("-Conservado")
                break
        except ValueError:
            print("Error, solo valores enteros !")
    while True:
        try:
            r = input("   Ingrese nuevo CodTransaccion: ").strip()
            if r:
                r = int(r)
                activo["CodTransaccion"] = str(r)
                print("-Modificado")
                break
            else:
                print("-Conservado")
                break
        except ValueError:
            print("Error, solo valores enteros !")
    while True:
        try:
            r = input("   Ingrese nuevo NroSerial: ").strip()
            if r:
                activo["NroSerial"] = r
                print("-Modificado")
                break
            else:
                print("-Conservado")
                break
        except ValueError:
            print("Error, solo valores enteros !")
    while True:
        try:
            r = input("   Ingrese nuevo CodCampus: ").strip()
            if r:
                activo["CodCampus"] = r
                print("-Modificado")
                break
            else:
                print("-Conservado")
                break
        except ValueError:
            print("Error, solo valores enteros !")

    #peticion = requests.put(f"http://154.38.171.54:5006/pagos/{id}", json=activo)
    #res = peticion.json()
    print("Activo modificado correctamente")
    input("   Presione ENTER para continuar...")