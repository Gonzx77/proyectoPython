import os
import modulos.postAll as post
import modulos.editAll as edit
import modulos.removeAll as remove
import menus.buscar.Bzonas as buscarZonas

def menu():
    while True:
        os.system("clear")
        print(f"""
            
            ----------- MENU - ZONAS -----------

                    1. AGREGAR
                    2. EDITAR
                    3. ELIMINAR
                    4. BUSCAR
                    
                    0. Regresar
            """)
        
        while True:
            op = input("Ingrese opcion: ")
            if op == "1":
                print(post.Zona())
                break
            elif op == "2":
                print(edit.Zona())
                break
            elif op == "3":
                print(remove.Zona())
                break
            elif op == "4":
                buscarZonas.menu()
                break
            elif op == "0":
                break
            else:
                print("Esta opcion no existe")
            
        break