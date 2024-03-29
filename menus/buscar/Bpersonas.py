import os
import modulos.getActivos as gActivos
import modulos.getPersonas as gPersonas

def menu():
    while True:
        os.system("clear")
        print(f"""
            
            ----------- MENU - BUSCAR PERSONAS -----------
            
                    1. Buscar Persona por ID
                    
                    0. Regresar
            """)
        
        while True:
            op = input("   Ingrese opcion: ")
            if op == "1":
                gPersonas.getPersonaID()
                break
            elif op == "0":
                break
            else:
                print("Esta opcion no existe")
            
        break