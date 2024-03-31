# S A V E
c = 0
os.system("clear")
idsA = data.ListID_Activos()
idsP = data.ListID_Personas()

while True:
    id = input("   Ingrese ID del Activo al que desea dar de baja: ")
    if id in idsA:
        activo = requests.get(f"http://localhost:5501/activos/{id}")
        activo = activo.json()
        estado = activo.get("idEstado")
        if estado != "2":
            break
        else:
            print("Este Activo ya esta dado de baja !")
            confirm = input("\n   desea dar de baja otro Activo? (Si/No): ")
            if confirm.lower() == "si" or confirm.lower() == "s":
                print("Ok")
            else:
                print("Ok")
                c = 1
                break
    else:
        print("Error, este id de Activo no existe !")
        
while True:
    if c == 1:
        break
    
    fecha = input("   Ingrese la fecha en la que se realizo la accion (YYYY-MM-DD): ")
    if patronFecha.match(fecha):
        break
    else:
        print("Error, debe seguir el formato de fecha !")

while True:
    if c == 1:
        break
    
    person = input("   Ingrese id de la persona responsable: ")
    if person in idsP:
        break
    else:
        print("Error, este id de Persona no existe !")

while True:
    if c == 1:
        break
    
    activo = requests.get(f"http://localhost:5501/activos/{id}")
    activo = activo.json()
    activoH = activo.get("historialActivos")
    activo["idEstado"] = "1"
    
    activoH.append({
        "NroId": "1",
        "Fecha": fecha,
        "tipoMov": "2",
        "idRespMov": person
    })
    
    activo["idEstado"] = "2"
    peticion = requests.put(f"http://localhost:5501/activos/{id}", json=activo)
    
    print("Activo dado de baja correctamente \n")
    input("   Presione ENTER para continuar...")
    break