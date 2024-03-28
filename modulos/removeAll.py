import modulos.getAllData as data
from tabulate import tabulate
import requests
import json
import os

import re
patronFecha = re.compile("^\d{2}-\d{2}-\d{4}$")


# D A R _ D E _ B A J A
def Activo():
    c = 0
    os.system("clear")
    idsA = data.ListID_Activos()
    idsP = data.ListID_Personas()
    
    while True:
        id = input("   Ingrese ID del Activo al que decea dar de baja: ")
        if id in idsA:
            activo = requests.get(f"http://154.38.171.54:5502/activos/{id}")
            activo = activo.json()
            estado = activo.get("idEstado")
            if estado != "2":
                break
            else:
                print("Este Activo ya esta dado de baja !")
                confirm = input("\n   Decea dar de baja otro Activo? (Si/No): ")
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
        
        fecha = input("   Ingrese la fecha en la que se realizo la accion (DD-MM-YYYY): ")
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
        
        activo = requests.get(f"http://154.38.171.54:5502/activos/{id}")
        activo = activo.json()
        activoH = activo.get("historialActivos")
        activo["idEstado"] = "1"
        
        activoH.append({
            "NroId": "1",
            "Fecha": fecha,
            "tipoMov": "2",
            "idRespMov": person
        })
        
        activo["idEstado"] = "2"
        peticion = requests.put(f"http://154.38.171.54:5502/activos/{id}", json=activo)
        res = peticion.json()
        
        print("Activo dado de baja correctamente \n")
        input("   Presione ENTER para continuar...")
        break
    
# E L I M I N A R
def Persona():
    os.system("clear")
    idsP = data.ListID_Personas()
    
    while True:
        id = input("   Ingrese ID de Persona a eliminar: ")
        if id in idsP:
            break
        else:
            print("Este ID de Persona no existe !")
    
    persona = requests.get(f"http://154.38.171.54:5502/personas/{id}")
    persona = persona.json()
    
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
        peticion = requests.delete(f"http://154.38.171.54:5502/personas/{id}")
        res = peticion.json()
        print("-Persona Eliminada")
    else:
        print("-Bien, operacion cancelada")
    input("   Presione ENTER para continuar...")