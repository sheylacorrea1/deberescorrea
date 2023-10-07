# Definimos el nombre del archivo
file_name = " my_notes.txt"

# Modo de apertura: "w" para escritura (write)
# Si el archivo no existe, se creará; si existe, se sobrescribirá
archivo = open(file_name, "w")

# Escribimos en el archivo
archivo.write("El mes de los enamorados es febrero\n")
archivo.write("Tenemos 4 meses de verano\n")
archivo.write("Los feriados nose trabajan")

# Cerramos el archivo para liberar recursos
archivo.close()

# Modo de apertura: "r" para lectura (read)
# Abrimos el archivo que acabamos de crear
archivo_lectura = open(file_name, "r")
archivo_lectura.seek(0)  # Reiniciamos el cursor al principio del archivo
linea_1 = archivo_lectura.readline()
linea_2 = archivo_lectura.readline()
linea_3 = archivo_lectura.readline()

print("\nContenido línea por línea usando readline():")
print(linea_1.strip())
print(linea_2.strip())
print(linea_3.strip())


# Cerramos el archivo después de leer
archivo.close()