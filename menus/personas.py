import os
import modulos.postAll as post
import modulos.editAll as edit
import modulos.removeAll as remove

def menu():
    while True:
        os.system("clear")
        print(f"""
            
            ----------- MENU - PERSONAS -----------

                    1. AGREGAR
                    2. EDITAR
                    3. ELIMINAR
                    4. BUSCAR
                    
                    0. Regresar
            """)
        
        while True:
            op = input("Ingrese opcion: ")
            if op == "1":
                print(post.Persona())
                break
            elif op == "2":
                print(edit.Persona())
                break
            elif op == "3":
                print(remove.Persona())
                break
            elif op == "4":
                #asigActivos.menu()
                break
            elif op == "0":
                break
            else:
                print("Esta opcion no existe")
            
        break