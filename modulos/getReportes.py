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
    
    os.system("clear")
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
        os.system("clear")
        print(tabulate(result, headers=["ID", "NroItem", "NroSerial", "Nombre", "Fecha en la que se dio de baja"], tablefmt="github"))
    else:
        print("No se dio de baja ningun activo durante este año !")

    input("   Presione ENTER para continuar...")
    
def getActivosAsig():
    
    activos = data.Activos()
    personas = data.Personas()
    zonas = data.Zonas()
    
    result = []
    
    for val in activos:
        asigacion = [val.get("asignaciones")]
        ultimaAsig = asigacion[-1]
        for val2 in ultimaAsig:
            tipo = val2.get("TipoAsignacion")
            id = val2.get("AsignadoA")
            
            result.append([
                val.get("id"),
                val.get("NroItem"),
                val.get("Nombre"),
                val.get("NroSerial"),
                tipo,
                id,
            ])
        
    os.system("clear")
    print(tabulate(result, headers=["ID", "NroItem", "Nombre", "NroSerial", "Tipo Asignacion", "ID Asignacion", "ASignacion"]))
    input("   Presione ENTER para continuar...")
    
def getHistorialActivo():
    os.system("clear")
    while True:
        try:
            id = int(input("   Ingrese ID del activo al que desea buscar su historial: "))
            if id in data.ListID_Activos():
                break
            else:
                print("Este ID de Activo no existe !")
        except ValueError:
            print("Solo valores enteros !")
            
    activo = requests.get(f"http://localhost:5501/activos/{id}")
    activo = activo.json()
    activoH = activo.get("historialActivos")
    
    result = []
    for item in activoH:
        result.extend([[key, value] for key, value in item.items()])
    
    print(tabulate(result, headers=["NroId", "Fecha", "ID Tipo Movimiento", "ID Responsable"], tablefmt="github"))
    input("   Presione ENTER para continuar...")