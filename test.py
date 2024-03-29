import requests

activos = requests.get(f"http://154.38.171.54:5502/activos")
activos = activos.json()

result = []
for val in activos:
    asignaciones = val.get("asignaciones", [])
    for asignacion in asignaciones:
        if asignacion.get("AsignadoA") == "Skylab":
            result.append(val.get("Nombre"))
            
print(result)