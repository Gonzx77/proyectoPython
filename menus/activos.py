import os
import modulos.postAll as post

def menu():
    while True:
        os.system("clear")
        print(f"""
            
            ----------- MENU ACTIVOS -----------
            
                    1. AGREGAR
                    2. EDITAR
                    3. ELIMINAR
                    4. BUSCAR
                    
                    0. Regresar
            """)
        
        while True:
            op = input("   Ingrese opcion: ")
            if op == "1":
                post.Activo()
                break
            elif op == "2":
                #personal.menu()
                break
            elif op == "3":
                #zonas.menu()
                break
            elif op == "4":
                #asigActivos.menu()
                break
            elif op == "0":
                break
            else:
                print("Esta opcion no existe")
            
        break