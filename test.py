nombres = ["Juan", "María", "Carlos", "Ana", "Pedro", "Laura", "Diego", "Sofía", "Luis", "Elena"]
nombre_ingresado = input("Ingrese un nombre (parcial o completo): ")
coincidencias = [nombre for nombre in nombres if nombre_ingresado.lower() in nombre.lower()]

if coincidencias:
    print("Coincidencias encontradas:")
    for coincidencia in coincidencias:
        print(coincidencia)
else:
    print("No se encontraron coincidencias.")