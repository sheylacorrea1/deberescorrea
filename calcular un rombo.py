def calcular_area_rombo(diagonal_mayor, diagonal_menor):
    """
    Calcula el área de un rombo.

    :param diagonal_mayor: Longitud de la diagonal mayor del rombo.
    :param diagonal_menor: Longitud de la diagonal menor del rombo.
    :return: El área del rombo.
    """
    area = (diagonal_mayor * diagonal_menor) / 2
    return area

# Solicitar al usuario las longitudes de las diagonales
diagonal_mayor = float(input("Ingresa la longitud de la diagonal mayor del rombo: "))
diagonal_menor = float(input("Ingresa la longitud de la diagonal menor del rombo: "))

# Calcular el área del rombo
area_rombo = calcular_area_rombo(diagonal_mayor, diagonal_menor)

# Mostrar el resultado
print(f"El área del rombo con diagonal mayor {diagonal_mayor} y diagonal menor {diagonal_menor} es: {area_rombo}")