import requests
import os
import modulos.getAllData as data
from tabulate import tabulate
import json

def getAllActivos():
    os.system("clear")
    info = data.Activos()
    result = []
    
    for val in info:
        result.append([
            val.get("id"),
            val.get("NroItem"),
            val.get("NroSerial"),
            val.get("CodCampus"),
            val.get("Nombre"),
            val.get("Proveedor"),
            val.get("EmpresaResponsable"),
            val.get("idMarca"),
            val.get("idCategoria"),
            val.get("idTipo"),
            val.get("ValorUnitario"),
            val.get("idEstado")
        ])
    
    print(tabulate(result, headers=["ID", "NroItem", "NroSerial", "CodCampus", "Nombre", "Proveedor", "EmpresaResponsable", "idMarca", "idCategoria", "idTipo", "ValorUnitario", "idEstado"]))
    
    input("Presione ENTER para continuar...")
    
    
def getActivosCategoria():
    os.system("clear")
    print(tabulate(data.ListCategorias(), headers=["ID", "Nombre"], tablefmt="github"))
    while True:
        categoria = input("   Ingrese Categoria a buscar: ")
        if categoria in data.ListID_Categorias():
            break
        else:
            print("Esta Categoria de Activo no existe !")
    
    peticion = requests.get(f"http://154.38.171.54:5502/activos")
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
    
def getActivosBajaAño():
    os.system("clear")
    año = input("   Ingrese Año con el que desea realizar la busqueda: ")
    
    activos = data.Activos()
    
    result = []
    for val in activos:
        x = val.get("idEstado")
        if x == "2":
            historial = [val.get("historialActivos")]
            ultimoMov = historial[-1]
            for val2 in ultimoMov:
                fecha = val2.get("Fecha")
                if fecha.startswith(año):
                    result.append([
                        val.get("id"),
                        val.get("NroItem"),
                        val.get("NroSerial"),
                        val.get("Nombre"),
                        fecha
                    ])
    if result:
        print(tabulate(result, headers=["ID", "NroItem", "NroSerial", "Nombre", "Fecha en la que se dio de baja"], tablefmt="github"))
    else:
        print("No se dio de baja ningun activo durante este año !")

    input("   Presione ENTER para continuar...")