import os
import modulos.getZonas as gZonas

def menu():
    while True:
        os.system("clear")
        print(f"""
            
            ----------- MENU - BUSCAR ZONAS -----------
            
                    1. Buscar Zona por ID
                    2. Buscaar Zona por Capacidad Minima
                    
                    0. Regresar
            """)
        
        while True:
            op = input("   Ingrese opcion: ")
            if op == "1":
                gZonas.getZonaID()
                break
            elif op == "2":
                gZonas.getZonasCapacidadMin()
                break
            elif op == "0":
                break
            else:
                print("Esta opcion no existe")
            
        break