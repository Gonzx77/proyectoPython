import requests
import os
import modulos.getAllData as data
from tabulate import tabulate
import json


def getActivoID():
    os.system("clear")
    while True:
        id = input("   Ingrese ID a buscar: ")
        if id in data.ListID_Activos():
            break
        else:
            print("Este ID de Activo no existe !")
    
    peticion = requests.get(f"http://localhost:5501/activos/{id}")
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
    
    
def getActivoCategoria():
    os.system("clear")
    print(tabulate(data.ListCategorias(), headers=["ID", "Nombre"], tablefmt="github"))
    while True:
        categoria = input("   Ingrese Categoria a buscar: ")
        if categoria in data.ListID_Categorias():
            break
        else:
            print("Esta Categoria de Activo no existe !")
    
    peticion = requests.get(f"http://localhost:5501/activos")
    info = peticion.json()
    
    result = []
    for val in info:
        if val.get("idCategoria") == categoria:
            result.append([
                val.get("NroItem"),
                val.get("NroSerial"),
                val.get("Nombre"),
                val.get("idEstado"),
                val.get("idCategoria")
            ])
    
    os.system("clear")
    print(tabulate(result, headers=["Nro Item", "Nro Serial", "Nombre", "ID Estado", "ID Categoria"], tablefmt="github"))
    input("\n   Presione ENTER para continuar...")
    
    
def getActivoNroSerial():
    os.system("clear")
    while True:
        NroSerial = input("   Ingrese NroSerial a buscar: ")
        if NroSerial in data.ListActivoNroSerial():
            break
        else:
            print("Este NroSerial de Activo no existe !")
            
    peticion = requests.get(f"http://localhost:5501/activos")
    info = peticion.json()
    
    result = []
    for val in info:
        if val.get("NroSerial") == NroSerial:
            result.append([
                val.get("NroItem"),
                val.get("NroSerial"),
                val.get("Nombre"),
                val.get("idEstado"),
                val.get("idCategoria")
            ])
    
    os.system("clear")
    print(tabulate(result, headers=["Nro Item", "Nro Serial", "Nombre", "ID Estado", "ID Categoria"], tablefmt="github"))
    input("\n   Presione ENTER para continuar...")