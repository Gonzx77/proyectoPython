import requests
import json
import re
import os

patronCodCampus = re.compile(r"^[A-Z]{3}\d{3}$")

def Activo():
    os.system("clear")
    newActivo = {}
    
    print("NUEVO ACTIVO \n")
    
    while True:
        try:
            newActivo["NroItem"] = int(input("   Ingrese numero de item del activo: "))
            print("-Guardado")
            break
        except ValueError:
            print("Error, solo valores enteros !")
    while True:
        try:
            newActivo["CodTransaccion"] = int(input("   Ingrese codigo de transaccion del activo: "))
            print("-Guardado")
            break
        except ValueError:
            print("Error, solo valores enteros !")
    while True:
        try:
            newActivo["NroSerial"] = input("   Ingrese numero serial del activo: ")
            print("-Guardado")
            break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            r = input("   Ingrese codigo campus del activo (AAA000): ")
            r = r.upper()
            if patronCodCampus.match(r):
                newActivo["CodCampus"] = r
                print("-Guardado")
                break
            else:
                print("Error, debe seguir el formato !")
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            newActivo["NroFormulario"] = int(input("   Ingrese numero formulario del activo: "))
            print("-Guardado")
            break
        except ValueError:
            print("Error, solo valores enteros !")
    while True:
        try:
            newActivo["Nombre"] = input("   Ingrese numero formulario del activo: ")
            print("-Guardado")
            break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            newActivo["Proveedor"] = input("   Ingrese proveedor del activo: ")
            print("-Guardado")
            break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            newActivo["EmpresaResponsable"] = input("   Ingrese empresa responsable del activo: ")
            print("-Guardado")
            break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            newActivo["idMarca"] = input("   Ingrese id marca del activo: ")
            print("-Guardado")
            break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            newActivo["idCategoria"] = input("   Ingrese id categoria del activo: ")
            print("-Guardado")
            break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            newActivo["idTipo"] = input("   Ingrese id tipo del activo: ")
            print("-Guardado")
            break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            newActivo["ValorUnitario"] = input("   Ingrese valor unitario del activo: ")
            print("-Guardado")
            break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            newActivo["idEstado"] = input("   Ingrese id estado del activo: ")
            print("-Guardado")
            break
        except ValueError:
            print("Error, caracteres invalidos !")

    peticion = requests.post("http://154.38.171.54:5502/activos", data=json.dumps(newActivo))
    res = peticion.json()
    res["Mensaje"] = "Pago Guardado"
    return [res]