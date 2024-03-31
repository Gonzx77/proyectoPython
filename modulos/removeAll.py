import modulos.getAllData as data
from tabulate import tabulate
import requests
import json
import os

import re
patronFecha = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def Activo():
    c = 0
    os.system("clear")
    idsA = data.ListID_Activos()
    idsP = data.ListID_Personas()
    
    while True:
        id = input("   Ingrese ID del Activo al que desea eliminar: ")
        if id in idsA:
            activo = requests.get(f"http://localhost:5501/activos/{id}")
            activo = activo.json()
            estado = activo.get("idEstado")
            if estado == "2" or estado == "0":
                break
            else:
                print("Este Activo no se puede eliminar, su estado no lo permite !")
                confirm = input("\n   desea eliminar otro Activo? (Si/No): ")
                if confirm.lower() == "si" or confirm.lower() == "s":
                    print("Ok")
                else:
                    print("Ok")
                    c = 1
                    break
        else:
            print("Error, este id de Activo no existe !")
            
    while True:
        if c == 1:
            break
        
        fecha = input("   Ingrese la fecha en la que se realizo la accion (YYYY-MM-DD): ")
        if patronFecha.match(fecha):
            break
        else:
            print("Error, debe seguir el formato de fecha !")
    
    while True:
        if c == 1:
            break
        
        person = input("   Ingrese id de la persona responsable: ")
        if person in idsP:
            break
        else:
            print("Error, este id de Persona no existe !")
    
    while True:
        if c == 1:
            break
        
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
        
        os.system("clear")
        print(tabulate(result, headers=["Key", "Contenido"], tablefmt="github"))
        confirm = input("   Esta es la persona que desea eliminar? (Si/No): ")
        if confirm.lower() == "si" or confirm.lower() == "s":
            peticion = requests.delete(f"http://localhost:5501/activos/{id}")
            print("-Persona Eliminada")
        else:
            print("-Bien, operacion cancelada")
        input("   Presione ENTER para continuar...")
        break
    
def Persona():
    c = 0
    while True:
        if c == 1:
            break
        os.system("clear")
        idsP = data.ListID_Personas()
        
        while True:
            id = input("   Ingrese ID de Persona a eliminar: ")
            if id in idsP:
                break
            else:
                print("Este ID de Persona no existe !")
        
        persona = requests.get(f"http://localhost:5501/personas/{id}")
        persona = persona.json()
        
        activos = requests.get(f"http://localhost:5501/activos")
        activos = activos.json()
        
        for val in activos:
            asignaciones = val.get("asignaciones", [])
            for asignacion in asignaciones:
                if asignacion.get("AsignadoA") == id and asignacion.get("TipoAsignacion") == "Personal":
                    c = 1
        
        if c == 1:
            print("No se puede eliminar esta persona, ya que tiene activos asignados !")
            confirm = input("   desea eliminar otra persona? (Si/No): ")
            if confirm.lower() == "si" or confirm.lower() == "s":
                c = 0
            else:
                print("-Bien, operacion cancelada")
            input("   Presione ENTER para continuar...")
            
        else:
            break
    
    result = []
    for (key, value) in persona.items():
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
    confirm = input("   Esta es la persona que desea eliminar? (Si/No): ")
    if confirm.lower() == "si" or confirm.lower() == "s":
        peticion = requests.delete(f"http://localhost:5501/personas/{id}")
        print("-Persona Eliminada")
    else:
        print("-Bien, operacion cancelada")
    input("   Presione ENTER para continuar...")
    
def Zona():
    c = 0
    while True:
        if c == 1:
            break
        os.system("clear")
        idsP = data.ListID_Personas()
        
        while True:
            id = input("   Ingrese ID de Zona a eliminar: ")
            if id in idsP:
                break
            else:
                print("Este ID de Zona no existe !")
        
        zona = requests.get(f"http://localhost:5501/zonas/{id}")
        zona = zona.json()
        
        activos = requests.get(f"http://localhost:5501/activos")
        activos = activos.json()
        
        for val in activos:
            asignaciones = val.get("asignaciones", [])
            for asignacion in asignaciones:
                if asignacion.get("AsignadoA") == id and asignacion.get("TipoAsignacion") == "Zona":
                    c = 1
        
        if c == 1:
            print("No se puede eliminar esta zona, ya que tiene activos asignados !")
            confirm = input("   desea eliminar otra zona? (Si/No): ")
            if confirm.lower() == "si" or confirm.lower() == "s":
                c = 0
            else:
                print("-Bien, operacion cancelada")
            input("   Presione ENTER para continuar...")
            
        else:
            break
    
    result = []
    for (key, value) in zona.items():
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
    confirm = input("   Esta es la Zona que desea eliminar? (Si/No): ")
    if confirm.lower() == "si" or confirm.lower() == "s":
        peticion = requests.delete(f"http://localhost:5501/personas/{id}")
        print("-Zona Eliminada")
    else:
        print("-Bien, operacion cancelada")
    input("   Presione ENTER para continuar...")
    