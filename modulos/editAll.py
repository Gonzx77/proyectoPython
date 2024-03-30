import requests
import json
import re
import os

from tabulate import tabulate
import modulos.getAllData as data

patronCodCampus = re.compile(r"^[A-Z]{3}\d{3}$")

def Activo():
    while True:
        id = input("   Ingrese ID del Activo a editar: ")
        if id in data.ListID_Activos():
            break
        else:
            print("Error, este ID de Activo no existe !")
        
        
    activo = requests.get(f"http://154.38.171.54:5502/activos/{id}")
    activo = activo.json()
    
    def tabla():
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
        return result
    
    print("EDITANDO ACTIVO (deje en blanco para mantener) \n")
    input("   Presione ENTER para continuar...")
    
    while True:
        os.system("clear")
        print(tabulate(tabla(), headers=["Key", "Contenido"], tablefmt="github"))
        try:
            r = input("   Ingrese nuevo NroItem: ").strip()
            if r:
                r = int(r)
                activo["NroItem"] = str(r)
                print("-Modificado")
                input("   Presione ENTER para continuar...")
                break
            else:
                print("-Conservado")
                input("   Presione ENTER para continuar...")
                break
        except ValueError:
            print("Error, solo valores enteros !")
    while True:
        os.system("clear")
        print(tabulate(tabla(), headers=["Key", "Contenido"], tablefmt="github"))
        try:
            r = input("   Ingrese nuevo CodTransaccion: ").strip()
            if r:
                r = int(r)
                activo["CodTransaccion"] = str(r)
                print("-Modificado")
                input("   Presione ENTER para continuar...")
                break
            else:
                print("-Conservado")
                input("   Presione ENTER para continuar...")
                break
        except ValueError:
            print("Error, solo valores enteros !")
        input("   Presione ENTER para continuar...")
    while True:
        os.system("clear")
        print(tabulate(tabla(), headers=["Key", "Contenido"], tablefmt="github"))
        try:
            r = input("   Ingrese nuevo NroSerial: ").strip()
            if r:
                activo["NroSerial"] = r
                print("-Modificado")
                input("   Presione ENTER para continuar...")
                break
            else:
                print("-Conservado")
                input("   Presione ENTER para continuar...")
                break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        os.system("clear")
        print(tabulate(tabla(), headers=["Key", "Contenido"], tablefmt="github"))
        try:
            r = input("   Ingrese nuevo CodCampus (AAA000): ").strip()
            if r:
                if patronCodCampus.match(r):
                    activo["CodCampus"] = r
                    print("-Modificado")
                    input("   Presione ENTER para continuar...")
                    break
                else:
                    print("Error, debe seguir el formato !")
            else:
                print("-Conservado")
                input("   Presione ENTER para continuar...")
                break
        except ValueError:
            print("Error, solo valores enteros !")
    while True:
        os.system("clear")
        print(tabulate(tabla(), headers=["Key", "Contenido"], tablefmt="github"))
        try:
            r = input("   Ingrese nuevo NroFormulario: ").strip()
            if r:
                r = int(r)
                activo["NroFormulario"] = str(r)
                print("-Modificado")
                input("   Presione ENTER para continuar...")
                break
            else:
                print("-Conservado")
                input("   Presione ENTER para continuar...")
                break
        except ValueError:
            print("Error, solo valores enteros !")
    while True:
        os.system("clear")
        print(tabulate(tabla(), headers=["Key", "Contenido"], tablefmt="github"))
        try:
            r = input("   Ingrese nuevo Nombre: ").strip()
            if r:
                activo["Nombre"] = r
                print("-Modificado")
                input("   Presione ENTER para continuar...")
                break
            else:
                print("-Conservado")
                input("   Presione ENTER para continuar...")
                break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        os.system("clear")
        print(tabulate(tabla(), headers=["Key", "Contenido"], tablefmt="github"))
        try:
            r = input("   Ingrese nuevo Proveedor: ").strip()
            if r:
                activo["Proveedor"] = r
                print("-Modificado")
                input("   Presione ENTER para continuar...")
                break
            else:
                print("-Conservado")
                input("   Presione ENTER para continuar...")
                break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        os.system("clear")
        print(tabulate(tabla(), headers=["Key", "Contenido"], tablefmt="github"))
        try:
            r = input("   Ingrese nuevo EmpresaResponsable: ").strip()
            if r:
                activo["EmpresaResponsable"] = r
                print("-Modificado")
                input("   Presione ENTER para continuar...")
                break
            else:
                print("-Conservado")
                input("   Presione ENTER para continuar...")
                break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        os.system("clear")
        try:
            print(tabulate(data.ListMarcas(), headers=["ID", "Marca"], tablefmt="github"))
            r = input("   Ingrese nuevo idMarca: ").strip()
            if r:
                if r in data.ListID_Marcas():
                    activo["idMarca"] = r
                    print("-Modificado")
                    input("   Presione ENTER para continuar...")
                    break
                else:
                    print("Este ID de marca no existe !")
            else:
                print("-Conservado")
                input("   Presione ENTER para continuar...")
                break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        os.system("clear")
        try:
            print(tabulate(data.ListCategorias(), headers=["ID", "Categoria"], tablefmt="github"))
            r = input("\n   Ingrese nuevo idCategoria: ").strip()
            if r:
                if r in data.ListID_Categorias():
                    activo["idCategoria"] = r
                    print("-Modificado")
                    input("   Presione ENTER para continuar...")
                    break
                else:
                    print("Este ID de categoria no existe !")
            else:
                print("-Conservado")
                input("   Presione ENTER para continuar...")
                break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        os.system("clear")
        try:
            print(tabulate(data.ListTipoActivos(), headers=["ID", "Tipo"], tablefmt="github"))
            r = input("\n   Ingrese nuevo idTipo: ").strip()
            if r:
                if r in data.ListID_TipoActivos():
                    activo["idTipo"] = r
                    print("-Modificado")
                    input("   Presione ENTER para continuar...")
                    break
                else:
                    print("Este ID de tipo de existe !")
            else:
                print("-Conservado")
                input("   Presione ENTER para continuar...")
                break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        os.system("clear")
        print(tabulate(tabla(), headers=["Key", "Contenido"], tablefmt="github"))
        try:
            r = input("   Ingrese nuevo ValorUnitario: ").strip()
            if r:
                r = int(r)
                activo["ValorUnitario"] = str(r)
                print("-Modificado")
                input("   Presione ENTER para continuar...")
                break
            else:
                print("-Conservado")
                input("   Presione ENTER para continuar...")
                break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        
        try:
            print(tabulate(data.ListEstados(), headers=["ID", "Estado"], tablefmt="github"))
            r = input("\n   Ingrese nuevo idEstado: ").strip()
            if r:
                if r in data.ListID_Estados():
                    activo["idEstado"] = r
                    print("-Modificado")
                    input("   Presione ENTER para continuar...")
                    break
                else:
                    print("Este ID de categoria no existe !")
            else:
                print("-Conservado")
                input("   Presione ENTER para continuar...")
                break
        except ValueError:
            print("Error, caracteres invalidos !")




    peticion = requests.put(f"http://154.38.171.54:5502/activos/{id}", json=activo)
    res = peticion.json()
    print("Activo modificado correctamente")
    input("\n   Presione ENTER para continuar...")
    
def Persona():
    while True:
        id = input("   Ingrese ID de Persona a editar: ")
        if id in data.ListID_Personas():
            break
        else:
            print("Error, este ID de Persona no existe !")
        
        
    persona = requests.get(f"http://154.38.171.54:5502/personas/{id}")
    persona = persona.json()
    
    def tabla():
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
        return result
    
    print("EDITANDO PERSONA (deje en blanco para mantener) \n")
    input("   Presione ENTER para continuar...")
    
    while True:
        os.system("clear")
        print(tabulate(tabla(), headers=["Key", "Contenido"], tablefmt="github"))
        try:
            r = input("   Ingrese nuevo nroId (CC, Nit): ").strip()
            if r:
                r = int(r)
                persona["nroId (CC, Nit)"] = str(r)
                print("-Modificado")
                input("   Presione ENTER para continuar...")
                break
            else:
                print("-Conservado")
                input("   Presione ENTER para continuar...")
                break
        except ValueError:
            print("Error, solo valores enteros !")
    while True:
        os.system("clear")
        print(tabulate(tabla(), headers=["Key", "Contenido"], tablefmt="github"))
        try:
            r = input("   Ingrese nuevo Nombre: ").strip()
            if r:
                persona["Nombre"] = r
                print("-Modificado")
                input("   Presione ENTER para continuar...")
                break
            else:
                print("-Conservado")
                input("   Presione ENTER para continuar...")
                break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        os.system("clear")
        print(tabulate(tabla(), headers=["Key", "Contenido"], tablefmt="github"))
        try:
            r = input("   Ingrese nuevo Email (example@example.com): ").strip()
            if r:
                if "@" in r and r.endswith(".com"):
                    persona["Email"] = r
                    print("-Modificado")
                    input("   Presione ENTER para continuar...")
                    break
                else:
                    print("Error, debe seguir el formato !")
            else:
                print("-Conservado")
                input("   Presione ENTER para continuar...")
                break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        os.system("clear")
        try:
            n1 = input("   Ingrese nuevo numero de telefono del movil de la persona: ").strip()
            if n1:
                n1 = int(n1)
                print("-Modificado")
                input("   Presione ENTER para continuar...")
                break
            else:
                print("Este valor no puede estar vacio !")
        except ValueError:
            print("Error, solo se permiten numeros !")
    while True:
        os.system("clear")
        try:
            n2 = input("   Ingrese nuevo numero de telefono de la casa de la persona: ").strip()
            if n2:
                n2 = int(n2)
                print("-Guardado")
                input("   Presione ENTER para continuar...")
                break
            else:
                print("Este valor no puede estar vacio !")
        except ValueError:
            print("Error, solo se permiten numeros !")
        
    persona["Telefonos"] = [
        {
            "movil": {
            "id": id,
            "num": str(n1)
            },
            "casa": {
            "id": id,
            "num": str(n2)
            }
        }
    ]



    peticion = requests.put(f"http://154.38.171.54:5502/personas/{id}", json=persona)
    res = peticion.json()
    print("Persona modificada correctamente")
    input("\n   Presione ENTER para continuar...")
    
def Zona():
    while True:
        id = input("   Ingrese ID de la Zona a editar: ")
        if id in data.ListID_Zonas():
            break
        else:
            print("Error, este ID de Zona no existe !")
        
        
    persona = requests.get(f"http://154.38.171.54:5502/zonas/{id}")
    zona = persona.json()
    
    def tabla():
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
        return result
    
    print("EDITANDO ZONA (deje en blanco para mantener) \n")
    input("   Presione ENTER para continuar...")
    
    while True:
        os.system("clear")
        print(tabulate(tabla(), headers=["Key", "Contenido"], tablefmt="github"))
        try:
            r = input("   Ingrese nuevo nombreZona: ").strip()
            if r:
                zona["nombreZona"] = r
                print("-Modificado")
                input("   Presione ENTER para continuar...")
                break
            else:
                print("-Conservado")
                input("   Presione ENTER para continuar...")
                break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        os.system("clear")
        print(tabulate(tabla(), headers=["Key", "Contenido"], tablefmt="github"))
        try:
            r = input("   Ingrese nueva Capacidad Total: ").strip()
            if r:
                r = int(r)
                zona["totalCapacidad"] = r
                print("-Modificado")
                input("   Presione ENTER para continuar...")
                break
            else:
                print("-Conservado")
                input("   Presione ENTER para continuar...")
                break
        except ValueError:
            print("Error, solo valores enteros !")



    peticion = requests.put(f"http://154.38.171.54:5502/zonas/{id}", json=zona)
    res = peticion.json()
    print("Zona modificada correctamente")
    input("\n   Presione ENTER para continuar...")