import os
import modulos.postAll as post

def menu():
    while True:
        os.system("clear")
        print(f"""
            
            ----------- MENU - MOVIMIENTO DE ACTIVOS -----------
                    
                    1. RETORNO DE ACTIVO
                    2. DAR DE BAJA ACTIVO
                    3. CAMBIAR ASIGNACION DE ACTIVO
                    4. ENVIAR A GARANTIA ACTIVO
                    
                    0. Regresar
            """)
        
        while True:
            op = input("Ingrese opcion: ")
            if op == "1":
                post.retornoActivo()
                break
            elif op == "2":
                post.darBajaActivo()
                break
            elif op == "3":
                post.reasignarActivo()
                break
            elif op == "4":
                post.garantiaActivo()
                break
            elif op == "0":
                break
            else:
                print("Esta opcion no existe")
            
        break