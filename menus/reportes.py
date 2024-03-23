import os

def menu():
    while True:
        os.system("clear")
        print(f"""
            
            ----------- MENU REPORTES -----------

                    1. LISTAR TODOS LOS ACTIVOS
                    2. LISTAR ACTIVOS POR CATEGORIA
                    3. LISTAR ACTIVOS DADOS DE BAJA POR DAÑO
                    4. LISTAR ACTIVOS Y ASIGNACION
                    5. LISTAR HISTORIAL DE MOV. DE ACTIVO
                    
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
            elif op == "3":
                #zonas.menu()
                break
            elif op == "4":
                #asigActivos.menu()
                break
            elif op == "5":
                #reportes.menu()
                break
            elif op == "0":
                break
            else:
                print("Esta opcion no existe")
            
        break