import modulos.getAllData as data
import requests
import json
import os

import re
patronFecha = re.compile("^\d{2}-\d{2}-\d{4}$")


# D A R _ D E _ B A J A
def Activo():
    idsA = data.ListID_Activos()
    idsP = data.ListID_Personas()
    
    while True:
        id = input("   Ingrese ID del Activo al que decea dar de baja: ")
        if id in idsA:
            break
        else:
            print("Error, este id de Activo no existe !")
            
    while True:
        fecha = input("   Ingrese la fecha en la que se realizo la accion (DD-MM-YYYY): ")
        if patronFecha.match(fecha):
            break
        else:
            print("Error, debe seguir el formato de fecha !")
    
    while True:
        person = input("   Ingrese id de la persona responsable: ")
        if person in idsP:
            break
        else:
            print("Error, este id de Persona no existe !")
    
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