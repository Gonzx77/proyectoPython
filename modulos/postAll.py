import requests
import json
import re
import os

import modulos.getAllData as data

patronCodCampus = re.compile(r"^[A-Z]{3}\d{3}$")

def Activo():
    os.system("clear")
    newPersona = {}
    
    print("NUEVO ACTIVO \n")
    
    while True:
        try:
            newPersona["NroItem"] = int(input("   Ingrese numero de item del activo: "))
            print("-Guardado")
            break
        except ValueError:
            print("Error, solo valores enteros !")
    while True:
        try:
            newPersona["CodTransaccion"] = int(input("   Ingrese codigo de transaccion del activo: "))
            print("-Guardado")
            break
        except ValueError:
            print("Error, solo valores enteros !")
    while True:
        try:
            newPersona["NroSerial"] = input("   Ingrese numero serial del activo: ")
            print("-Guardado")
            break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            r = input("   Ingrese codigo campus del activo (AAA000): ")
            r = r.upper()
            if patronCodCampus.match(r):
                newPersona["CodCampus"] = r
                print("-Guardado")
                break
            else:
                print("Error, debe seguir el formato !")
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            newPersona["NroFormulario"] = int(input("   Ingrese numero formulario del activo: "))
            print("-Guardado")
            break
        except ValueError:
            print("Error, solo valores enteros !")
    while True:
        try:
            newPersona["Nombre"] = input("   Ingrese nombre del activo: ")
            print("-Guardado")
            break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            newPersona["Proveedor"] = input("   Ingrese proveedor del activo: ")
            print("-Guardado")
            break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            newPersona["EmpresaResponsable"] = input("   Ingrese empresa responsable del activo: ")
            print("-Guardado")
            break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            newPersona["idMarca"] = input("   Ingrese id marca del activo: ")
            print("-Guardado")
            break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            newPersona["idCategoria"] = input("   Ingrese id categoria del activo: ")
            print("-Guardado")
            break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            newPersona["idTipo"] = input("   Ingrese id tipo del activo: ")
            print("-Guardado")
            break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            newPersona["ValorUnitario"] = input("   Ingrese valor unitario del activo: ")
            print("-Guardado")
            break
        except ValueError:
            print("Error, caracteres invalidos !")
    
    
    newPersona["idEstado"] = "0"
    newPersona["historialActivos"] = []
    newPersona["asignaciones"] = []

    peticion = requests.post("http://154.38.171.54:5502/activos", data=json.dumps(newPersona))
    res = peticion.json()
    res["Mensaje"] = "Activo Guardado"
    return [res]



def Personas():
    os.system("clear")
    newPersona = {}
    
    print("NUEVO ACTIVO \n")
    
    while True:
        try:
            r = int(input("   Ingrese identificacion de la persona: "))
            newPersona["nroId (CC, Nit)"] = str(r)
            print("-Guardado")
            break
        except ValueError:
            print("Error, solo se permiten numeros !")
    while True:
        try:
            newPersona["Nombre"] = input("   Ingrese nombre de la persona: ")
            print("-Guardado")
            break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            r = input("   Ingrese email de la persona (example@example.com): ")
            if "@" in r and r.endswith(".com"):
                newPersona["Email"] = r
                print("-Guardado")
                break
            else:
                print("Error, debe seguir el formato")
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            n1 = int(input("   Ingrese numero de telefono del movil de la persona: "))
            n1 = str(n1)
            print("-Guardado")
            break
        except ValueError:
            print("Error, solo se permiten numeros !")
    while True:
        try:
            n2 = int(input("   Ingrese numero de telefono de la casa de la persona: "))
            n2 = str(n2)
            print("-Guardado")
            break
        except ValueError:
            print("Error, solo se permiten numeros !")
        
    newPersona["Telefonos"] = [
        {
            "movil": {
            "id": id,
            "num": n1
            },
            "casa": {
            "id": id,
            "num": n2
            }
        }
    ]
    
    peticion = requests.post("http://154.38.171.54:5502/personas", data=json.dumps(newPersona))
    res = peticion.json()
    res["Mensaje"] = "Persona Guardada"
    return [res]