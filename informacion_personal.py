informacion_personal = {
    "Nombre": "ALEX JARAMILLO",
    "Edad": 28,
    "Ciudad": "LOJA",
    "Profesion":"INGENIERO CIVIL"
}

informacion_personal["Ciudad"] = "LOJA"
informacion_personal["Profesion"] = "INGENIERO CIVIL"

# Verificar si "telefono" no está presente y luego agregarlo
if "Telefono" not in informacion_personal:
    informacion_personal["Telefono"] = "0985692011"

# Verificar si "edad" está presente y luego eliminarlo
if "Edad" in informacion_personal:
    del informacion_personal["Edad"]

print(informacion_personal)