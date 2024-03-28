import os
import modulos.getActivos as gActivos

def menu():
    while True:
        os.system("clear")
        print(f"""
            
            ----------- MENU - BUSCAR ACTIVOS -----------
            
                    1. Buscar Activo por ID
                    2. Buscaar Activo por Categoria
                    3. Buscar Activo por NroSerial
                    
                    0. Regresar
            """)
        
        while True:
            op = input("   Ingrese opcion: ")
            if op == "1":
                gActivos.getActivoID()
                break
            elif op == "2":
                gActivos.getActivoCategoria()
                break
            elif op == "3":
                gActivos.getActivoNroSerial()
                break
            elif op == "0":
                break
            else:
                print("Esta opcion no existe")
            
        break