import modulos.getAllData as data

info = data.Activos()
for val in info:
    result = val.get("id")