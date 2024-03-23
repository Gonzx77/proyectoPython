import os
import menus.activos as activos
import menus.personal as personal
import menus.zonas as zonas
import menus.asginacionActivos as asigActivos
import menus.reportes as reportes
import menus.movimientoActivos as movActivos


def menuInicial():
    while True:
        os.system("clear")
        print(f"""
            
            ----------- SISTEMA G&C DE INVENTARIO CAMPUSLANDS -----------

                    1. Activos
                    2. Personal
                    3. Zonas
                    4. Asignacion de Activos
                    5. Reportes
                    6. Movimientos de Activos
                    
                    0. Salir
            """)
        
        while True:
            op = input("Ingrese opcion: ")
            if op == "1":
                activos.menu()
                break
            elif op == "2":
                personal.menu()
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