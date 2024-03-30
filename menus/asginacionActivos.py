import os
import modulos.postAll as post
import modulos.getAsignacion as gAsignacion

def menu():
    while True:
        os.system("clear")
        print(f"""
            
            ----------- MENU - ASIGNACION ACTIVOS -----------
                    
                    1. CREAR ASIGNACION
                    2. BUSCAR ASIGNACION

                    0. Regresar
            """)
        
        while True:
            op = input("Ingrese opcion: ")
            if op == "1":
                print(post.crearAsignacion())
                break
            elif op == "2":
                print(gAsignacion.getAsignacionID())
                break
            elif op == "0":
                break
            else:
                print("Esta opcion no existe")
            
        break