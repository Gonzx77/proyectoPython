import requests
import json
import re
import os

from tabulate import tabulate
import modulos.getAllData as data

patronCodCampus = re.compile("^[A-Z]{3}\d{3}$")
patronFecha = re.compile("^\d{4}-\d{2}-\d{2}$")

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
            newActivo["Nombre"] = input("   Ingrese nombre del activo: ")
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
            print(tabulate(data.ListMarcas(), headers=["ID", "Marca"], tablefmt="github"))
            r = input("\n   Ingrese id marca del activo: ")
            if r in data.ListID_Marcas():
                newActivo["idMarca"] = r
                print("-Guardado")
                break
            else:
                print("Eerror, este ID de marca no existe !")
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            print(tabulate(data.ListCategorias(), headers=["ID", "Categoria"], tablefmt="github"))
            r = input("\n   Ingrese id categoria del activo: ")
            if r in data.ListID_Categorias():
                newActivo["idCategoria"] = r
                print("-Guardado")
                break
            else:
                print("Error, este ID de categoria no existe !")
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            print(tabulate(data.ListTipoActivos(), headers=["ID", "Tipo"], tablefmt="github"))
            r = input("\n   Ingrese id tipo del activo: ")
            if r in data.ListID_TipoActivos():
                newActivo["idTipo"] = r
                print("-Guardado")
                break
            else:
                print("Error, este ID de tipo no existe !")
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            newActivo["ValorUnitario"] = input("   Ingrese valor unitario del activo: ")
            print("-Guardado")
            break
        except ValueError:
            print("Error, caracteres invalidos !")
    
    
    newActivo["idEstado"] = "0"
    newActivo["historialActivos"] = []
    newActivo["asignaciones"] = []

    peticion = requests.post("http://154.38.171.54:5502/activos", data=json.dumps(newActivo))
    res = peticion.json()
    print("Persona guardada correctamente \n")
    input("   Presione ENTER para continuar...")

def Persona():
    os.system("clear")
    newPersona = {}
    
    print("NUEVO ACTIVO \n")
    
    while True:
        try:
            id = input("   Ingrese ID de la persona (4 caracteres): ")
            id = id.lower()
            if len(id) == 4:
                newPersona["id"] = str(id)
                print("-Guardado")
                break
            else:
                print("Error, debe incluir 4 caracteres !")
        except ValueError:
            print("Error, caracteres invalidos !")
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
    print("Persona guardada correctamente \n")
    input("   Presione ENTER para continuar...")
    
def Zona():
    os.system("clear")
    newZona = {}
    
    print("NUEVO ACTIVO \n")
    
    while True:
        try:
            newZona["nombreZona"] = input("   Ingrese Nombre de la Zona: ")
            print("-Guardado")
            break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            r = int(input("   Ingrese Capacidad de la Zona: "))
            newZona["totalCapacidad"] = str(r)
            print("-Guardado")
            break
        except ValueError:
            print("Error, solo se permiten numeros !")
    
    peticion = requests.post("http://154.38.171.54:5502/zonas", data=json.dumps(newZona))
    res = peticion.json()
    print("Zona guardada correctamente \n")
    input("   Presione ENTER para continuar...")
    

# M O V I M I E N T O S
def crearAsignacion():
    os.system("clear")
    
    opciones = ["1", "2"]
    c = 0
    
    while True:
        id = input("   Ingrese ID del Activo al que desea mover: ")
        if id in data.ListID_Activos():
            break
        else:
            print("Este ID de activo no existe !")
    while True:
        try:
            NroAsignacion = int(input("   Ingrese NroAsignacion: "))
            break
        except ValueError:
            print("Error, solo valores enteros !")
    while True:
        try:
            FechaAsignacion = input("   Ingrese FechaAsignacion (YYYY-MM-DD):")
            if patronFecha.match(FechaAsignacion):
                break
            else:
                print("Error, debe seguir el formato !")
        except ValueError:
            print("Error, caracteres invalidos !")
        
        
    print(f"""
        1. Personal
        2. Zona
        """)
    
    while True:
        if c == 1:
            break
        try:
            a = input("\n   Seleccione tipo de asignacion: ")
            if a in opciones:
                if a == "1":
                    while True:
                        b = input("   Ingrese ID a la persona que decea asignar el Activo: ")
                        if b in data.ListID_Activos():
                            TipoAsignacion = "Personal"
                            AsignadoA = b
                            c = 1
                            break
                        else:
                            print("Este ID de Activo no existe !")
                elif a == "2":
                    while True:
                        b = input("   Ingrese ID a la Zona que decea asignar el Activo: ")
                        if b in data.ListID_Zonas():
                            TipoAsignacion = "Zona"
                            AsignadoA = b
                            c = 1
                            break
                        else:
                            print("Este ID de Zona no existe !")
            else:
                print("Esta opcion no esta en la lista de opciones !")
        except ValueError:
            print("Error, caracteres invalidos !")
            
            
            
    activo = requests.get(f"http://154.38.171.54:5502/activos/{id}")
    activo = activo.json()
    activoAsig = activo.get("asignaciones")
    
    activoAsig.append({
        "NroAsignacion": NroAsignacion,
        "FechaAsignacion": FechaAsignacion,
        "TipoAsignacion": TipoAsignacion,
        "AsignadoA": AsignadoA
    })
    
    peticion = requests.put(f"http://154.38.171.54:5502/activos/{id}", json=activo)
    res = peticion.json()
    
    print("Asignacion Terminada \n")
    input("   Presione ENTER para continuar...")