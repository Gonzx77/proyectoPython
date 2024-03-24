import os
import menus.activos as activos
import menus.personas as personas
import menus.zonas as zonas
import menus.asginacionActivos as asigActivos
import menus.reportes as reportes
import menus.movimientoActivos as movActivos


def menuInicial():
    while True:
        os.system("clear")
        print(f"""
            
            ----------- SISTEMA G&C DE INVENTARIO CAMPUSLANDS -----------

                    1. ACTIVOS
                    2. PERSONAL
                    3. ZONAS
                    4. ASIGNACION DE ACTIVOS
                    5. REPORTES
                    6. MOVIMIENTO DE ACTIVOS
                    
                    0. Salir
            """)
        
        while True:
            op = input("   Ingrese opcion: ")
            if op == "1":
                activos.menu()
                break
            elif op == "2":
                personas.menu()
                break
            elif op == "3":
                zonas.menu()
                break
            elif op == "4":
                asigActivos.menu()
                break
            elif op == "5":
                reportes.menu()
                break
            elif op == "6":
                movActivos.menu()
                break
            elif op == "0":
                exit()
            else:
                print("Esta opcion no existe")
            
        
menuInicial()