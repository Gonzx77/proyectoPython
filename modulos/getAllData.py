import requests

def Cliente():
    peticion = requests.get("http://154.38.171.54:5501/activos")
    data = peticion.json()
    return data
def DetallePed():
    peticion = requests.get("http://154.38.171.54:5501/marcas")
    data = peticion.json()
    return data
def Empleado():
    peticion = requests.get("http://154.38.171.54:5501/categoriaActivos")
    data = peticion.json()
    return data
def Gama():
    peticion = requests.get("http://154.38.171.54:5501/tipoMovActivos")
    data = peticion.json()
    return data
def Oficina():
    peticion = requests.get("http://154.38.171.54:5501/estados")
    data = peticion.json()
    return data
def Pago():
    peticion = requests.get("http://154.38.171.54:5501/tipoActivos")
    data = peticion.json()
    return data
def Pedido():
    peticion = requests.get("http://154.38.171.54:5501/personas")
    data = peticion.json()
    return data
def Producto():
    peticion = requests.get("http://154.38.171.54:5501/zonas")
    data = peticion.json()
    return data