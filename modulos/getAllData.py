import requests

# D A T A 
def Activos():
    peticion = requests.get("http://154.38.171.54:5501/activos")
    data = peticion.json()
    return data
def Marcas():
    peticion = requests.get("http://154.38.171.54:5501/marcas")
    data = peticion.json()
    return data
def CategoriaActivos():
    peticion = requests.get("http://154.38.171.54:5501/categoriaActivos")
    data = peticion.json()
    return data
def TipoMovActivos():
    peticion = requests.get("http://154.38.171.54:5501/tipoMovActivos")
    data = peticion.json()
    return data
def Estados():
    peticion = requests.get("http://154.38.171.54:5501/estados")
    data = peticion.json()
    return data
def TipoActivos():
    peticion = requests.get("http://154.38.171.54:5501/tipoActivos")
    data = peticion.json()
    return data
def Personas():
    peticion = requests.get("http://154.38.171.54:5501/personas")
    data = peticion.json()
    return data
def Zonas():
    peticion = requests.get("http://154.38.171.54:5501/zonas")
    data = peticion.json()
    return data


# T E L E F O N O S
def TelefonosPersonas():
    peticion = requests.get("http://154.38.171.54:5501/personas")
    peticion = peticion.json()
    telefonos = []
    for val in peticion:
        telefonos_persona = val.get("Telefonos", [])
        telefonos.extend(telefonos_persona)
    return telefonos


# L I S T A S
def ListaMarcas():
    peticion = requests.get("http://154.38.171.54:5501/marcas")
    peticion = peticion.json()
    data = []
    for val in peticion:
        data.append(val.get("id"))
    return data


# U L T I M O _ I D
def UID_Activos():
    peticion = requests.get("http://154.38.171.54:5501/activos")
    data = peticion.json()
    for val in data:
        result = val.get("id")
    return result
def UID_Personas():
    peticion = requests.get("http://154.38.171.54:5501/personas")
    data = peticion.json()
    for val in data:
        result = val.get("id")
    return result
def UID_Zoas():
    peticion = requests.get("http://154.38.171.54:5501/zonas")
    data = peticion.json()
    for val in data:
        result = val.get("id")
    return result