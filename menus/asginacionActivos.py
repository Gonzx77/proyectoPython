import os

def menu():
    while True:
        os.system("clear")
        print(f"""
            
            ----------- MENU ASIGNACION ACTIVOS -----------
                    
                    1. CREAR ASIGNACION
                    2. BUSCAR ASIGNACION

                    0. Regresar
            """)
        
        while True:
            op = input("Ingrese opcion: ")
            if op == "1":
                #activos.menu()
                break
            elif op == "2":
                #personal.menu()
                break
            elif op == "0":
                break
            else:
                print("Esta opcion no existe")
            
        break