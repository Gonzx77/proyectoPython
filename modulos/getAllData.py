import requests

# D A T A 
def Activos():
    peticion = requests.get("http://154.38.171.54:5502/activos")
    data = peticion.json()
    return data
def Marcas():
    peticion = requests.get("http://154.38.171.54:5502/marcas")
    data = peticion.json()
    return data
def CategoriaActivos():
    peticion = requests.get("http://154.38.171.54:5502/categoriaActivos")
    data = peticion.json()
    return data
def TipoMovActivos():
    peticion = requests.get("http://154.38.171.54:5502/tipoMovActivos")
    data = peticion.json()
    return data
def Estados():
    peticion = requests.get("http://154.38.171.54:5502/estados")
    data = peticion.json()
    return data
def TipoActivos():
    peticion = requests.get("http://154.38.171.54:5502/tipoActivos")
    data = peticion.json()
    return data
def Personas():
    peticion = requests.get("http://154.38.171.54:5502/personas")
    data = peticion.json()
    return data
def Zonas():
    peticion = requests.get("http://154.38.171.54:5502/zonas")
    data = peticion.json()
    return data


# T E L E F O N O S
def TelefonosPersonas():
    peticion = requests.get("http://154.38.171.54:5502/personas")
    peticion = peticion.json()
    telefonos = []
    for val in peticion:
        telefonos_persona = val.get("Telefonos", [])
        telefonos.extend(telefonos_persona)
    return telefonos


# L I S T A S
def ListMarcas():
    peticion = requests.get("http://154.38.171.54:5502/marcas")
    data = peticion.json()
    
    result = []
    for val in data:
        result.append([
            val.get("id"),
            val.get("Nombre")
        ])
    return result
def ListCategorias():
    peticion = requests.get("http://154.38.171.54:5502/categoriaActivos")
    data = peticion.json()
    
    result = []
    for val in data:
        result.append([
            val.get("id"),
            val.get("Nombre")
        ])
    return result
def ListTipoActivos():
    peticion = requests.get("http://154.38.171.54:5502/categoriaActivos")
    data = peticion.json()
    
    result = []
    for val in data:
        result.append([
            val.get("id"),
            val.get("Nombre")
        ])
    return result
def ListEstados():
    peticion = requests.get("http://154.38.171.54:5502/estados")
    data = peticion.json()
    
    result = []
    for val in data:
        result.append([
            val.get("id"),
            val.get("Nombre")
        ])
    return result
def ListActivoNroSerial():
    peticion = requests.get("http://154.38.171.54:5502/activos")
    data = peticion.json()
    
    result = []
    for val in data:
        result.append(
            val.get("NroSerial")
        )
    return result
def ListPersonasNombres():
    peticion = requests.get("http://154.38.171.54:5502/personas")
    data = peticion.json()
    
    result = []
    for val in data:
        result.append(
            val.get("Nombre")
        )
    return result


# L I S T A S _ I D
def ListID_Activos():
    peticion = requests.get("http://154.38.171.54:5502/activos")
    data = peticion.json()
    result = []
    for val in data:
        result.append(val.get("id"))
    return result
def ListID_Personas():
    peticion = requests.get("http://154.38.171.54:5502/personas")
    data = peticion.json()
    result = []
    for val in data:
        result.append(val.get("id"))
    return result
def ListID_Zonas():
    peticion = requests.get("http://154.38.171.54:5502/zonas")
    data = peticion.json()
    result = []
    for val in data:
        result.append(val.get("id"))
    return result
def ListID_Marcas():
    peticion = requests.get("http://154.38.171.54:5502/marcas")
    data = peticion.json()
    result = []
    for val in data:
        result.append(val.get("id"))
    return result
def ListID_Categorias():
    peticion = requests.get("http://154.38.171.54:5502/categoriaActivos")
    data = peticion.json()
    result = []
    for val in data:
        result.append(val.get("id"))
    return result
def ListID_TipoActivos():
    peticion = requests.get("http://154.38.171.54:5502/categoriaActivos")
    data = peticion.json()
    result = []
    for val in data:
        result.append(val.get("id"))
    return result
def ListID_Estados():
    peticion = requests.get("http://154.38.171.54:5502/estados")
    data = peticion.json()
    result = []
    for val in data:
        result.append(val.get("id"))
    return result


# L I S T A _ A S I G N A C I O N E S
def ListID_ActivosAsignacion():
    peticion = requests.get("http://154.38.171.54:5502/activos")
    data = peticion.json()
    result = []
    for val in data:
        result.append(val.get("id"))
    return result